#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to generate data.ts with all individual equipment entries from PDF data
"""

def expand_tag_numbers(tag_str):
    """Expand tag numbers like '301/302/303' or '301-C-01' to individual tags"""
    if '/' not in tag_str:
        return [tag_str]
    
    # Split by '/'
    parts = tag_str.split('/')
    
    # Find the common prefix and suffix
    # Example: "301/302/303/751/752/753/754-C-01"
    if '-' in tag_str:
        # Has equipment type suffix
        base_parts = tag_str.split('-')
        prefix_group = base_parts[0]  # "301/302/303/751/752/753/754"
        suffix = '-'.join(base_parts[1:])  # "C-01"
        
        numbers = prefix_group.split('/')
        return [f"{num}-{suffix}" for num in numbers]
    else:
        # No suffix, just numbers
        return parts

def generate_typescript_file():
    """Generate the complete data.ts file"""
    
    # Header
    header = '''import { EquipantType, LubricantType } from './types';

export const EQUIPMENT_DATABASE: EquipmentData[] = [
'''
    
    # Equipment data will be added here
    equipment_entries = []
    
    # PFM101: MOTOR DRIVEN FEED GAS AND SALES GAS CENTRIFUGAL COMPRESSOR
    # 301/302/303/751/752/753/754 equipment
    compressor_tags = ['301', '302', '303', '751', '752', '753', '754']
    
    # Gas Compressor - Bearings
    for tag in compressor_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-C-01',
    tagNo: '{tag}-C-01',
    description: 'Gas Compressor',
    part: 'Bearings',
    package: 'JI2045-0-PFM101',
    type: LubricantType.OIL,
    grade: 'ISO VG 46',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Quantity included in respective skid mounted Lube Oil Tank ({tag}-TK-51)'
  }}''')
    
    # Gs Compressor Main Drive Motor - Bearings
    for tag in compressor_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-CM-01',
    tagNo: '{tag}-CM-01',
    description: 'Gs Compressor Main Drive Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM101',
    type: LubricantType.OIL,
    grade: 'ISO VG 46',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Quantity included in respective skid mounted Lube Oil Tank ({tag}-TK-51)'
  }}''')
    
    # Gear Box - Bearings
    for tag in compressor_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-CG-01',
    tagNo: '{tag}-CG-01',
    description: 'Gear Box',
    part: 'Bearings',
    package: 'JI2045-0-PFM101',
    type: LubricantType.OIL,
    grade: 'ISO VG 46',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Quantity included in respective skid mounted Lube Oil Tank ({tag}-TK-51)'
  }}''')
    
    # Main Lube Oil Pump - Bearings
    for tag in compressor_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-P-51A',
    tagNo: '{tag}-P-51A',
    description: 'Main Lube Oil Pump',
    part: 'Bearings',
    package: 'JI2045-0-PFM101',
    type: LubricantType.OIL,
    grade: 'ISO VG 46',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Quantity included in respective skid mounted Lube Oil Tank ({tag}-TK-51)'
  }}''')
    
    # Auxiliary Lube Oil Pump - Bearings
    for tag in compressor_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-P-51B',
    tagNo: '{tag}-P-51B',
    description: 'Auxiliary Lube Oil Pump',
    part: 'Bearings',
    package: 'JI2045-0-PFM101',
    type: LubricantType.OIL,
    grade: 'ISO VG 46',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Quantity included in respective skid mounted Lube Oil Tank ({tag}-TK-51)'
  }}''')
    
    # Lube Oil Tank
    for tag in compressor_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-TK-51',
    tagNo: '{tag}-TK-51',
    description: 'Lube Oil Tank',
    part: 'Lube Oil Tank',
    package: 'JI2045-0-PFM101',
    type: LubricantType.OIL,
    grade: 'ISO VG 46',
    initialFill: '7103 L',
    topUpQty: '59 L',
    topUpInterval: '720 hrs',
    replacementInterval: 'Based on oil analysis',
    brands: {{ bp: 'CASTROL PERFECTO XEP 46', shell: 'TELLUS OIL 46', total: 'PRESLIA 46', naftal: 'TORBA 46' }},
    remarks: '1. Oil shall be Turbine Quality Mineral Oil. 2. During start up, check monthly until 6 months. After 6 months, oil analysis every 6 months. 3. Yearly consumption 710 litres.'
  }}''')
    
    # Main Lube Oil Pump Motor - Bearings
    for tag in compressor_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-PM-51A',
    tagNo: '{tag}-PM-51A',
    description: 'Main Lube Oil Pump Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM101',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 3',
    initialFill: '35 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '1475 hrs',
    brands: {{ shell: 'Gadus S5 V 100 2 / Unirex N2 or N3', mobil: 'Mobilith SHC 100', total: 'Multis Complex S2 A', other: 'Rhenus LKZ 2 / Klüber Kl³berplex BEM 41-132 / FAG Arcanol TEMP110 / Lubcon Turmogrease L 802 EP PLUS' }},
    remarks: 'Lithium Grease. Initial Fill of Grease at Factory.'
  }}''')
    
    # Auxiliary Lube Oil Pump Motor - Bearings
    for tag in compressor_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-PM-51B',
    tagNo: '{tag}-PM-51B',
    description: 'Auxiliary Lube Oil Pump Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM101',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 3',
    initialFill: '35 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '1475 hrs',
    brands: {{ shell: 'Gadus S5 V 100 2 / Unirex N2 or N3', mobil: 'Mobilith SHC 100', total: 'Multis Complex S2 A' }},
    remarks: 'Lithium Grease. Initial Fill of Grease at Factory.'
  }}''')
    
    # Lube Oil Cooler Fan - Bearings (A/B/C variants)
    for tag in compressor_tags:
        for variant in ['A', 'B', 'C']:
            equipment_entries.append(f'''  {{
    id: '{tag}-EAF-51{variant}',
    tagNo: '{tag}-EAF-51{variant}',
    description: 'Lube Oil Cooler Fan',
    part: 'Bearings',
    package: 'JI2045-0-PFM101',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 3',
    initialFill: '140 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '3000 hrs',
    brands: {{ bp: 'Olista Longtime 3EP', shell: 'Alvania EP2 / Gadus S2 V220 2 / Unirex N2 or N3', mobil: 'Mobilith SHC 100', total: 'Multis Complex S2 A', other: 'AGIP GR MU EP2 / IP ATHESIA EP2' }},
    remarks: 'Lithium Grease. Initial Fill at Factory. If stationary >30 days, re-lubricate before restart.'
  }}''')
    
    # Lube Oil Cooler Fan Motor - Bearings (A/B/C variants) - Greased For Life
    for tag in compressor_tags:
        for variant in ['A', 'B', 'C']:
            equipment_entries.append(f'''  {{
    id: '{tag}-EAM-51{variant}',
    tagNo: '{tag}-EAM-51{variant}',
    description: 'Lube Oil Cooler Fan Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM101',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Greased For Life'
  }}''')
    
    # MV Motor Cooling Fan Motor - Bearings (A/B/C variants)
    for tag in compressor_tags:
        for variant in ['A', 'B', 'C']:
            equipment_entries.append(f'''  {{
    id: '{tag}-EAM-52{variant}',
    tagNo: '{tag}-EAM-52{variant}',
    description: 'MV Motor Cooling Fan Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM101',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 3',
    initialFill: '30 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '7550 hrs',
    brands: {{ shell: 'Gadus S5 V 100 2 / Unirex N2 or N3', mobil: 'Mobilith SHC 100', total: 'Multis Complex S2 A', other: 'Rhenus LKZ 2 / Klüber Kl³berplex BEM 41-132 / FAG Arcanol TEMP110 / Lubcon Turmogrease L 802 EP PLUS' }},
    remarks: 'Lithium Grease. Initial Fill of Grease at Factory.'
  }}''')
    
    # Oil Mist Fan Motor - Bearings - Greased For Life
    for tag in compressor_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-VFM-51',
    tagNo: '{tag}-VFM-51',
    description: 'Oil Mist Fan Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM101',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Greased For Life'
  }}''')
    
    # Join all entries
    all_entries = ',\n'.join(equipment_entries)
    
    # Footer
    footer = '\n];\n'
    
    # Write complete file
    complete_file = header + all_entries + footer
    
    return complete_file

# Generate and save
output = generate_typescript_file()
print(f"Generated {output.count('id:')} equipment entries")
print("Writing to data_generated.ts...")

with open('data_generated.ts', 'w', encoding='utf-8') as f:
    f.write(output)

print("Done! File saved as data_generated.ts")
print("Review the file, then rename it to data.ts to replace the current one")
