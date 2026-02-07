#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add ALL Air Cooler MOTORS (Drive End & Non-Drive End)
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

def generate_air_cooler_motors():
    """Generate all Air Cooler Motor entries (DE & NDE)"""
    
    existing_ids, current_content = read_current_data()
    
    new_entries = []
    
    print("="*80)
    print("إضافة محركات Air Cooler (Drive End & Non-Drive End)")
    print("="*80)
    
    # Define all air cooler motors with their specifications
    air_cooler_motors = [
        # Feed Gas Compressor After Cooler Motors
        ('301-EAM-01', 'Feed Gas Compressor After Cooler Motor', 18, '27 g', '4000', '6314-C3'),
        ('302-EAM-01', 'Feed Gas Compressor After Cooler Motor', 18, '27 g', '4000', '6314-C3'),
        ('303-EAM-01', 'Feed Gas Compressor After Cooler Motor', 18, '27 g', '4000', '6314-C3'),
        
        # Hot Oil Trim Cooler Motor
        ('401-EAM-01', 'Hot Oil Trim Cooler Motor', 2, '11 g (DE) / 7 g (NDE)', '14000 (DE) / 17000 (NDE)', '6308-C3 (DE) / 6207-C3 (NDE)'),
        
        # Gas Dehydrator Regeneration Gas Cooler Motors
        ('510-EAM-01', 'Gas Dehydrator Regeneration Gas Cooler Motor', 4, '13 g (DE) / 9 g (NDE)', '13000 (DE) / 14000 (NDE)', '6309-C3'),
        ('610-EAM-01', 'Gas Dehydrator Regeneration Gas Cooler Motor', 4, '13 g (DE) / 9 g (NDE)', '13000 (DE) / 14000 (NDE)', '6309-C3'),
        
        # LPG Splitter Condenser Motors
        ('530-EAM-02', 'LPG Splitter Condenser Motor', 16, '18 g (DE) / 11 g (NDE)', '11000 (DE) / 12000 (NDE)', '6311-C3 (DE) / 6211-C3 (NDE)'),
        ('630-EAM-02', 'LPG Splitter Condenser Motor', 16, '18 g (DE) / 11 g (NDE)', '11000 (DE) / 12000 (NDE)', '6311-C3 (DE) / 6211-C3 (NDE)'),
        
        # Condensate Rundown Cooler Motors
        ('530-EAM-03', 'Condensate Rundown Cooler Motor', 4, '18 g (DE) / 11 g (NDE)', '11000 (DE) / 12000 (NDE)', '6311-C3 (DE) / 6211-C3 (NDE)'),
        ('630-EAM-03', 'Condensate Rundown Cooler Motor', 4, '18 g (DE) / 11 g (NDE)', '11000 (DE) / 12000 (NDE)', '6311-C3 (DE) / 6211-C3 (NDE)'),
        
        # Sales Gas Compressor After Cooler Motor
        ('750-EAM-03', 'Sales Gas Compressor After Cooler Motor', 10, '27 g', '4000', '6314-C3'),
        
        # Sales Gas Compressor Suction Cooler Motors
        ('751-EAM-01', 'Sales Gas Compressor Suction Cooler Motor', 8, '27 g', '4000', '6314-C3'),
        ('752-EAM-01', 'Sales Gas Compressor Suction Cooler Motor', 8, '27 g', '4000', '6314-C3'),
        ('753-EAM-01', 'Sales Gas Compressor Suction Cooler Motor', 8, '27 g', '4000', '6314-C3'),
        ('754-EAM-01', 'Sales Gas Compressor Suction Cooler Motor', 8, '27 g', '4000', '6314-C3'),
        
        # Sales Gas Compressor Interstage Cooler Motors
        ('751-EAM-02', 'Sales Gas Compressor Interstage Cooler Motor', 16, '18 g (DE) / 11 g (NDE)', '11000 (DE) / 12000 (NDE)', '6311-C3 (DE) / 6211-C3 (NDE)'),
        ('752-EAM-02', 'Sales Gas Compressor Interstage Cooler Motor', 16, '18 g (DE) / 11 g (NDE)', '11000 (DE) / 12000 (NDE)', '6311-C3 (DE) / 6211-C3 (NDE)'),
        ('753-EAM-02', 'Sales Gas Compressor Interstage Cooler Motor', 16, '18 g (DE) / 11 g (NDE)', '11000 (DE) / 12000 (NDE)', '6311-C3 (DE) / 6211-C3 (NDE)'),
        ('754-EAM-02', 'Sales Gas Compressor Interstage Cooler Motor', 16, '18 g (DE) / 11 g (NDE)', '11000 (DE) / 12000 (NDE)', '6311-C3 (DE) / 6211-C3 (NDE)'),
    ]
    
    count = 0
    for motor_tag, desc, qty, init_fill, repl, bearing in air_cooler_motors:
        # Check if this motor has separate DE/NDE entries or combined
        if 'DE' in init_fill or 'NDE' in init_fill:
            # Create separate entries for DE and NDE
            motor_de_id = f'{motor_tag}-DE'
            motor_nde_id = f'{motor_tag}-NDE'
            
            if motor_de_id not in existing_ids:
                de_fill = init_fill.split('/')[0].strip().replace('(DE)', '').strip()
                de_repl = repl.split('/')[0].strip().replace('(DE)', '').strip()
                de_bearing = bearing.split('/')[0].strip().replace('(DE)', '').strip()
                
                new_entries.append(f'''  {{
    id: '{motor_de_id}',
    tagNo: '{motor_tag}',
    description: '{desc}',
    part: 'MOTOR DRIVE END / {de_bearing}',
    package: 'JI2045-0-PFM001',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '{de_fill}',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '{de_repl} hrs',
    brands: {{ mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2, SKF - LGHP2' }},
    remarks: ''
  }}''')
                count += 1
            
            if motor_nde_id not in existing_ids:
                nde_fill = init_fill.split('/')[1].strip().replace('(NDE)', '').strip()
                nde_repl = repl.split('/')[1].strip().replace('(NDE)', '').strip()
                nde_bearing = bearing.split('/')[1].strip().replace('(NDE)', '').strip() if '/' in bearing else bearing
                
                new_entries.append(f'''  {{
    id: '{motor_nde_id}',
    tagNo: '{motor_tag}',
    description: '{desc}',
    part: 'MOTOR NON DRIVE END / {nde_bearing}',
    package: 'JI2045-0-PFM001',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '{nde_fill}',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '{nde_repl} hrs',
    brands: {{ mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2, SKF - LGHP2' }},
    remarks: ''
  }}''')
                count += 1
        else:
            # Create both DE and NDE entries with same specs
            motor_de_id = f'{motor_tag}-DE'
            motor_nde_id = f'{motor_tag}-NDE'
            
            if motor_de_id not in existing_ids:
                new_entries.append(f'''  {{
    id: '{motor_de_id}',
    tagNo: '{motor_tag}',
    description: '{desc}',
    part: 'MOTOR DRIVE END / {bearing}',
    package: 'JI2045-0-PFM001',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '{init_fill}',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '{repl} hrs',
    brands: {{ mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2, SKF - LGHP2' }},
    remarks: ''
  }}''')
                count += 1
            
            if motor_nde_id not in existing_ids:
                new_entries.append(f'''  {{
    id: '{motor_nde_id}',
    tagNo: '{motor_tag}',
    description: '{desc}',
    part: 'MOTOR NON DRIVE END / {bearing}',
    package: 'JI2045-0-PFM001',
    type: LubricantType.GREASE,
    grade: 'NLGI Grade 2',
    initialFill: '{init_fill}',
    topUpQty: '-',
    topUpInterval: '-',
    replacementInterval: '{repl} hrs',
    brands: {{ mobil: 'MOBIL POLYREX EM', other: 'Chevron - SRI NLGI2, SKF - LGHP2' }},
    remarks: ''
  }}''')
                count += 1
    
    print(f"\n✓ أضيف {count} محرك Air Cooler (DE & NDE)")
    
    return new_entries, count

# ============================================
# MAIN EXECUTION
# ============================================
if __name__ == "__main__":
    print("\n" + "="*80)
    print("إضافة محركات Air Cooler المفقودة")
    print("="*80)
    print("\nجاري الإضافة...\n")
    
    new_entries, count = generate_air_cooler_motors()
    
    if count == 0:
        print("\n" + "="*80)
        print("✅ جميع محركات Air Cooler موجودة بالفعل!")
        print("="*80)
    else:
        # Read current file
        with open('data.ts', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find position
        import re
        match = re.search(r'\n\];\n$', content)
        if match:
            insert_pos = match.start()
            
            # Insert new entries
            new_content = content[:insert_pos] + ',\n' + ',\n'.join(new_entries) + content[insert_pos:]
            
            # Write back
            with open('data.ts', 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("\n" + "="*80)
            print("✅ تم بنجاح!")
            print("="*80)
            print(f"\n📊 عدد محركات Air Cooler المضافة: {count}")
            print(f"📁 تم تحديث الملف: data.ts")
            print("\n" + "="*80)
        else:
            print("\n❌ خطأ: لم يتم العثور على نهاية الملف")
