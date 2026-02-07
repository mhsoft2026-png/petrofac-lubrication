import re

# Read current data.ts
with open('data.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last equipment entry
if '}' not in content or '];' not in content:
    print("Error: Could not find the end of the equipment array")
    exit(1)

# New equipment data for Fire Water System (Package 450)
new_equipment = """  },
  {
    id: '450-P-02A',
    tagNo: '450-P-02A',
    description: 'Fire Water Pump (Motor Driven)',
    part: 'Bearing',
    package: 'PFA450',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '100 g',
    topUpQty: '50 g',
    topUpInterval: '4320 hrs',
    replacementInterval: '8640 hrs',
    brands: ['ENER LS2', 'GADUS S2 V220 2', 'Mobilux EP2', 'MULTIS EP2', 'TESSALA EP2'],
    remarks: '-'
  },
  {
    id: '450-P-02B',
    tagNo: '450-P-02B',
    description: 'Fire Water Pump (Motor Driven)',
    part: 'Bearing',
    package: 'PFA450',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '100 g',
    topUpQty: '50 g',
    topUpInterval: '4320 hrs',
    replacementInterval: '8640 hrs',
    brands: ['ENER LS2', 'GADUS S2 V220 2', 'Mobilux EP2', 'MULTIS EP2', 'TESSALA EP2'],
    remarks: '-'
  },
  {
    id: '450-PM-02A',
    tagNo: '450-PM-02A',
    description: 'Fire Water Pump Motor',
    part: 'Bearing',
    package: 'PFA450',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '105 g',
    topUpQty: '50 g',
    topUpInterval: '4320 hrs',
    replacementInterval: '8640 hrs',
    brands: ['ENER LS2', 'GADUS S2 V220 2', 'POLYREX EM', 'MULTIS EP2', 'TESSALA EP2'],
    remarks: '-'
  },
  {
    id: '450-PM-02B',
    tagNo: '450-PM-02B',
    description: 'Fire Water Pump Motor',
    part: 'Bearing',
    package: 'PFA450',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '105 g',
    topUpQty: '50 g',
    topUpInterval: '4320 hrs',
    replacementInterval: '8640 hrs',
    brands: ['ENER LS2', 'GADUS S2 V220 2', 'POLYREX EM', 'MULTIS EP2', 'TESSALA EP2'],
    remarks: '-'
  },
  {
    id: '450-P-03A',
    tagNo: '450-P-03A',
    description: 'Fire Water Pump (Diesel Engine Driven)',
    part: 'Bearing',
    package: 'PFA450',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '100 g',
    topUpQty: '50 g',
    topUpInterval: '4320 hrs',
    replacementInterval: '8640 hrs',
    brands: ['ENER LS2', 'GADUS S2 V220 2', 'Mobilux EP2', 'MULTIS EP2', 'TESSALA EP2'],
    remarks: '-'
  },
  {
    id: '450-P-03B',
    tagNo: '450-P-03B',
    description: 'Fire Water Pump (Diesel Engine Driven)',
    part: 'Bearing',
    package: 'PFA450',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '100 g',
    topUpQty: '50 g',
    topUpInterval: '4320 hrs',
    replacementInterval: '8640 hrs',
    brands: ['ENER LS2', 'GADUS S2 V220 2', 'Mobilux EP2', 'MULTIS EP2', 'TESSALA EP2'],
    remarks: '-'
  },
  {
    id: '450-PD-03A-OIL',
    tagNo: '450-PD-03A',
    description: 'Fire Water Pump Diesel Engine',
    part: 'Oil Pan',
    package: 'PFA450',
    type: LubricantType.OIL,
    grade: 'SAE 15W-40 API CJ-4 / CK-4',
    initialFill: '45 L',
    topUpQty: '8 L',
    topUpInterval: '4320 hrs',
    replacementInterval: '8640 hrs',
    brands: ['BP VANELLUS MULTI-FLEET', 'VALVOLINE PREMIUM BLUE', 'Rotella T5', 'Delvac', 'RUBIA TIR 7400', 'CHEVIA VP SUPER DIESEL'],
    remarks: '-'
  },
  {
    id: '450-PD-03B-OIL',
    tagNo: '450-PD-03B',
    description: 'Fire Water Pump Diesel Engine',
    part: 'Oil Pan',
    package: 'PFA450',
    type: LubricantType.OIL,
    grade: 'SAE 15W-40 API CJ-4 / CK-4',
    initialFill: '45 L',
    topUpQty: '8 L',
    topUpInterval: '4320 hrs',
    replacementInterval: '8640 hrs',
    brands: ['BP VANELLUS MULTI-FLEET', 'VALVOLINE PREMIUM BLUE', 'Rotella T5', 'Delvac', 'RUBIA TIR 7400', 'CHEVIA VP SUPER DIESEL'],
    remarks: '-'
  },
  {
    id: '450-PD-03A-COOLANT',
    tagNo: '450-PD-03A',
    description: 'Fire Water Pump Diesel Engine',
    part: 'Heat Exchanger (Engine Coolant)',
    package: 'PFA450',
    type: LubricantType.OIL,
    grade: 'ASTM D6210 (50%Glycol+50%Potable Water)',
    initialFill: '52.6 L',
    topUpQty: '15 L',
    topUpInterval: '4320 hrs',
    replacementInterval: '8640 hrs',
    brands: ['-'],
    remarks: '-'
  },
  {
    id: '450-PD-03B-COOLANT',
    tagNo: '450-PD-03B',
    description: 'Fire Water Pump Diesel Engine',
    part: 'Heat Exchanger (Engine Coolant)',
    package: 'PFA450',
    type: LubricantType.OIL,
    grade: 'ASTM D6210 (50%Glycol+50%Potable Water)',
    initialFill: '52.6 L',
    topUpQty: '15 L',
    topUpInterval: '4320 hrs',
    replacementInterval: '8640 hrs',
    brands: ['-'],
    remarks: '-'
  },
  {
    id: '450-P-01A',
    tagNo: '450-P-01A',
    description: 'Fire Water Jockey Pump',
    part: 'Bearing',
    package: 'PFA450',
    type: LubricantType.OIL,
    grade: 'ISO VG 46',
    initialFill: '1.1 L',
    topUpQty: '0.20 L',
    topUpInterval: '4320 hrs',
    replacementInterval: '8640 hrs',
    brands: ['ENERGOL HPL-D-46', 'TELLUS S46', 'DTE 25', 'EQUIVIS ZS 46', 'TISKA 46'],
    remarks: '-'
  },
  {
    id: '450-P-01B',
    tagNo: '450-P-01B',
    description: 'Fire Water Jockey Pump',
    part: 'Bearing',
    package: 'PFA450',
    type: LubricantType.OIL,
    grade: 'ISO VG 46',
    initialFill: '1.1 L',
    topUpQty: '0.20 L',
    topUpInterval: '4320 hrs',
    replacementInterval: '8640 hrs',
    brands: ['ENERGOL HPL-D-46', 'TELLUS S46', 'DTE 25', 'EQUIVIS ZS 46', 'TISKA 46'],
    remarks: '-'
  },
  {
    id: '450-PM-01A',
    tagNo: '450-PM-01A',
    description: 'Fire Water Jockey Pump Motor',
    part: 'Bearing',
    package: 'PFA450',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '70 g',
    topUpQty: '30 g',
    topUpInterval: '4320 hrs',
    replacementInterval: '8640 hrs',
    brands: ['ENER LS2', 'GADUS S2 V220 2', 'Mobilux EP2', 'MULTIS EP2', 'TESSALA EP2'],
    remarks: '-'
  },
  {
    id: '450-PM-01B',
    tagNo: '450-PM-01B',
    description: 'Fire Water Jockey Pump Motor',
    part: 'Bearing',
    package: 'PFA450',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '70 g',
    topUpQty: '30 g',
    topUpInterval: '4320 hrs',
    replacementInterval: '8640 hrs',
    brands: ['ENER LS2', 'GADUS S2 V220 2', 'Mobilux EP2', 'MULTIS EP2', 'TESSALA EP2'],
    remarks: '-'
  },
  {
    id: '471-PK-01',
    tagNo: '471-PK-01',
    description: 'Air Lubricator',
    part: 'Air Lubricator',
    package: 'PFA471',
    type: LubricantType.OIL,
    grade: 'ISO VG 32',
    initialFill: '0.05 L',
    topUpQty: '0.02 L',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: ['Castrol HySpin AW 32', 'Mobil DTE 24'],
    remarks: '1. The Air Lubricator, should be kept filled with lube and Top-Up Frequency will depend on how much lube is lost in the unlikely event that it occurs. 2. 1.07 litres of Mobil DTE 24 are supplied by Vendor'
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
print(f"✅ تم إضافة 15 معدة جديدة من Fire Water System (Package 450)")
print(f"✅ إجمالي المعدات الآن: {equipment_count}")
