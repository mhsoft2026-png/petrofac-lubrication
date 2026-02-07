import re

# Read data.ts
with open('data.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Additional parts for 441-P-03A and 441-P-03B
new_equipment = """  {
    id: '441-P-03A-PUMP-JOINT',
    tagNo: '441-P-03A',
    description: 'Waste Oil Pump',
    part: 'Pump Joint',
    package: 'PFA441',
    type: LubricantType.OIL,
    grade: 'ISO VG 460',
    initialFill: '0.01 L',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '4000 hrs',
    brands: { other: 'Castrol - Tribol ET1510 ISO 460 / Allweller Type B' },
    remarks: 'Initial fill is by package vendor'
  },
  {
    id: '441-P-03A-GEAR',
    tagNo: '441-P-03A',
    description: 'Waste Oil Pump',
    part: 'Gear Unit',
    package: 'PFA441',
    type: LubricantType.OIL,
    grade: 'CLP VG 220',
    initialFill: '0.65 L',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '4000 hrs',
    brands: { other: 'Castrol-Alphasyn EP 220 / ENI BLASIA 220' },
    remarks: 'Initial fill is by package vendor'
  },
  {
    id: '441-P-03B-PUMP-JOINT',
    tagNo: '441-P-03B',
    description: 'Waste Oil Pump',
    part: 'Pump Joint',
    package: 'PFA441',
    type: LubricantType.OIL,
    grade: 'ISO VG 460',
    initialFill: '0.01 L',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '4000 hrs',
    brands: { other: 'Castrol - Tribol ET1510 ISO 460 / Allweller Type B' },
    remarks: 'Initial fill is by package vendor'
  },
  {
    id: '441-P-03B-GEAR',
    tagNo: '441-P-03B',
    description: 'Waste Oil Pump',
    part: 'Gear Unit',
    package: 'PFA441',
    type: LubricantType.OIL,
    grade: 'CLP VG 220',
    initialFill: '0.65 L',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '4000 hrs',
    brands: { other: 'Castrol-Alphasyn EP 220 / ENI BLASIA 220' },
    remarks: 'Initial fill is by package vendor'
  },"""

# Find position after 441-P-03B-MOTOR
pattern = r"(id: '441-P-03B-MOTOR'[\s\S]*?remarks: '[^']*'\s*},)"
match = re.search(pattern, content)

if match:
    insert_pos = match.end()
    updated_content = content[:insert_pos] + "\n" + new_equipment + content[insert_pos:]
    
    with open('data.ts', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    count = len(re.findall(r"  id: '", updated_content))
    print(f"✅ تم إضافة 4 أجزاء لـ 441-P-03A/B (Pump Joint + Gear Unit)")
    print(f"📊 إجمالي المعدات: {count}")
else:
    print("❌ لم يتم العثور على 441-P-03B-MOTOR")
