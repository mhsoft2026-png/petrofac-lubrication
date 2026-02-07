import re

# Read current data.ts
with open('data.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# New equipment data for missing crane components
new_equipment = """  },
  {
    id: '750-Z-01-CROSS',
    tagNo: '750-Z-01',
    description: 'EOT Crane for Sales Gas Compressor Shelter',
    part: 'Cross Travel gearbox',
    package: 'PFM750',
    type: LubricantType.GREASE,
    grade: 'ISO 2137',
    initialFill: '200 g',
    topUpQty: '200 g',
    topUpInterval: '8640 hrs',
    replacementInterval: '43200 hrs',
    brands: { bp: "Energrease LS-EP2", shell: "Alvania Grease EP2", mobil: "Mobilux EP2", total: "Multis EP2", naftal: "Tessala EP2" },
    remarks: '1. Inspect/check 12 month Replace at overhaul. 2. Initial fill is by package vendor'
  },
  {
    id: '750-Z-01-LONG',
    tagNo: '750-Z-01',
    description: 'EOT Crane for Sales Gas Compressor Shelter',
    part: 'Long Travel gearbox',
    package: 'PFM750',
    type: LubricantType.OIL,
    grade: 'ISO VG 460',
    initialFill: '1 L',
    topUpQty: '0.25 L',
    topUpInterval: '8640 hrs',
    replacementInterval: '43200 hrs',
    brands: { bp: "Energol GR XP460", shell: "Omala Oil 460", mobil: "Mobilgear 634", total: "Carter EP 460", naftal: "Fodda 460" },
    remarks: '1. Inspect/check 12 month Replace at overhaul. 2. Initial fill is by package vendor'
  },
  {
    id: '810-Z-01-CROSS',
    tagNo: '810-Z-01',
    description: 'EOT Crane for Gas Turbine Generator Building',
    part: 'Cross Travel gearbox',
    package: 'PFM810',
    type: LubricantType.GREASE,
    grade: 'ISO 2137',
    initialFill: '200 g',
    topUpQty: '200 g',
    topUpInterval: '8640 hrs',
    replacementInterval: '43200 hrs',
    brands: { bp: "Energrease LS-EP2", shell: "Alvania Grease EP2", mobil: "Mobilux EP2", total: "Multis EP2", naftal: "Tessala EP2" },
    remarks: '1. Inspect/check 12 month Replace at overhaul. 2. Initial fill is by package vendor'
  },
  {
    id: '810-Z-01-LONG',
    tagNo: '810-Z-01',
    description: 'EOT Crane for Gas Turbine Generator Building',
    part: 'Long Travel gearbox',
    package: 'PFM810',
    type: LubricantType.OIL,
    grade: 'ISO VG 460',
    initialFill: '1 L',
    topUpQty: '0.25 L',
    topUpInterval: '8640 hrs',
    replacementInterval: '43200 hrs',
    brands: { bp: "Energol GR XP460", shell: "Omala Oil 460", mobil: "Mobilgear 634", total: "Carter EP 460", naftal: "Fodda 460" },
    remarks: '1. Inspect/check 12 month Replace at overhaul. 2. Initial fill is by package vendor'
  },
  {
    id: '990-Z-01-CROSS',
    tagNo: '990-Z-01',
    description: 'EOT Crane for Warehouse',
    part: 'Cross Travel gearbox',
    package: 'PFM990',
    type: LubricantType.GREASE,
    grade: 'ISO 2137',
    initialFill: '200 g',
    topUpQty: '200 g',
    topUpInterval: '8640 hrs',
    replacementInterval: '43200 hrs',
    brands: { bp: "Energrease LS-EP2", shell: "Alvania Grease EP2", mobil: "Mobilux EP2", total: "Multis EP2", naftal: "Tessala EP2" },
    remarks: '1. Inspect/check 12 month Replace at overhaul. 2. Initial fill is by package vendor'
  },
  {
    id: '990-Z-01-LONG',
    tagNo: '990-Z-01',
    description: 'EOT Crane for Warehouse',
    part: 'Long Travel gearbox',
    package: 'PFM990',
    type: LubricantType.OIL,
    grade: 'ISO VG 460',
    initialFill: '1 L',
    topUpQty: '0.25 L',
    topUpInterval: '8640 hrs',
    replacementInterval: '43200 hrs',
    brands: { bp: "Energol GR XP460", shell: "Omala Oil 460", mobil: "Mobilgear 634", total: "Carter EP 460", naftal: "Fodda 460" },
    remarks: '1. Inspect/check 12 month Replace at overhaul. 2. Initial fill is by package vendor'
  }
];
"""

# Replace the closing bracket with new equipment
content = content.replace('  }\n];', new_equipment)

# Write updated content
with open('data.ts', 'w', encoding='utf-8') as f:
    f.write(content)

# Count equipment
equipment_count = len(re.findall(r"  id: '", content))
print(f"✅ تم إضافة 6 معدات رافعات جديدة (750-Z-01, 810-Z-01, 990-Z-01)")
print(f"✅ إجمالي المعدات الآن: {equipment_count}")
