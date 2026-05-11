-- ═══════════════════════════════════════════════
-- НОМИН Холдинг — Supabase Database Schema
-- Supabase SQL Editor дотор энэ скриптийг ажиллуулна уу
-- ═══════════════════════════════════════════════

-- 1. МЭДЭЭНИЙ ХҮСНЭГТ
create table if not exists nomin_news (
  id          bigint generated always as identity primary key,
  title_mn    text not null,
  sub_mn      text,
  body_mn     text,
  title_en    text,
  sub_en      text,
  body_en     text,
  title_ru    text,
  sub_ru      text,
  body_ru     text,
  category    text default 'Компанийн мэдээ',
  news_date   date,
  status      text default 'draft' check (status in ('published','draft','archived')),
  featured    boolean default false,
  image_url   text,
  created_at  timestamptz default now(),
  updated_at  timestamptz default now(),
  created_by  uuid references auth.users(id)
);

-- 2. АЖЛЫН БАЙРНЫ ХҮСНЭГТ
create table if not exists nomin_jobs (
  id          bigint generated always as identity primary key,
  title       text not null,
  department  text,
  location    text default 'Улаанбаатар',
  salary      text,
  job_type    text default 'Бүтэн цагийн',
  deadline    date,
  description text,
  status      text default 'open' check (status in ('open','closed')),
  created_at  timestamptz default now(),
  updated_at  timestamptz default now()
);

-- 3. ТЕНДЕРИЙН ХҮСНЭГТ
create table if not exists nomin_tenders (
  id              bigint generated always as identity primary key,
  title           text not null,
  organization    text,
  amount          text,
  published_date  date,
  deadline        date,
  description     text,
  status          text default 'open' check (status in ('open','closed')),
  created_at      timestamptz default now(),
  updated_at      timestamptz default now()
);

-- 4. ХУУДАСНЫ КОНТЕНТ ХҮСНЭГТ (optional)
create table if not exists nomin_pages (
  id          bigint generated always as identity primary key,
  page_key    text unique not null,
  label       text,
  h1_text     text,
  body_text   text,
  seo_title   text,
  seo_desc    text,
  updated_at  timestamptz default now()
);

-- ═══════════════════════════════════════════════
-- RLS (Row Level Security) тохиргоо
-- ═══════════════════════════════════════════════

-- Нийтэд унших боломжтой (PUBLIC READ)
alter table nomin_news    enable row level security;
alter table nomin_jobs    enable row level security;
alter table nomin_tenders enable row level security;
alter table nomin_pages   enable row level security;

-- Нийтлэгдсэн мэдээг хэн ч унших боломжтой
create policy "Public read published news"
  on nomin_news for select
  using (status = 'published');

-- Нэвтэрсэн хэрэглэгч бүгдийг харах боломжтой
create policy "Auth users read all news"
  on nomin_news for select
  to authenticated
  using (true);

-- Нэвтэрсэн хэрэглэгч бичих/засах/устгах
create policy "Auth users write news"
  on nomin_news for all
  to authenticated
  using (true);

-- Ажлын байр — нийтэд харагдана
create policy "Public read jobs"
  on nomin_jobs for select
  using (true);

create policy "Auth users write jobs"
  on nomin_jobs for all
  to authenticated
  using (true);

-- Тендер — нийтэд харагдана
create policy "Public read tenders"
  on nomin_tenders for select
  using (true);

create policy "Auth users write tenders"
  on nomin_tenders for all
  to authenticated
  using (true);

-- Хуудас
create policy "Auth users manage pages"
  on nomin_pages for all
  to authenticated
  using (true);

-- ═══════════════════════════════════════════════
-- ЖИШИГ ӨГӨГДӨЛ (SEED DATA)
-- ═══════════════════════════════════════════════
insert into nomin_news (title_mn, title_en, title_ru, sub_mn, category, news_date, status, featured)
values
  ('"Номин Холдинг" ХХК "Entrepreneur-2025"-аас Оны шилдэг аж ахуйн нэгжээр шалгарлаа',
   'Nomin Holding Named Company of the Year at Entrepreneur 2025',
   'АО «Номин Холдинг» — Компания года Entrepreneur 2025',
   'Монгол Улсын эдийн засгийн хөгжилд оруулж буй хувь нэмрийг бататгалаа.',
   'Шагнал', '2025-12-24', 'published', true),
  ('"ЦАЛГИМ ХАЛГИМ" — супер азтангуудаа хүлээн авлаа',
   'Tsalgim Halgim Promotion — Winners Announced',
   '«Цалгим Халгим» — победители объявлены',
   'Хайнанд аялах эрх болон iPhone 17 Pro Max зэрэг бэлгүүдийг гардан авлаа.',
   'Урамшуулал', '2026-03-13', 'published', false);

insert into nomin_jobs (title, department, location, salary, job_type, deadline, status)
values
  ('Маркетингийн менежер', 'Маркетинг хэлтэс', 'Улаанбаатар', '2,500,000—4,000,000 ₮', 'Бүтэн цагийн', '2026-04-30', 'open'),
  ('Програм хангамжийн инженер', 'IT хэлтэс', 'Улаанбаатар', '3,000,000—5,500,000 ₮', 'Бүтэн цагийн', '2026-04-15', 'open');

insert into nomin_tenders (title, organization, amount, published_date, deadline, status)
values
  ('IT тоног төхөөрөмж нийлүүлэлт', 'Номин Юнайтед', '320,000,000 ₮', '2026-03-01', '2026-04-30', 'open'),
  ('Барилгын материалын нийлүүлэлт', 'Номин Их Дэлгүүр', '500,000,000 ₮', '2026-03-15', '2026-05-15', 'open');
