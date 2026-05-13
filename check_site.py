"""
check_site.py — research.nexcore.ltd вэбийн шалгуур
Хэрэглэх: python check_site.py
Байршил: C:\Myagmardorj\check_site.py
"""
import re, os, sys

# ── Mapping ──
PLAT_NAV  = ['/', '/intro.html', '/landscape.html', '/verify.html', '/paper1/']
P1_NAV    = ['/paper1/', '/paper1/formalism.html', '/paper1/charts.html',
             '/paper1/calculator.html', '/paper1/lab.html', '/paper1/steven_clark.html',
             '/paper1/faq.html', '/paper1/methods.html', '/paper1/references.html',
             '/paper1/nulltests.html', '/paper1/livestats.html', '/paper1/roadmap.html',
             '/paper1/discussion.html', '/paper1/about.html']

PLAT_FILES = ['contact.html','index.html','intro.html','landscape.html',
              'roadmap.html','site-map.html','verify.html']
P1_FILES   = ['paper1/about.html','paper1/calculator.html','paper1/changelog.html',
              'paper1/charts.html','paper1/data.html','paper1/discussion.html',
              'paper1/faq.html','paper1/formalism.html','paper1/index.html',
              'paper1/lab.html','paper1/livestats.html','paper1/methods.html',
              'paper1/nulltests.html','paper1/references.html','paper1/replication.html',
              'paper1/roadmap.html','paper1/steven_clark.html']

# ── Check function ──
def check(filepath, req_nav):
    if not os.path.exists(filepath):
        return [f'ФАЙЛ БАЙХГҮЙ']
    c = open(filepath, encoding='utf-8', errors='ignore').read()
    issues = []

    # 1. Nav links
    missing = [l for l in req_nav if f'href="{l}"' not in c]
    if missing:
        issues.append(f'Nav дутуу: {missing}')

    # 2. Nav CSS
    if '.MN{' not in c and '.MN {' not in c:
        issues.append('.MN CSS байхгүй')

    # 3. CSS давхардал
    dup = c.count('.MN{') + c.count('.MN {')
    if dup > 1:
        issues.append(f'CSS давхардал {dup}x')

    # 4. setLang
    if 'setLang' not in c:
        issues.append('setLang байхгүй')

    # 5. nav-fix.js
    if 'nav-fix.js' in c:
        issues.append('nav-fix.js reference байна')

    # 6. Raw JS (script tag-гүй)
    for marker in ['// ── NAV ACTIVE', 'function cleanPath']:
        idx = c.find(marker)
        if idx > 0:
            opens  = len(re.findall(r'<script[^>]*>', c[:idx]))
            closes = len(re.findall(r'</script>',    c[:idx]))
            if opens <= closes:
                issues.append(f'Raw JS: {marker[:25]}')
            break

    # 7. <body> байгаа эсэх
    if '<body' not in c:
        issues.append('<body> байхгүй')

    # 8. Контент хэмжээ
    if len(c) < 5000:
        issues.append(f'Контент хэт бага ({len(c)}b)')

    # 9. CSS selector bug
    if re.search(r'nav/\*.*?\*/\s*\.MN', c, re.DOTALL):
        issues.append('nav/* CSS bug')

    return issues

# ── Run ──
print()
print('=' * 60)
print('  research.nexcore.ltd — вэбийн шалгуур')
print('=' * 60)

all_files = [(f, PLAT_NAV) for f in PLAT_FILES] + \
            [(f, P1_NAV)   for f in P1_FILES]

ok = 0; fail = 0

print('\n🟢 PLATFORM')
for f in PLAT_FILES:
    issues = check(f, PLAT_NAV)
    if issues:
        print(f'  ❌ {f}')
        for i in issues: print(f'     → {i}')
        fail += 1
    else:
        print(f'  ✅ {f}')
        ok += 1

print('\n🟡 PAPER1')
for f in P1_FILES:
    issues = check(f, P1_NAV)
    if issues:
        print(f'  ❌ {f}')
        for i in issues: print(f'     → {i}')
        fail += 1
    else:
        print(f'  ✅ {f}')
        ok += 1

print()
print('=' * 60)
if fail == 0:
    print(f'  ✅ БҮГД ЗӨВ — {ok}/{ok+fail} файл — Push хийход бэлэн!')
else:
    print(f'  ❌ {fail} файлд алдаа байна ({ok}/{ok+fail} зөв)')
    print(f'  Дээрх алдааг засаад дахин ажиллуул.')
print('=' * 60)
print()

sys.exit(0 if fail == 0 else 1)
