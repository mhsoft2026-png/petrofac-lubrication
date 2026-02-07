import re

# Read current data.ts
with open('data.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# New equipment data for additional crane components
new_equipment = """  },
  {
    id: '750-Z-01-EX-PANEL',
    tagNo: '750-Z-01',
    description: 'EOT Crane for Sales Gas Compressor Shelter',
    part: 'Ex control panel enclosure',
    package: 'PFM750',
    type: LubricantType.GREASE,
    grade: 'ISO 2137 (Copper Grease)',
    initialFill: '100 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '8640 hrs',
    brands: { other: "3 In One Anti-Seize Copper Grease / Fuchs-PBC/DGrease Anti-Seize" },
    remarks: '1. Inspect/check/ clean & relube Ex gap at 12 month. 2. Initial fill is by package vendor'
  },
  {
    id: '750-Z-01-CT-MOTOR',
    tagNo: '750-Z-01',
    description: 'EOT Crane for Sales Gas Compressor Shelter',
    part: 'C.T. Motor Bearings',
    package: 'PFM750',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {},
    remarks: 'Greased For Life'
  },
  {
    id: '810-Z-01-SPLINE',
    tagNo: '810-Z-01',
    description: 'EOT Crane for Gas Turbine Generator Building',
    part: 'Spline shaft cross travel',
    package: 'PFM810',
    type: LubricantType.GREASE,
    grade: 'ISO 2137',
    initialFill: '200 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '43200 hrs',
    brands: { bp: "Energrease LS-EP2", shell: "Alvania Grease EP2", mobil: "Mobilux EP2", total: "Multis EP2", naftal: "Tessala EP2" },
    remarks: '1. Replace at overhaul. 2. Initial fill is by package vendor'
  },
  {
    id: '810-Z-01-SPRINGS',
    tagNo: '810-Z-01',
    description: 'EOT Crane for Gas Turbine Generator Building',
    part: 'Springs on overload cut off',
    package: 'PFM810',
    type: LubricantType.GREASE,
    grade: 'ISO 2137',
    initialFill: '50 g',
    topUpQty: '50 g',
    topUpInterval: '8640 hrs',
    replacementInterval: '8640 hrs',
    brands: { bp: "Energrease LS-EP2", shell: "Alvania Grease EP2", mobil: "Mobilux EP2", total: "Multis EP2", naftal: "Tessala EP2" },
    remarks: '1. Inspect/check at 12 month. 2. Initial fill is by package vendor'
  },
  {
    id: '990-Z-01-SPLINE',
    tagNo: '990-Z-01',
    description: 'EOT Crane for Warehouse',
    part: 'Spline shaft cross travel',
    package: 'PFM990',
    type: LubricantType.GREASE,
    grade: 'ISO 2137',
    initialFill: '200 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '43200 hrs',
    brands: { bp: "Energrease LS-EP2", shell: "Alvania Grease EP2", mobil: "Mobilux EP2", total: "Multis EP2", naftal: "Tessala EP2" },
    remarks: '1. Replace at overhaul. 2. Initial fill is by package vendor'
  },
  {
    id: '990-Z-01-SPRINGS',
    tagNo: '990-Z-01',
    description: 'EOT Crane for Warehouse',
    part: 'Springs on overload cut off',
    package: 'PFM990',
    type: LubricantType.GREASE,
    grade: 'ISO 2137',
    initialFill: '50 g',
    topUpQty: '50 g',
    topUpInterval: '8640 hrs',
    replacementInterval: '8640 hrs',
    brands: { bp: "Energrease LS-EP2", shell: "Alvania Grease EP2", mobil: "Mobilux EP2", total: "Multis EP2", naftal: "Tessala EP2" },
    remarks: '1. Inspect/check at 12 month. 2. Initial fill is by package vendor'
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
print(f"✅ تم إضافة 6 معدات رافعات إضافية (Splines, Springs, Ex Panel)")
print(f"✅ إجمالي المعدات الآن: {equipment_count}")
