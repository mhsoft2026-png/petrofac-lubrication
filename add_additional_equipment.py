#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add MORE equipment from PDF - Cranes, Injection Pumps, etc.
"""

def read_current_data():
    """Read current data.ts and extract existing IDs"""
    try:
        with open('data.ts', 'r', encoding='utf-8') as f:
            content = f.read()
            import re
            ids = re.findall(r"id: '([^']+)'", content)
            return set(ids), content
    except:
        return set(), ""

def generate_more_equipment():
    """Generate additional missing equipment"""
    
    existing_ids, current_content = read_current_data()
    
    new_entries = []
    
    print("="*80)
    print("إضافة معدات إضافية جديدة")
    print("="*80)
    
    # ========================================
    # CRANE 300-Z-01 (Feed Gas Compressor Shelter)
    # ========================================
    print("\n[1] إضافة رافعة 300-Z-01...")
    
    crane_300_parts = [
        ('300-Z-01-HOIST', 'Hoist gearbox', 'OIL', 'ISO VG 460', '16 L', '1.52 L', '8640 hrs', '43200 hrs'),
        ('300-Z-01-WIRE', 'Wire rope & rope guide', 'GREASE', 'ISO 2137', '2500 g', '250 g', '4320 hrs', '8640 hrs'),
        ('300-Z-01-CT-GB', 'Cross Travel gearbox', 'GREASE', 'ISO 2137', '200 g', '200 g', '8640 hrs', '43200 hrs'),
        ('300-Z-01-LT-GB1', 'Long Travel gearbox 1', 'OIL', 'ISO VG 460', '1 L', '0.25 L', '8640 hrs', '43200 hrs'),
        ('300-Z-01-LT-GB2', 'Long Travel gearbox 2', 'OIL', 'ISO VG 460', '1 L', '0.25 L', '8640 hrs', '43200 hrs'),
        ('300-Z-01-SPLINE', 'Spline shaft cross travel', 'GREASE', 'ISO 2137', '200 g', '-', '-', '43200 hrs'),
        ('300-Z-01-SPRINGS', 'Springs on overload cut off', 'GREASE', 'ISO 2137', '50 g', '50 g', '8640 hrs', '8640 hrs'),
        ('300-Z-01-PANEL', 'Ex control panel enclosure', 'GREASE', 'ISO 2137 (Copper)', '100 g', '-', '-', '8640 hrs'),
    ]
    
    count = 0
    for part_id, part_desc, lub_type, grade, init_fill, topup, topup_int, repl_int in crane_300_parts:
        if part_id not in existing_ids:
            brands_str = '{ bp: "Energol GR XP460", shell: "Omala Oil 460", mobil: "Mobilgear 634", total: "Carter EP 460", naftal: "Fodda 460" }' if lub_type == 'OIL' else '{ bp: "Energrease LS-EP2", shell: "Alvania Grease EP2", mobil: "Mobilux EP2", total: "Multis EP2", naftal: "Tessala EP2" }'
            if 'Copper' in grade:
                brands_str = '{ other: "3 In One Anti-Seize Copper Grease, Fuchs-PBC/DGrease Anti-Seize" }'
            
            new_entries.append(f'''  {{
    id: '{part_id}',
    tagNo: '300-Z-01',
    description: 'EOT Crane for Feed Gas Compressor Shelter',
    part: '{part_desc}',
    package: 'JI2045-0-PFM113',
    type: LubricantType.{lub_type},
    grade: '{grade}',
    initialFill: '{init_fill}',
    topUpQty: '{topup}',
    topUpInterval: '{topup_int}',
    replacementInterval: '{repl_int}',
    brands: {brands_str},
    remarks: 'Inspect/check 12 month. Initial fill by package vendor'
  }}''')
            count += 1
    
    # Motor bearings for 300-Z-01
    for motor_type in ['HOIST', 'CT', 'LT']:
        motor_id = f'300-Z-01-{motor_type}-MOTOR'
        if motor_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{motor_id}',
    tagNo: '300-Z-01',
    description: 'EOT Crane for Feed Gas Compressor Shelter',
    part: '{motor_type} Motor Bearings',
    package: 'JI2045-0-PFM113',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Greased For Life'
  }}''')
            count += 1
    
    print(f"   ✓ أضيف {count} جزء رافعة 300-Z-01")
    
    # ========================================
    # CRANE 750-Z-01
    # ========================================
    print("[2] إضافة رافعة 750-Z-01...")
    
    crane_750_parts = [
        ('750-Z-01-HOIST', 'Hoist gearbox', 'OIL', 'ISO VG 460', '16 L', '1.52 L', '8640 hrs', '43200 hrs'),
        ('750-Z-01-WIRE', 'Wire rope & rope guide', 'GREASE', 'ISO 2137', '2500 g', '250 g', '4320 hrs', '8640 hrs'),
        ('750-Z-01-CT-GB', 'Cross Travel gearbox', 'GREASE', 'ISO 2137', '200 g', '200 g', '8640 hrs', '43200 hrs'),
        ('750-Z-01-LT-GB1', 'Long Travel gearbox 1', 'OIL', 'ISO VG 460', '1 L', '0.25 L', '8640 hrs', '43200 hrs'),
        ('750-Z-01-LT-GB2', 'Long Travel gearbox 2', 'OIL', 'ISO VG 460', '1 L', '0.25 L', '8640 hrs', '43200 hrs'),
        ('750-Z-01-SPLINE', 'Spline shaft cross travel', 'GREASE', 'ISO 2137', '200 g', '-', '-', '43200 hrs'),
        ('750-Z-01-SPRINGS', 'Springs on overload cut off', 'GREASE', 'ISO 2137', '50 g', '50 g', '8640 hrs', '8640 hrs'),
        ('750-Z-01-PANEL', 'Ex control panel enclosure', 'GREASE', 'ISO 2137 (Copper)', '100 g', '-', '-', '8640 hrs'),
    ]
    
    count = 0
    for part_id, part_desc, lub_type, grade, init_fill, topup, topup_int, repl_int in crane_750_parts:
        if part_id not in existing_ids:
            brands_str = '{ bp: "Energol GR XP460", shell: "Omala Oil 460", mobil: "Mobilgear 634", total: "Carter EP 460", naftal: "Fodda 460" }' if lub_type == 'OIL' else '{ bp: "Energrease LS-EP2", shell: "Alvania Grease EP2", mobil: "Mobilux EP2", total: "Multis EP2", naftal: "Tessala EP2" }'
            if 'Copper' in grade:
                brands_str = '{ other: "3 In One Anti-Seize Copper Grease, Fuchs-PBC/DGrease Anti-Seize" }'
            
            new_entries.append(f'''  {{
    id: '{part_id}',
    tagNo: '750-Z-01',
    description: 'EOT Crane for Sales Gas Compressor Shelter',
    part: '{part_desc}',
    package: 'JI2045-0-PFM113',
    type: LubricantType.{lub_type},
    grade: '{grade}',
    initialFill: '{init_fill}',
    topUpQty: '{topup}',
    topUpInterval: '{topup_int}',
    replacementInterval: '{repl_int}',
    brands: {brands_str},
    remarks: 'Inspect/check 12 month. Initial fill by package vendor'
  }}''')
            count += 1
    
    for motor_type in ['HOIST', 'CT', 'LT']:
        motor_id = f'750-Z-01-{motor_type}-MOTOR'
        if motor_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{motor_id}',
    tagNo: '750-Z-01',
    description: 'EOT Crane for Sales Gas Compressor Shelter',
    part: '{motor_type} Motor Bearings',
    package: 'JI2045-0-PFM113',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Greased For Life'
  }}''')
            count += 1
    
    print(f"   ✓ أضيف {count} جزء رافعة 750-Z-01")
    
    # ========================================
    # METHANOL INJECTION PUMPS (481)
    # ========================================
    print("[3] إضافة مضخات حقن الميثانول...")
    
    methanol_items = [
        ('481-P-01A-GEAR', '481-P-01A', 'Methanol Injection Pump', 'Gear', 'ISO VG 220 PAO', '5 L', '-', '-', '8000 hrs'),
        ('481-P-01B-GEAR', '481-P-01B', 'Methanol Injection Pump', 'Gear', 'ISO VG 220 PAO', '5 L', '-', '-', '8000 hrs'),
        ('481-P-01A-HEAD', '481-P-01A', 'Methanol Injection Pump', 'Pump Head', 'ISO VG 10', '0.65 L', '-', '-', '8000 hrs'),
        ('481-P-01B-HEAD', '481-P-01B', 'Methanol Injection Pump', 'Pump Head', 'ISO VG 10', '0.65 L', '-', '-', '8000 hrs'),
        ('481-PM-01A', '481-PM-01A', 'Methanol Injection Pump Motor', 'Bearings', '-', '-', '-', '-', '-'),
        ('481-PM-01B', '481-PM-01B', 'Methanol Injection Pump Motor', 'Bearings', '-', '-', '-', '-', '-'),
        ('481-P-51-GEAR', '481-P-51', 'Portable Methanol Injection Pump', 'Gear', 'ISO VG 220 PAO', '5 L', '-', '-', '8000 hrs'),
        ('481-P-61-GEAR', '481-P-61', 'Portable Methanol Injection Pump', 'Gear', 'ISO VG 220 PAO', '5 L', '-', '-', '8000 hrs'),
        ('481-P-51-HEAD', '481-P-51', 'Portable Methanol Injection Pump', 'Pump Head', 'ISO VG 10', '0.45 L', '-', '-', '8000 hrs'),
        ('481-P-61-HEAD', '481-P-61', 'Portable Methanol Injection Pump', 'Pump Head', 'ISO VG 10', '0.45 L', '-', '-', '8000 hrs'),
        ('481-PM-51', '481-PM-51', 'Portable Methanol Injection Pump Motor', 'Bearings', '-', '-', '-', '-', '-'),
        ('481-PM-62', '481-PM-62', 'Portable Methanol Injection Pump Motor', 'Bearings', '-', '-', '-', '-', '-'),
    ]
    
    count = 0
    for item_id, tag, desc, part, grade, init, topup, topup_int, repl in methanol_items:
        if item_id not in existing_ids:
            is_greased_for_life = grade == '-' and init == '-'
            lub_type = 'GREASE' if 'Motor' in desc else 'OIL'
            brands_str = '{}' if is_greased_for_life else '{ bp: "Enersyn HTX 220", shell: "Omala S4 GX 220/SHELL Morlina Oil 10", mobil: "Mobilgear SHC XMP 220/MOBIL Oil Velocite No.6", other: "CASTROL Tribol 1510/220 or Hyspin AWS10" }'
            remarks = 'Greased For Life' if is_greased_for_life else '1st fill by vendor. Oil change based on temperature'
            
            new_entries.append(f'''  {{
    id: '{item_id}',
    tagNo: '{tag}',
    description: '{desc}',
    part: '{part}',
    package: 'JI2045-0-PFM112',
    type: LubricantType.{lub_type},
    grade: '{grade}',
    initialFill: '{init}',
    topUpQty: '{topup}',
    topUpInterval: '{topup_int}',
    replacementInterval: '{repl}',
    brands: {brands_str},
    remarks: '{remarks}'
  }}''')
            count += 1
    
    print(f"   ✓ أضيف {count} مضخة ميثانول")
    
    # ========================================
    # CORROSION INHIBITOR PUMPS (30 pumps)
    # ========================================
    print("[4] إضافة مضخات Corrosion Inhibitor...")
    
    corrosion_pump_numbers = ['101', '102', '105', '108', '109', '110', '111', '112', '113', '114', 
                               '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', 
                               '125', '126', '127', '128', '129', '130', '131', '132', '133', '191']
    
    count = 0
    for pump_num in corrosion_pump_numbers:
        # Gear
        gear_id = f'{pump_num}-P-01-GEAR'
        if gear_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{gear_id}',
    tagNo: '{pump_num}-P-01',
    description: 'Corrosion Inhibitor Pump',
    part: 'Gear',
    package: 'JI2045-0-PFM112',
    type: LubricantType.OIL,
    grade: 'ISO VG 220 PAO',
    initialFill: '0.25 L',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '4000 hrs (first oil change in 300 hours)',
    brands: {{ bp: "Enersyn HTX 220", shell: "Omala S4 GX 220", mobil: "Mobilgear SHC XMP 220", other: "CASTROL Tribol 1510/220" }},
    remarks: 'First oil change in 300 hours'
  }}''')
            count += 1
        
        # Pump Head
        head_id = f'{pump_num}-P-01-HEAD'
        if head_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{head_id}',
    tagNo: '{pump_num}-P-01',
    description: 'Corrosion Inhibitor Pump',
    part: 'Pump Head',
    package: 'JI2045-0-PFM112',
    type: LubricantType.OIL,
    grade: 'ISO VG 10',
    initialFill: '0.25 L',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '8000 hrs',
    brands: {{ shell: "SHELL Morlina Oil 10", mobil: "MOBIL Oil Velocite No.6", other: "CASTROL Hyspin AWS10" }},
    remarks: ''
  }}''')
            count += 1
        
        # Motor
        motor_id = f'{pump_num}-PM-01'
        if motor_id not in existing_ids:
            new_entries.append(f'''  {{
    id: '{motor_id}',
    tagNo: '{pump_num}-PM-01',
    description: 'Corrosion Inhibitor Pump Motor',
    part: 'Bearings',
    package: 'JI2045-0-PFM112',
    type: LubricantType.GREASE,
    grade: '-',
    initialFill: '-',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '-',
    brands: {{}},
    remarks: 'Greased For Life'
  }}''')
            count += 1
    
    print(f"   ✓ أضيف {count} مضخة Corrosion Inhibitor")
    
    return new_entries, len(new_entries)

# ============================================
# MAIN EXECUTION
# ============================================
if __name__ == "__main__":
    print("\n" + "="*80)
    print("إضافة معدات إضافية من PDF")
    print("="*80)
    print("\nجاري الإضافة...\n")
    
    new_entries, count = generate_more_equipment()
    
    if count == 0:
        print("\n" + "="*80)
        print("✅ جميع المعدات موجودة بالفعل!")
        print("="*80)
    else:
        with open('data.ts', 'r', encoding='utf-8') as f:
            content = f.read()
        
        import re
        match = re.search(r'\n\];\n$', content)
        if match:
            insert_pos = match.start()
            new_content = content[:insert_pos] + ',\n' + ',\n'.join(new_entries) + content[insert_pos:]
            
            with open('data.ts', 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("\n" + "="*80)
            print("✅ تم بنجاح!")
            print("="*80)
            print(f"\n📊 عدد المعدات المضافة: {count}")
            print(f"📁 تم تحديث الملف: data.ts")
            print("\n" + "="*80)
        else:
            print("\n❌ خطأ: لم يتم العثور على نهاية الملف")
