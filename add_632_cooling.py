import re

with open('data.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Add missing Cooling Media part for 632-C-01
new_equipment = """  {
    id: '632-C-01-COOLING',
    tagNo: '632-C-01',
    description: 'Stabilizer Overhead Compressor',
    part: 'Cooling Media',
    package: 'JI2045-0-PFM102',
    type: LubricantType.COOLANT,
    grade: '15% Ethylene Glycol+85% Potable Water',
    initialFill: '1450 L',
    topUpQty: '50 L',
    topUpInterval: '360 hrs',
    replacementInterval: '-',
    brands: {},
    remarks: ''
  },"""

# Insert after 632-C-01
pattern = r"(id: '632-C-01',[\s\S]*?remarks: '[^']*'\s*},)"
match = re.search(pattern, content)

if match:
    content = content[:match.end()] + "\n" + new_equipment + content[match.end():]
    
    with open('data.ts', 'w', encoding='utf-8') as f:
        f.write(content)
    
    count = len(re.findall(r"  id: '", content))
    print(f"✅ تم إضافة Cooling Media لـ 632-C-01")
    print(f"📊 إجمالي المعدات: {count}")
else:
    print("❌ لم يتم العثور على 632-C-01")
