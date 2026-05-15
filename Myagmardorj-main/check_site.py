import re, os, sys

PLAT_NAV = ['/', '/intro.html', '/landscape.html', '/verify.html', '/roadmap.html', '/contact.html', '/paper1/']
P1_NAV = ['/paper1/', '/paper1/formalism.html', '/paper1/charts.html',
    '/paper1/calculator.html', '/paper1/lab.html', '/paper1/steven_clark.html',
    '/paper1/faq.html', '/paper1/methods.html', '/paper1/references.html',
    '/paper1/nulltests.html', '/paper1/livestats.html', '/paper1/roadmap.html',
    '/paper1/discussion.html', '/paper1/about.html', '/paper1/replication.html',
    '/paper1/data.html', '/paper1/changelog.html']

PLAT_FILES = ['contact.html','index.html','intro.html','landscape.html','roadmap.html','site-map.html','verify.html']
P1_FILES = [f'paper1/{f}' for f in ['about.html','calculator.html','changelog.html','charts.html',
    'data.html','discussion.html','faq.html','formalism.html','index.html','lab.html',
    'livestats.html','methods.html','nulltests.html','references.html','replication.html',
    'roadmap.html','steven_clark.html']]

def check(f, req):
    if not os.path.exists(f): return ['ФАЙЛ БАЙХГҮЙ']
    c = open(f, encoding='utf-8', errors='ignore').read()
    issues = []
    missing = [l for l in req if f'href="{l}"' not in c]
    if missing: issues.append(f'Nav дутуу: {missing}')
    if '.MN{' not in c: issues.append('.MN CSS байхгүй')
    if c.count('.MN{') > 1: issues.append(f'CSS давхардал {c.count(".MN{")}x')
    if 'setLang' not in c: issues.append('setLang байхгүй')
    if 'nav-fix.js' in c: issues.append('nav-fix.js байна')
    if '<body' not in c: issues.append('<body> байхгүй')
    if len(c) < 3000: issues.append(f'Контент бага ({len(c)}b)')
    idx = c.find('// ── NAV ACTIVE')
    if idx > 0:
        if len(re.findall(r'<script[^>]*>', c[:idx])) <= len(re.findall(r'</script>', c[:idx])):
            issues.append('Raw JS')
    return issues

print('\n' + '='*60)
print('  research.nexcore.ltd — вэбийн шалгуур')
print('='*60)
ok=0; fail=0
print('\n🟢 PLATFORM (6 nav links)')
for f in PLAT_FILES:
    iss = check(f, PLAT_NAV)
    if iss: print(f'  ❌ {f}'); [print(f'     → {i}') for i in iss]; fail+=1
    else: print(f'  ✅ {f}'); ok+=1
print('\n🟡 PAPER1 (17 nav links)')
for f in P1_FILES:
    iss = check(f, P1_NAV)
    if iss: print(f'  ❌ {f}'); [print(f'     → {i}') for i in iss]; fail+=1
    else: print(f'  ✅ {f}'); ok+=1
print('\n' + '='*60)
if fail==0: print(f'  ✅ БҮГД ЗӨВ — {ok}/24 — Push хийход бэлэн!')
else: print(f'  ❌ {fail} файлд алдаа байна ({ok}/24 зөв)')
print('='*60 + '\n')
sys.exit(0 if fail==0 else 1)
