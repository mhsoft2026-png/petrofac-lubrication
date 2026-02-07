import re

with open('data.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Add missing 480-P-01B
new_equipment = """  {
    id: '480-P-01B',
    tagNo: '480-P-01B',
    description: 'Methanol Injection Pump',
    part: 'Bearing',
    package: 'PFA480',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {},
    remarks: 'Greased For Life'
  },
  {
    id: '480-PM-01B',
    tagNo: '480-PM-01B',
    description: 'Methanol Injection Pump Motor',
    part: 'Bearing',
    package: 'PFA480',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {},
    remarks: 'Greased For Life'
  },"""

# Insert after 480-PM-01A
pattern = r"(id: '480-PM-01A',[\s\S]*?remarks: '[^']*'\s*},)"
match = re.search(pattern, content)

if match:
    content = content[:match.end()] + "\n" + new_equipment + content[match.end():]
    
    with open('data.ts', 'w', encoding='utf-8') as f:
        f.write(content)
    
    count = len(re.findall(r"  id: '", content))
    print(f"✅ تم إضافة 480-P-01B و 480-PM-01B")
    print(f"📊 إجمالي المعدات: {count}")
else:
    print("❌ لم يتم العثور على 480-PM-01A")
