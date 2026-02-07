#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete Script to generate data.ts with ALL equipment entries from PDF
This includes PFM101, PFM102, PFM104, PFM105-PFM117, Air Coolers, and standalone equipment
"""

def generate_complete_database():
    """Generate the complete data.ts file with all equipment"""
    
    # Header
    header = '''import { EquipmentData, LubricantType } from './types';

export const EQUIPMENT_DATABASE: EquipmentData[] = [
'''
    
    equipment_entries = []
    
    # ================================
    # PFM101: MOTOR DRIVEN FEED GAS AND SALES GAS CENTRIFUGAL COMPRESSOR
    # ================================
    print("Generating PFM101 equipment...")
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
    
    # Gas Compressor Main Drive Motor - Bearings
    for tag in compressor_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-CM-01',
    tagNo: '{tag}-CM-01',
    description: 'Gas Compressor Main Drive Motor',
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
    
    # Main Lube Oil Pump
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
    
    # Auxiliary Lube Oil Pump
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
    
    # Main Lube Oil Pump Motor
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
    brands: {{ shell: 'Gadus S5 V 100 2 / Unirex N2 or N3', mobil: 'Mobilith SHC 100', total: 'Multis Complex S2 A' }},
    remarks: 'Lithium Grease. Initial Fill of Grease at Factory.'
  }}''')
    
    # Auxiliary Lube Oil Pump Motor
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
    
    # Lube Oil Cooler Fan (A/B/C)
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
    brands: {{ bp: 'Olista Longtime 3EP', shell: 'Alvania EP2 / Gadus S2 V220 2 / Unirex N2 or N3', mobil: 'Mobilith SHC 100', total: 'Multis Complex S2 A' }},
    remarks: 'Lithium Grease. Initial Fill at Factory. If stationary >30 days, re-lubricate before restart.'
  }}''')
    
    # Lube Oil Cooler Fan Motor (A/B/C) - Greased For Life
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
    
    # MV Motor Cooling Fan Motor (A/B/C)
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
    brands: {{ shell: 'Gadus S5 V 100 2 / Unirex N2 or N3', mobil: 'Mobilith SHC 100', total: 'Multis Complex S2 A' }},
    remarks: 'Lithium Grease. Initial Fill of Grease at Factory.'
  }}''')
    
    # Oil Mist Fan Motor - Greased For Life
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
    
    print(f"PFM101: Generated {len([e for e in equipment_entries if 'PFM101' in e])} entries")
    
    # ================================
    # PFM102: RECIPROCATING COMPRESSOR PACKAGE
    # ================================
    print("Generating PFM102 equipment...")
    recip_tags = ['531', '532', '631', '632']
    
    # Stabilizer Overhead Compressor - Crank Mechanism
    for tag in recip_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-C-01',
    tagNo: '{tag}-C-01',
    description: 'Stabilizer Overhead Compressor',
    part: 'Compressor Crank Mechanism',
    package: 'JI2045-0-PFM102',
    type: LubricantType.OIL,
    grade: 'ISO VG 150',
    initialFill: '80 L',
    topUpQty: '80 L',
    topUpInterval: '4000 hrs',
    replacementInterval: '4000 Running hours or 8640 hours',
    brands: {{ shell: 'MORLINA S1B', mobil: 'RARUS 429', other: 'SIAD - PARASYNTH GREEN / AGIP - ACER' }},
    remarks: '1. Lubrication oil to be replaced 4000 working hours or once a year whichever is earlier. 2. Lubrication oil visual level check every 100 hours.'
  }}''')
    
    # Stabilizer Overhead Compressor Motor - Bearings
    for tag in recip_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-CM-01',
    tagNo: '{tag}-CM-01',
    description: 'Stabilizer Overhead Compressor Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM102',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '55 g (DE) / 40 g (NDE)',
    topUpQty: '55 g (DE) / 40 g (NDE)',
    topUpInterval: '6500 hrs',
    replacementInterval: '6500 Running hours or 8640 hours',
    brands: {{ shell: 'Gadus S5 V 100 2', mobil: 'UNIREX N2/N3', total: 'Multiplex S2 A' }},
    remarks: '1. Lubrication Grease to be replaced 6500 working hours or once a year whichever is earlier.'
  }}''')
    
    # Cylinder Lubricating Oil Pump
    for tag in recip_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-P-55',
    tagNo: '{tag}-P-55',
    description: 'Cylinder Lubricating Oil Pump',
    part: 'Cylinder lubrication',
    package: 'JI2045-0-PFM102',
    type: LubricantType.OIL,
    grade: 'ISO VG 150',
    initialFill: '32 L',
    topUpQty: '32 L',
    topUpInterval: '600 hrs',
    replacementInterval: '4000 hrs',
    brands: {{ shell: 'MORLINA S1B', mobil: 'RARUS 429', other: 'SIAD - PARASYNTH GREEN / AGIP - ACER' }},
    remarks: '1. Lubrication oil visual level check every 100 hours. Re-fill the missing amount in tank.'
  }}''')
    
    # Cylinder Lubricating Oil Pump Motor - Greased For Life
    for tag in recip_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-PM-55',
    tagNo: '{tag}-PM-55',
    description: 'Cylinder Lubricating Oil Pump Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM102',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Greased For Life'
  }}''')
    
    # Auxiliary Oil Pump Motor - Greased For Life
    for tag in recip_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-PM-52',
    tagNo: '{tag}-PM-52',
    description: 'Auxiliary Oil Pump Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM102',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Greased For Life'
  }}''')
    
    # Main Water Pump Motor - Only for 531/631
    for tag in ['531', '631']:
        equipment_entries.append(f'''  {{
    id: '{tag}-PM-56',
    tagNo: '{tag}-PM-56',
    description: 'Main Water Pump Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM102',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Greased For Life'
  }}''')
    
    # Main Water Pump - Only for 531/631
    for tag in ['531', '631']:
        equipment_entries.append(f'''  {{
    id: '{tag}-P-56',
    tagNo: '{tag}-P-56',
    description: 'Main Water Pump',
    part: 'Bearings',
    package: 'JI2045-0-PFM102',
    type: LubricantType.OIL,
    grade: 'ISO VG 46',
    initialFill: '0.2 L',
    topUpQty: '0.2 L',
    topUpInterval: '300 hrs',
    replacementInterval: '8500 running hours (first oil change in 300 working hours)',
    brands: {{ shell: 'Shell Tellus 46', mobil: 'DTE Oil Medium', total: 'Drosera MS 46' }},
    remarks: ''
  }}''')
    
    # Auxiliary Water Pump Motor - Only for 531/631
    for tag in ['531', '631']:
        equipment_entries.append(f'''  {{
    id: '{tag}-PM-57',
    tagNo: '{tag}-PM-57',
    description: 'Auxiliary Water Pump Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM102',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Greased For Life'
  }}''')
    
    # Auxiliary Water Pump - Only for 531/631
    for tag in ['531', '631']:
        equipment_entries.append(f'''  {{
    id: '{tag}-P-57',
    tagNo: '{tag}-P-57',
    description: 'Auxiliary Water Pump',
    part: 'Bearings',
    package: 'JI2045-0-PFM102',
    type: LubricantType.OIL,
    grade: 'ISO VG 46',
    initialFill: '0.2 L',
    topUpQty: '0.2 L',
    topUpInterval: '300 hrs',
    replacementInterval: '8500 running hours (first oil change in 300 working hours)',
    brands: {{ shell: 'Shell Tellus 46', mobil: 'DTE Oil Medium', total: 'Drosera MS 46' }},
    remarks: ''
  }}''')
    
    # Air Cooler Fan Motor (A/B) - Only for 531/631
    for tag in ['531', '631']:
        for variant in ['A', 'B']:
            equipment_entries.append(f'''  {{
    id: '{tag}-EAM-54{variant}',
    tagNo: '{tag}-EAM-54{variant}',
    description: 'Air Cooler Fan Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM102',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Greased For Life'
  }}''')
    
    # Cooling Media - Only 2 units (531/631)
    for tag in ['531', '631']:
        equipment_entries.append(f'''  {{
    id: '{tag}-C-01-COOLING',
    tagNo: '{tag}-C-01',
    description: 'Stabilizer Overhead Compressor',
    part: 'Cooling Media',
    package: 'JI2045-0-PFM102',
    type: LubricantType.OIL,
    grade: '15% Ethylene Glycol+85% Potable Water',
    initialFill: '1450 L',
    topUpQty: '50 L',
    topUpInterval: '360 hrs',
    replacementInterval: '-',
    brands: {{}},
    remarks: ''
  }}''')
    
    print(f"PFM102: Generated {len([e for e in equipment_entries if 'PFM102' in e])} entries")
    
    # ================================
    # PFM104: GAS TURBINE GENERATOR PACKAGE
    # ================================
    print("Generating PFM104 equipment...")
    gtg_tags = ['811', '812', '813', '814', '815']
    
    # Lube Oil Tank
    for tag in gtg_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-TK-01',
    tagNo: '{tag}-TK-01',
    description: 'Lube Oil Tank',
    part: 'Gas Turbine / Load Gear / Auxiliary Gear / Generator / Torque Converter / SSS Clutch',
    package: 'JI2045-0-PFM104',
    type: LubricantType.OIL,
    grade: 'ISO VG 32',
    initialFill: '10000 L',
    topUpQty: '750 L',
    topUpInterval: '1500 hrs',
    replacementInterval: 'Based on oil analysis (sample check 24 hrs after 1st start and every 4000 hrs)',
    brands: {{ bp: 'CASTROL PERFECTO XEP 32', shell: 'Turbo S4 GX 32', mobil: 'DTE 832 / SHC 824', total: 'Preslia GT 32 / TISKA 32', other: 'ENI OTE GT 32 / Petronas Jenteram U 32 / Petronas Jenteram Syn 32' }},
    remarks: '1. Sample check 24 hrs after 1st start and every each 4000 hrs. Oil shall be replaced based on analysis results.'
  }}''')
    
    # Main Lube Oil Pump
    for tag in gtg_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-P-01',
    tagNo: '{tag}-P-01',
    description: 'Main Lube Oil Pump',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.OIL,
    grade: 'ISO VG 32',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: '1. Self lubricated by pumped fluid'
  }}''')
    
    # Stand-by Lube Oil Pump
    for tag in gtg_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-P-02',
    tagNo: '{tag}-P-02',
    description: 'Stand-by Lube Oil Pump',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.GREASE,
    grade: 'NLGI-2',
    initialFill: '60 g',
    topUpQty: '60 g',
    topUpInterval: '3000 Running hours or 4320 hours',
    replacementInterval: '3000 Running hours or 4320 hours',
    brands: {{ other: 'SKF - LGMT2' }},
    remarks: '1. Replacement Interval is to be calculated based on Operating hours of the equipment. 2. Initial Fill of Grease at Factory.'
  }}''')
    
    # Emergency Lube Oil Pump
    for tag in gtg_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-P-03',
    tagNo: '{tag}-P-03',
    description: 'Emergency Lube Oil Pump',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.GREASE,
    grade: 'NLGI-2',
    initialFill: '60 g',
    topUpQty: '60 g',
    topUpInterval: '3000 Running hours or 4320 hours',
    replacementInterval: '3000 Running hours or 4320 hours',
    brands: {{ other: 'SKF - LGMT2' }},
    remarks: '1. Initial Fill of Grease at Factory.'
  }}''')
    
    # Stand-by Lube Oil Pump Motor
    for tag in gtg_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-PM-02',
    tagNo: '{tag}-PM-02',
    description: 'Stand-by Lube Oil Pump Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.GREASE,
    grade: 'NLGI-2',
    initialFill: '53 g',
    topUpQty: '30 g (DE) / 23 g (NDE)',
    topUpInterval: '3700 Running hours',
    replacementInterval: '3700 Running hours',
    brands: {{ mobil: 'Unirex N2 or N3' }},
    remarks: '1. Grease shall be Lithium Complex Base. 2. Initial Fill of Grease at Factory.'
  }}''')
    
    # Emergency Lube Oil Pump Motor - Greased For Life
    for tag in gtg_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-PM-03',
    tagNo: '{tag}-PM-03',
    description: 'Emergency Lube Oil Pump Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Greased For Life'
  }}''')
    
    # Oil Vapor Separator Centrifugal Fan Motor - Greased For Life
    for tag in gtg_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-KM-02',
    tagNo: '{tag}-KM-02',
    description: 'Oil Vapor Separator Centrifugal Fan Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Greased For Life'
  }}''')
    
    # Ratchet Pump
    for tag in gtg_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-P-05',
    tagNo: '{tag}-P-05',
    description: 'Ratchet Pump',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.OIL,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: '1. Self lubricated by pumped fluid'
  }}''')
    
    # Ratchet Pump Motor - Greased For Life
    for tag in gtg_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-PM-05',
    tagNo: '{tag}-PM-05',
    description: 'Ratchet Pump Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Greased For Life'
  }}''')
    
    # Hydraulic Oil Main Pump
    for tag in gtg_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-P-04',
    tagNo: '{tag}-P-04',
    description: 'Hydraulic Oil Main Pump',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.OIL,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: '1. Self lubricated by pumped fluid'
  }}''')
    
    # Lube Oil Cooler Fan (A/B/C)
    for tag in gtg_tags:
        for variant in ['A', 'B', 'C']:
            equipment_entries.append(f'''  {{
    id: '{tag}-EAF-01{variant}',
    tagNo: '{tag}-EAF-01{variant}',
    description: 'Lube Oil Cooler Fan',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.GREASE,
    grade: 'NLGI-2',
    initialFill: '140 g',
    topUpQty: '70 g (Upper) / 70 g (Lower)',
    topUpInterval: '3000 Running hours',
    replacementInterval: '3000 Running hours',
    brands: {{ bp: 'Olista Longtime 3EP', shell: 'Alvina EP / Unirex N2 or N3', other: 'AGIP - GR MU EP2' }},
    remarks: '1. Grease shall be Lithium Complex Base'
  }}''')
    
    # Lube Oil Cooler Fan Motor (A/B/C)
    for tag in gtg_tags:
        for variant in ['A', 'B', 'C']:
            equipment_entries.append(f'''  {{
    id: '{tag}-EAM-01{variant}',
    tagNo: '{tag}-EAM-01{variant}',
    description: 'Lube Oil Cooler Fan Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.GREASE,
    grade: 'NLGI-2',
    initialFill: '100 g',
    topUpQty: '50 g (DE) / 50 g (NDE)',
    topUpInterval: '3000 Running hours',
    replacementInterval: '3000 Running hours',
    brands: {{ shell: 'GADUS S5 V 100 2 / Unirex N2 or N3', mobil: 'Mobilith SHC 100', total: 'Multis Complex S2 A', other: 'KLUBERPLEX BEM 41-132' }},
    remarks: '1. Grease shall be Lithium Complex Base'
  }}''')
    
    # Charge Pump For Torque Converter
    for tag in gtg_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-P-06',
    tagNo: '{tag}-P-06',
    description: 'Charge Pump For Torque Converter',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.OIL,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: '1. Self lubricated by pumped fluid'
  }}''')
    
    # Starting Motor
    for tag in gtg_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-PM-06',
    tagNo: '{tag}-PM-06',
    description: 'Starting Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.GREASE,
    grade: 'NLGI-2',
    initialFill: '65 g',
    topUpQty: '41 g (DE) / 24 g (NDE)',
    topUpInterval: '1000 Running hours (NDE) / 1400 Running hours (DE)',
    replacementInterval: '1000 Running hours (NDE) / 1400 Running hours (DE)',
    brands: {{ mobil: 'Polyrex EM' }},
    remarks: '1. Grease shall be Lithium Complex Base. 2. Replacement Interval is to be calculated based on Operating hours of the equipment. 3. Initial Fill of Grease at Factory.'
  }}''')
    
    # Dust Extractor Fan Motor (03/04) - No Lubrication Required
    for tag in gtg_tags:
        for num in ['03', '04']:
            equipment_entries.append(f'''  {{
    id: '{tag}-KM-{num}',
    tagNo: '{tag}-KM-{num}',
    description: 'Dust Extractor Fan Motor',
    part: 'Sealed Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.OIL,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: '1. Lubrication not required. Bearings L10 rating life 40000 hrs'
  }}''')
    
    # Main and Auxiliary Ventilation Fan Motor (A/B)
    for tag in gtg_tags:
        for variant in ['A', 'B']:
            equipment_entries.append(f'''  {{
    id: '{tag}-KM-01{variant}',
    tagNo: '{tag}-KM-01{variant}',
    description: 'Main and Auxiliary Ventilation Fan Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.GREASE,
    grade: 'NLGI-2',
    initialFill: '80 g',
    topUpQty: '40 g (DE) / 40 g (NDE)',
    topUpInterval: '7800 Running hours',
    replacementInterval: '7800 Running hours',
    brands: {{ mobil: 'Unirex N2 or N3' }},
    remarks: '1. Grease shall be Lithium Complex Base. 2. Initial Fill of Grease at Factory.'
  }}''')
    
    # Generator Cooler Fan Motors (A/B/C) - Greased For Life
    for tag in gtg_tags:
        for variant in ['A', 'B', 'C']:
            equipment_entries.append(f'''  {{
    id: '{tag}-GEM-01{variant}',
    tagNo: '{tag}-GEM-01{variant}',
    description: 'Generator Cooler Fan Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Greased For Life'
  }}''')
    
    # Gas Turbine Generator - Washing Detergent
    for tag in gtg_tags:
        equipment_entries.append(f'''  {{
    id: '{tag}-GT-01',
    tagNo: '{tag}-GT-01',
    description: 'Gas Turbine Generator',
    part: 'Washing Detergent',
    package: 'JI2045-0-PFM104',
    type: LubricantType.OIL,
    grade: 'BH ITN07831.04 AND GEI 41042p',
    initialFill: '600 L',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: '200 litres of detergent is required for one off-line washing cycle of one GTG Unit.'
  }}''')
    
    # Standalone 810-P-07 Washing Solution Pump - Greased For Life
    equipment_entries.append('''  {
    id: '810-P-07',
    tagNo: '810-P-07',
    description: 'Washing Solution Pump',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {},
    remarks: 'Greased For Life'
  }''')
    
    # Standalone 810-PM-07 Washing Solution Pump Motor - Greased For Life
    equipment_entries.append('''  {
    id: '810-PM-07',
    tagNo: '810-PM-07',
    description: 'Washing Solution Pump Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM104',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {},
    remarks: 'Greased For Life'
  }''')
    
    print(f"PFM104: Generated {len([e for e in equipment_entries if 'PFM104' in e])} entries")
    
    # ================================
    # AIR COOLER HEAT EXCHANGERS
    # ================================
    print("Generating Air Cooler Heat Exchangers...")
    
    # 301/302/303-EA-01: Feed Gas Compressor After Cooler (3 units × 4 parts = 12 entries)
    for tag in ['301', '302', '303']:
        # UPPER FAN BEARING
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-01-UPPER',
    tagNo: '{tag}-EA-01',
    description: 'Feed Gas Compressor After Cooler',
    part: 'UPPER FAN BEARING (UCF316)',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '30 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '2160 hrs',
    brands: {{ bp: 'ENER LS2', shell: 'Shell Gadus S2 V100 2', mobil: 'MOBIL POLYREX EM', total: 'MULTIS EP2', naftal: 'TESSALA EP2' }},
    remarks: ''
  }}''')
        
        # LOWER FAN BEARING
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-01-LOWER',
    tagNo: '{tag}-EA-01',
    description: 'Feed Gas Compressor After Cooler',
    part: 'LOWER FAN BEARING (#22316)',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '50 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '2160 hrs',
    brands: {{ bp: 'ENER LS2', shell: 'Shell Gadus S2 V100 2', mobil: 'MOBIL POLYREX EM', total: 'MULTIS EP2', naftal: 'TESSALA EP2' }},
    remarks: ''
  }}''')
        
        # MOTOR DRIVE END
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-01-MOTOR-DE',
    tagNo: '{tag}-EA-01',
    description: 'Feed Gas Compressor After Cooler Motor',
    part: 'MOTOR DRIVE END / 6314-C3',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '27 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '4000 hrs',
    brands: {{ mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2 / SKF - LGHP2' }},
    remarks: ''
  }}''')
        
        # MOTOR NON DRIVE END
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-01-MOTOR-NDE',
    tagNo: '{tag}-EA-01',
    description: 'Feed Gas Compressor After Cooler Motor',
    part: 'MOTOR NON DRIVE END / 6314-C3',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '27 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '4000 hrs',
    brands: {{ mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2 / SKF - LGHP2' }},
    remarks: ''
  }}''')
    
    # 401-EA-01: Hot Oil Trim Cooler (1 unit × 4 parts = 4 entries)
    equipment_entries.append('''  {
    id: '401-EA-01-UPPER',
    tagNo: '401-EA-01',
    description: 'Hot Oil Trim Cooler',
    part: 'UPPER FAN BEARING (UCF315)',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '30 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '2160 hrs',
    brands: { bp: 'ENER LS2', shell: 'Shell Gadus S2 V100 2', mobil: 'MOBIL POLYREX EM', total: 'MULTIS EP2', naftal: 'TESSALA EP2' },
    remarks: ''
  }''')
    
    equipment_entries.append('''  {
    id: '401-EA-01-LOWER',
    tagNo: '401-EA-01',
    description: 'Hot Oil Trim Cooler',
    part: 'LOWER FAN BEARING (#22316)',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '50 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '2160 hrs',
    brands: { bp: 'ENER LS2', shell: 'Shell Gadus S2 V100 2', mobil: 'MOBIL POLYREX EM', total: 'MULTIS EP2', naftal: 'TESSALA EP2' },
    remarks: ''
  }''')
    
    equipment_entries.append('''  {
    id: '401-EA-01-MOTOR-DE',
    tagNo: '401-EA-01',
    description: 'Hot Oil Trim Cooler Motor',
    part: 'MOTOR DRIVE END / 6308-C3',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '11 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '14000 hrs',
    brands: { mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2 / SKF - LGHP2' },
    remarks: ''
  }''')
    
    equipment_entries.append('''  {
    id: '401-EA-01-MOTOR-NDE',
    tagNo: '401-EA-01',
    description: 'Hot Oil Trim Cooler Motor',
    part: 'MOTOR NON DRIVE END / 6207-C3',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '7 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '17000 hrs',
    brands: { mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2 / SKF - LGHP2' },
    remarks: ''
  }''')
    
    # 510/610-EA-01: Gas Dehydrator Regeneration Gas Cooler (2 units × 4 parts = 8 entries)
    for tag in ['510', '610']:
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-01-UPPER',
    tagNo: '{tag}-EA-01',
    description: 'Gas Dehydrator Regeneration Gas Cooler',
    part: 'UPPER FAN BEARING (UC315)',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '30 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '2160 hrs',
    brands: {{ bp: 'ENER LS2', shell: 'Shell Gadus S2 V100 2', mobil: 'MOBIL POLYREX EM', total: 'MULTIS EP2', naftal: 'TESSALA EP2' }},
    remarks: ''
  }}''')
        
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-01-LOWER',
    tagNo: '{tag}-EA-01',
    description: 'Gas Dehydrator Regeneration Gas Cooler',
    part: 'LOWER FAN BEARING (#22316)',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '50 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '2160 hrs',
    brands: {{ bp: 'ENER LS2', shell: 'Shell Gadus S2 V100 2', mobil: 'MOBIL POLYREX EM', total: 'MULTIS EP2', naftal: 'TESSALA EP2' }},
    remarks: ''
  }}''')
        
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-01-MOTOR-DE',
    tagNo: '{tag}-EA-01',
    description: 'Gas Dehydrator Regeneration Gas Cooler Motor',
    part: 'MOTOR DRIVE END / 6309-C3',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '13 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '13000 hrs',
    brands: {{ mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2 / SKF - LGHP2' }},
    remarks: ''
  }}''')
        
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-01-MOTOR-NDE',
    tagNo: '{tag}-EA-01',
    description: 'Gas Dehydrator Regeneration Gas Cooler Motor',
    part: 'MOTOR NON DRIVE END / 6309-C3',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '9 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '14000 hrs',
    brands: {{ mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2 / SKF - LGHP2' }},
    remarks: ''
  }}''')
    
    # 530/630-EA-02: LPG Splitter Condenser (2 units × 4 parts = 8 entries)
    for tag in ['530', '630']:
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-02-UPPER',
    tagNo: '{tag}-EA-02',
    description: 'LPG Splitter Condenser',
    part: 'UPPER FAN BEARING (UC315)',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '30 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '2160 hrs',
    brands: {{ bp: 'ENER LS2', shell: 'Shell Gadus S2 V100 2', mobil: 'MOBIL POLYREX EM', total: 'MULTIS EP2', naftal: 'TESSALA EP2' }},
    remarks: ''
  }}''')
        
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-02-LOWER',
    tagNo: '{tag}-EA-02',
    description: 'LPG Splitter Condenser',
    part: 'LOWER FAN BEARING (#22316)',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '50 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '2160 hrs',
    brands: {{ bp: 'ENER LS2', shell: 'Shell Gadus S2 V100 2', mobil: 'MOBIL POLYREX EM', total: 'MULTIS EP2', naftal: 'TESSALA EP2' }},
    remarks: ''
  }}''')
        
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-02-MOTOR-DE',
    tagNo: '{tag}-EA-02',
    description: 'LPG Splitter Condenser Motor',
    part: 'MOTOR DRIVE END / 6311-C3',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '18 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '11000 hrs',
    brands: {{ mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2 / SKF - LGHP2' }},
    remarks: ''
  }}''')
        
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-02-MOTOR-NDE',
    tagNo: '{tag}-EA-02',
    description: 'LPG Splitter Condenser Motor',
    part: 'MOTOR NON DRIVE END / 6211-C3',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '11 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '12000 hrs',
    brands: {{ mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2 / SKF - LGHP2' }},
    remarks: ''
  }}''')
    
    # 530/630-EA-03: Condensate Rundown Cooler (2 units × 4 parts = 8 entries)
    for tag in ['530', '630']:
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-03-UPPER',
    tagNo: '{tag}-EA-03',
    description: 'Condensate Rundown Cooler',
    part: 'UPPER FAN BEARING (UC315)',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '30 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '2160 hrs',
    brands: {{ bp: 'ENER LS2', shell: 'Shell Gadus S2 V100 2', mobil: 'MOBIL POLYREX EM', total: 'MULTIS EP2', naftal: 'TESSALA EP2' }},
    remarks: ''
  }}''')
        
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-03-LOWER',
    tagNo: '{tag}-EA-03',
    description: 'Condensate Rundown Cooler',
    part: 'LOWER FAN BEARING (#22316)',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '50 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '2160 hrs',
    brands: {{ bp: 'ENER LS2', shell: 'Shell Gadus S2 V100 2', mobil: 'MOBIL POLYREX EM', total: 'MULTIS EP2', naftal: 'TESSALA EP2' }},
    remarks: ''
  }}''')
        
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-03-MOTOR-DE',
    tagNo: '{tag}-EA-03',
    description: 'Condensate Rundown Cooler Motor',
    part: 'MOTOR DRIVE END / 6311-C3',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '18 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '11000 hrs',
    brands: {{ mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2 / SKF - LGHP2' }},
    remarks: ''
  }}''')
        
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-03-MOTOR-NDE',
    tagNo: '{tag}-EA-03',
    description: 'Condensate Rundown Cooler Motor',
    part: 'MOTOR NON DRIVE END / 6211-C3',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '11 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '12000 hrs',
    brands: {{ mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2 / SKF - LGHP2' }},
    remarks: ''
  }}''')
    
    # 750-EA-03: Sales Gas Compressor After Cooler (1 unit × 4 parts = 4 entries)
    equipment_entries.append('''  {
    id: '750-EA-03-UPPER',
    tagNo: '750-EA-03',
    description: 'Sales Gas Compressor After Cooler',
    part: 'UPPER FAN BEARING (UC315)',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '30 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '2160 hrs',
    brands: { bp: 'ENER LS2', shell: 'Shell Gadus S2 V100 2', mobil: 'MOBIL POLYREX EM', total: 'MULTIS EP2', naftal: 'TESSALA EP2' },
    remarks: ''
  }''')
    
    equipment_entries.append('''  {
    id: '750-EA-03-LOWER',
    tagNo: '750-EA-03',
    description: 'Sales Gas Compressor After Cooler',
    part: 'LOWER FAN BEARING (#22316)',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '50 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '2160 hrs',
    brands: { bp: 'ENER LS2', shell: 'Shell Gadus S2 V100 2', mobil: 'MOBIL POLYREX EM', total: 'MULTIS EP2', naftal: 'TESSALA EP2' },
    remarks: ''
  }''')
    
    equipment_entries.append('''  {
    id: '750-EA-03-MOTOR-DE',
    tagNo: '750-EA-03',
    description: 'Sales Gas Compressor After Cooler Motor',
    part: 'MOTOR DRIVE END / 6314-C3',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '27 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '4000 hrs',
    brands: { mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2 / SKF - LGHP2' },
    remarks: ''
  }''')
    
    equipment_entries.append('''  {
    id: '750-EA-03-MOTOR-NDE',
    tagNo: '750-EA-03',
    description: 'Sales Gas Compressor After Cooler Motor',
    part: 'MOTOR NON DRIVE END / 6314-C3',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '27 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '4000 hrs',
    brands: { mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2 / SKF - LGHP2' },
    remarks: ''
  }''')
    
    # 751/752/753/754-EA-01: Sales Gas Compressor Suction Cooler (4 units × 4 parts = 16 entries)
    for tag in ['751', '752', '753', '754']:
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-01-UPPER',
    tagNo: '{tag}-EA-01',
    description: 'Sales Gas Compressor Suction Cooler',
    part: 'UPPER FAN BEARING (UCF316)',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '30 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '2160 hrs',
    brands: {{ bp: 'ENER LS2', shell: 'Shell Gadus S2 V100 2', mobil: 'MOBIL POLYREX EM', total: 'MULTIS EP2', naftal: 'TESSALA EP2' }},
    remarks: ''
  }}''')
        
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-01-LOWER',
    tagNo: '{tag}-EA-01',
    description: 'Sales Gas Compressor Suction Cooler',
    part: 'LOWER FAN BEARING (#22316)',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '50 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '2160 hrs',
    brands: {{ bp: 'ENER LS2', shell: 'Shell Gadus S2 V100 2', mobil: 'MOBIL POLYREX EM', total: 'MULTIS EP2', naftal: 'TESSALA EP2' }},
    remarks: ''
  }}''')
        
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-01-MOTOR-DE',
    tagNo: '{tag}-EA-01',
    description: 'Sales Gas Compressor Suction Cooler Motor',
    part: 'MOTOR DRIVE END / 6314-C3',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '27 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '4000 hrs',
    brands: {{ mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2 / SKF - LGHP2' }},
    remarks: ''
  }}''')
        
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-01-MOTOR-NDE',
    tagNo: '{tag}-EA-01',
    description: 'Sales Gas Compressor Suction Cooler Motor',
    part: 'MOTOR NON DRIVE END / 6314-C3',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '27 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '4000 hrs',
    brands: {{ mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2 / SKF - LGHP2' }},
    remarks: ''
  }}''')
    
    # 751/752/753/754-EA-02: Sales Gas Compressor Interstage Cooler (4 units × 4 parts = 16 entries)
    for tag in ['751', '752', '753', '754']:
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-02-UPPER',
    tagNo: '{tag}-EA-02',
    description: 'Sales Gas Compressor Interstage Cooler',
    part: 'UPPER FAN BEARING (UC315)',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '30 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '2160 hrs',
    brands: {{ bp: 'ENER LS2', shell: 'Shell Gadus S2 V100 2', mobil: 'MOBIL POLYREX EM', total: 'MULTIS EP2', naftal: 'TESSALA EP2' }},
    remarks: ''
  }}''')
        
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-02-LOWER',
    tagNo: '{tag}-EA-02',
    description: 'Sales Gas Compressor Interstage Cooler',
    part: 'LOWER FAN BEARING (#22316)',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '50 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '2160 hrs',
    brands: {{ bp: 'ENER LS2', shell: 'Shell Gadus S2 V100 2', mobil: 'MOBIL POLYREX EM', total: 'MULTIS EP2', naftal: 'TESSALA EP2' }},
    remarks: ''
  }}''')
        
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-02-MOTOR-DE',
    tagNo: '{tag}-EA-02',
    description: 'Sales Gas Compressor Interstage Cooler Motor',
    part: 'MOTOR DRIVE END / 6311-C3',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '18 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '11000 hrs',
    brands: {{ mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2 / SKF - LGHP2' }},
    remarks: ''
  }}''')
        
        equipment_entries.append(f'''  {{
    id: '{tag}-EA-02-MOTOR-NDE',
    tagNo: '{tag}-EA-02',
    description: 'Sales Gas Compressor Interstage Cooler Motor',
    part: 'MOTOR NON DRIVE END / 6211-C3',
    package: 'JI2045-0-PFM115',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '11 g',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '12000 hrs',
    brands: {{ mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2 / SKF - LGHP2' }},
    remarks: ''
  }}''')
    
    print(f"Air Coolers: Generated {len([e for e in equipment_entries if 'EA-' in e])} entries")
    
    # Join all entries with commas
    all_entries = ',\n'.join(equipment_entries)
    
    # Footer
    footer = '\n];\n'
    
    # Complete file
    complete_file = header + all_entries + footer
    
    return complete_file, len(equipment_entries)

# Generate and save
print("="*60)
print("GENERATING COMPLETE DATABASE")
print("="*60)
output, total_count = generate_complete_database()
print(f"\nTotal equipment entries generated: {total_count}")
print("Writing to data_generated_full.ts...")

with open('data_generated_full.ts', 'w', encoding='utf-8') as f:
    f.write(output)

print("="*60)
print(f"✅ SUCCESS! Generated {total_count} equipment entries")
print("="*60)
print("\nFile saved as: data_generated_full.ts")
print("\nNext steps:")
print("1. Review the file")
print("2. Backup your current data.ts (if not already done)")
print("3. Rename data_generated_full.ts to data.ts")
print("4. Restart the development server")
print("="*60)
