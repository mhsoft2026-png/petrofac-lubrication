import re

with open('data.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Add missing parts for 441-P-53A and 441-P-53B
new_equipment = """  {
    id: '441-P-53A-HYDRAULIC',
    tagNo: '441-P-53A',
    description: 'Emulsion Breaker Dosing Pump',
    part: 'Hydraulic Side',
    package: 'PFA441',
    type: LubricantType.OIL,
    grade: 'ISO VG 10',
    initialFill: '0.76 L',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '4000 hrs',
    brands: { bp: 'ENERGOL HP10', shell: 'Shell Morlina S2 BL 10', mobil: 'Mobil Velocite No. 6', other: 'ROL OIL LI/10' },
    remarks: 'Initial fill is by package vendor'
  },
  {
    id: '441-P-53A-MECHANISM',
    tagNo: '441-P-53A',
    description: 'Emulsion Breaker Dosing Pump',
    part: 'Mechanism',
    package: 'PFA441',
    type: LubricantType.OIL,
    grade: 'ISO VG 320',
    initialFill: '0.6 L',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '1500 hrs',
    brands: { other: 'ENERSYN SG 320 / ENERSYN SG XP 320 / TIVELA OIL S320 / GLYCOYLE HE320 / ROL OIL SINCAT 320' },
    remarks: 'Initial fill is by package vendor'
  },
  {
    id: '441-P-53B-HYDRAULIC',
    tagNo: '441-P-53B',
    description: 'Emulsion Breaker Dosing Pump',
    part: 'Hydraulic Side',
    package: 'PFA441',
    type: LubricantType.OIL,
    grade: 'ISO VG 10',
    initialFill: '0.76 L',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '4000 hrs',
    brands: { bp: 'ENERGOL HP10', shell: 'Shell Morlina S2 BL 10', mobil: 'Mobil Velocite No. 6', other: 'ROL OIL LI/10' },
    remarks: 'Initial fill is by package vendor'
  },
  {
    id: '441-P-53B-MECHANISM',
    tagNo: '441-P-53B',
    description: 'Emulsion Breaker Dosing Pump',
    part: 'Mechanism',
    package: 'PFA441',
    type: LubricantType.OIL,
    grade: 'ISO VG 320',
    initialFill: '0.6 L',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '1500 hrs',
    brands: { other: 'ENERSYN SG 320 / ENERSYN SG XP 320 / TIVELA OIL S320 / GLYCOYLE HE320 / ROL OIL SINCAT 320' },
    remarks: 'Initial fill is by package vendor'
  },"""

# Insert after 441-P-53B
pattern = r"(id: '441-P-53B',[\s\S]*?remarks: '[^']*'\s*},)"
match = re.search(pattern, content)

if match:
    content = content[:match.end()] + "\n" + new_equipment + content[match.end():]
    
    with open('data.ts', 'w', encoding='utf-8') as f:
        f.write(content)
    
    count = len(re.findall(r"  id: '", content))
    print(f"✅ تم إضافة 4 أجزاء لـ 441-P-53A/B")
    print(f"📊 إجمالي المعدات: {count}")
else:
    print("❌ لم يتم العثور على 441-P-53B")
