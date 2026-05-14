"""
rebuild_nav.py — NAV ШИНЭЧЛЭГЧ
================================
Ажиллуулах: python rebuild_nav.py
Хийдэг зүйл:
  1. nav_template.py-с template уншина
  2. Бүх 24 HTML файлаас хуучин nav/footer устгана
  3. Шинэ template суулгана
  4. check_site.py-р шалгана
"""
import re, os, sys
from nav_template import (NAV_CSS, NAV_JS, PLAT_NAV, PLAT_FOOT,
                           P1_NAV, P1_FOOT, PLAT_FILES, P1_FILES)

def get_body_content(filepath):
    c = open(filepath, encoding='utf-8', errors='ignore').read()
    body = re.search(r'<body[^>]*>(.*)</body>', c, re.DOTALL)
    if not body: return ''
    content = body.group(1)
    content = re.sub(r'<nav[^>]*>[\s\S]*?</nav>\s*', '', content)
    content = re.sub(r'<div[^>]*class=["\'][^"\']*MN-mob[^"\']*["\'][^>]*>[\s\S]*?</div>\s*', '', content)
    content = re.sub(r'<footer[^>]*>[\s\S]*?</footer>\s*', '', content)
    content = re.sub(r'<script[^>]*>\s*\(function\(\)\{[\s\S]*?setLang[\s\S]*?\}\)\(\);\s*</script>\s*', '', content)
    return content.strip()

def get_head_extras(filepath):
    c = open(filepath, encoding='utf-8', errors='ignore').read()
    head = re.search(r'<head[^>]*>(.*?)</head>', c, re.DOTALL)
    if not head: return '', '', []
    h = head.group(1)
    title = re.search(r'<title[^>]*>.*?</title>', h, re.DOTALL)
    title = title.group(0) if title else '<title>research.nexcore.ltd</title>'
    links = [l for l in re.findall(r'<link[^>]+>', h)
             if 'nav-fix' not in l and ('font' in l or 'icon' in l)]
    styles = []
    for m in re.finditer(r'<style[^>]*>(.*?)</style>', h, re.DOTALL):
        s = m.group(1)
        if any(x in s for x in ['.MN{', 'MN-logo', 'MN-links', 'data-li']): continue
        if s.strip(): styles.append(f'<style>{s.strip()}</style>')
    return title, '\n'.join(links), styles

def rebuild(filepath, nav, foot):
    body = get_body_content(filepath)
    title, links, styles = get_head_extras(filepath)
    html = f'''<!DOCTYPE html>
<html lang="mn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
{title}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600&family=Plus+Jakarta+Sans:wght@400;500&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
{links}
{''.join(styles)}
<style>{NAV_CSS}</style>
</head>
<body class="en">
{nav}
{body}
{foot}
{NAV_JS}
</body>
</html>'''
    open(filepath, 'w', encoding='utf-8').write(html)
    return len(body)

if __name__ == '__main__':
    print('\n🔨 Nav шинэчилж байна...\n')
    ok = fail = 0
    for f in PLAT_FILES:
        if not os.path.exists(f): print(f'  ⚠️  {f} байхгүй'); continue
        n = rebuild(f, PLAT_NAV, PLAT_FOOT)
        print(f'  {"✅" if n>200 else "⚠️ "} {f} ({n:,} chars)')
        if n > 200: ok += 1
        else: fail += 1
    for f in P1_FILES:
        if not os.path.exists(f): print(f'  ⚠️  {f} байхгүй'); continue
        n = rebuild(f, P1_NAV, P1_FOOT)
        print(f'  {"✅" if n>200 else "⚠️ "} {f} ({n:,} chars)')
        if n > 200: ok += 1
        else: fail += 1
    print(f'\n{"="*50}')
    print(f'✅ {ok}/24 файл шинэчлэгдлээ')
    if fail: print(f'⚠️  {fail} файлд контент бага байна')
    print('Одоо: python check_site.py')
    print('="'*25)
