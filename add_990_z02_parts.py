import re

# Read data.ts
with open('data.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# New equipment to add for 990-Z-02 missing parts
new_equipment = """  {
    id: '990-Z-02-SPLINE',
    tagNo: '990-Z-02',
    description: 'EOT Crane for Base Industrielle Well Engineering Workshop',
    part: 'Spline shaft cross travel',
    package: 'PFM113',
    type: LubricantType.GREASE,
    grade: 'ISO 2137',
    initialFill: '200 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '43200 hrs',
    brands: { bp: 'Energrease LS-EP2', shell: 'Alvania Grease EP2', mobil: 'Mobilux EP2', total: 'Multis EP2', naftal: 'Tessala EP2' },
    remarks: '1. Replace at overhaul. 2. Initial fill is by package vendor'
  },
  {
    id: '990-Z-02-SPRINGS',
    tagNo: '990-Z-02',
    description: 'EOT Crane for Base Industrielle Well Engineering Workshop',
    part: 'Springs on overload cut off',
    package: 'PFM113',
    type: LubricantType.GREASE,
    grade: 'ISO 2137',
    initialFill: '50 g',
    topUpQty: '50 g',
    topUpInterval: '8640 hrs',
    replacementInterval: '8640 hrs',
    brands: { bp: 'Energrease LS-EP2', shell: 'Alvania Grease EP2', mobil: 'Mobilux EP2', total: 'Multis EP2', naftal: 'Tessala EP2' },
    remarks: '1. Inspect/check at 12 month. 2. Initial fill is by package vendor'
  },"""

# Find position after last 990-Z-02 entry
pattern = r"(id: '990-Z-02-LT-MOTOR'[\s\S]*?remarks: '[^']*'\s*},)"
match = re.search(pattern, content)

if match:
    insert_pos = match.end()
    updated_content = content[:insert_pos] + "\n" + new_equipment + content[insert_pos:]
    
    with open('data.ts', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    count = len(re.findall(r"  id: '", updated_content))
    print(f"✅ تم إضافة 2 جزء لـ 990-Z-02")
    print(f"📊 إجمالي المعدات: {count}")
else:
    print("❌ لم يتم العثور على 990-Z-02-LT-MOTOR")
