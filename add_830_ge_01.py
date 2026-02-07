import re

# Read data.ts
with open('data.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# New equipment to add
new_equipment = """  {
    id: '830-GE-01',
    tagNo: '830-GE-01',
    description: 'Generator',
    part: 'Bearings',
    package: 'JI2045-0-PFM105',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '80 g (DE) / 70 g (NDE)',
    topUpQty: '30 g',
    topUpInterval: '4320 hrs',
    replacementInterval: '8640 hrs',
    brands: { bp: 'ENER LS2', shell: 'GADUS S2 V220 2', mobil: 'Mobilux EP2', total: 'MULTIS EP2', naftal: 'TESSALA EP2' },
    remarks: ''
  },"""

# Find position right before 830-GE-02
pattern = r"(\s+{[\s\S]*?id: '830-GE-02')"
replacement = new_equipment + r"\n\1"

# Replace
updated_content = re.sub(pattern, replacement, content, count=1)

# Write back
with open('data.ts', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print("✅ تم إضافة 830-GE-01")
