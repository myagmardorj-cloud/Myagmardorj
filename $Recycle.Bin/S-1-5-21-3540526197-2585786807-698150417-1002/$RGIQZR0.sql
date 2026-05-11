-- ═══════════════════════════════════════════════════════════════════════════
-- STEP12_FIX_STORAGE_POLICIES.sql
-- Supabase Storage (media bucket)-ын upload эрхийг засна
-- ═══════════════════════════════════════════════════════════════════════════

-- ─────────────────────────────────────────
-- 1. media bucket үүсгэх (хэрэв байхгүй бол)
-- ─────────────────────────────────────────
INSERT INTO storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
VALUES (
  'media',
  'media',
  true,  -- public хандалттай
  52428800,  -- 50 MB
  ARRAY[
    'image/jpeg', 'image/png', 'image/webp', 'image/gif', 'image/svg+xml',
    'application/pdf',
    'video/mp4', 'video/webm',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
  ]
)
ON CONFLICT (id) DO UPDATE
SET public = true,
    file_size_limit = 52428800,
    allowed_mime_types = EXCLUDED.allowed_mime_types;

-- ─────────────────────────────────────────
-- 2. Хуучин бүх policies устгах
-- ─────────────────────────────────────────
DROP POLICY IF EXISTS "public_read_media" ON storage.objects;
DROP POLICY IF EXISTS "anon_upload_media" ON storage.objects;
DROP POLICY IF EXISTS "auth_upload_media" ON storage.objects;
DROP POLICY IF EXISTS "auth_update_media" ON storage.objects;
DROP POLICY IF EXISTS "auth_delete_media" ON storage.objects;
DROP POLICY IF EXISTS "Give users authenticated access to folder" ON storage.objects;
DROP POLICY IF EXISTS "public_access_media" ON storage.objects;

-- ─────────────────────────────────────────
-- 3. Шинэ policies үүсгэх
-- ─────────────────────────────────────────

-- 🌐 Хэн ч унших боломжтой (public read)
CREATE POLICY "public_read_media"
ON storage.objects FOR SELECT
TO anon, authenticated
USING (bucket_id = 'media');

-- 📤 Anon хэрэглэгч upload хийж болно (админ нэвтрээгүй ч гэсэн ажиллана)
-- Учир: админ панел нь anon key ашигладаг
CREATE POLICY "anon_upload_media"
ON storage.objects FOR INSERT
TO anon, authenticated
WITH CHECK (bucket_id = 'media');

-- ✏️ Anon хэрэглэгч update хийж болно (overwrite)
CREATE POLICY "anon_update_media"
ON storage.objects FOR UPDATE
TO anon, authenticated
USING (bucket_id = 'media')
WITH CHECK (bucket_id = 'media');

-- 🗑 Anon хэрэглэгч устгаж болно
CREATE POLICY "anon_delete_media"
ON storage.objects FOR DELETE
TO anon, authenticated
USING (bucket_id = 'media');

-- ─────────────────────────────────────────
-- 4. Үр дүн шалгах
-- ─────────────────────────────────────────
SELECT 
  policyname AS "Policy нэр",
  cmd AS "Үйлдэл",
  CASE 
    WHEN 'anon' = ANY(roles::text[]) THEN '🌐 Anon'
    ELSE '🔒 Auth only'
  END AS "Эрх"
FROM pg_policies
WHERE schemaname = 'storage' AND tablename = 'objects'
  AND policyname LIKE '%media%'
ORDER BY cmd, policyname;

-- Bucket шалгах
SELECT 
  id, 
  name, 
  CASE WHEN public THEN '🌐 Public' ELSE '🔒 Private' END AS access,
  (file_size_limit/1024/1024)::TEXT || ' MB' AS "Max size"
FROM storage.buckets
WHERE id = 'media';
