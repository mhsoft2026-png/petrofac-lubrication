import re

with open('data.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Add missing parts for 441-M-51 and 441-M-52
new_equipment_m51 = """  {
    id: '441-M-51-BEARING',
    tagNo: '441-M-51',
    description: 'Recovered Oil Pit Mixer',
    part: 'Bearing',
    package: 'PFA441',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '20 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '4000 hrs',
    brands: { shell: 'Shell Gadus S2 V220 2', total: 'AGIP GR MU 3' },
    remarks: 'Initial fill is by package vendor'
  },
  {
    id: '441-M-51-MOTOR',
    tagNo: '441-M-51',
    description: 'Recovered Oil Pit Mixer',
    part: 'Motor Bearing',
    package: 'PFA441',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {},
    remarks: 'Greased For Life'
  },"""

new_equipment_m52 = """  {
    id: '441-M-52-BEARING',
    tagNo: '441-M-52',
    description: 'Recovered Oil Pit Mixer',
    part: 'Bearing',
    package: 'PFA441',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '20 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '4000 hrs',
    brands: { shell: 'Shell Gadus S2 V220 2', total: 'AGIP GR MU 3' },
    remarks: 'Initial fill is by package vendor'
  },
  {
    id: '441-M-52-MOTOR',
    tagNo: '441-M-52',
    description: 'Recovered Oil Pit Mixer',
    part: 'Motor Bearing',
    package: 'PFA441',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {},
    remarks: 'Greased For Life'
  },"""

# Insert after 441-M-51
pattern1 = r"(id: '441-M-51',[\s\S]*?remarks: '[^']*'\s*},)"
match1 = re.search(pattern1, content)
if match1:
    content = content[:match1.end()] + "\n" + new_equipment_m51 + content[match1.end():]
    print("✅ تم إضافة جزئين لـ 441-M-51")

# Insert after 441-M-52
pattern2 = r"(id: '441-M-52',[\s\S]*?remarks: '[^']*'\s*},)"
match2 = re.search(pattern2, content)
if match2:
    content = content[:match2.end()] + "\n" + new_equipment_m52 + content[match2.end():]
    print("✅ تم إضافة جزئين لـ 441-M-52")

with open('data.ts', 'w', encoding='utf-8') as f:
    f.write(content)

count = len(re.findall(r"  id: '", content))
print(f"📊 إجمالي المعدات: {count}")
