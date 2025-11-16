def classify_and_save_roots(roots):
    # تهيئة القواميس لتخزين الجذور حسب التصنيفات المطلوبة
    groups = {
        'و حرفان': [],
        'حرفان و': [],
        'حرف و حرف': [],
        'وو حرف': [],
        'حرف وو': [],
        'و حرف و': [],
        'ي حرفان': [],
        'حرفان ي': [],
        'حرف ي حرف': [],
        'ي ي حرف': [],
        'حرف ي ي': [],
        'ي حرف ي': [],
        'ي حرف و': [],
        'و حرف ي': [],
        'و ي حرف': [],
        'ي و حرف': [],
        'حرف و ي': [],
        'حرف ي و': [],
    }

    # التصنيف بناءً على الشروط
    for root in roots:
        # الشروط المتعلقة بالواو
        if root.startswith('و') and root[1] not in ('و', 'ي') and root[2] not in ('و', 'ي'):
            groups['و حرفان'].append(root)
        elif root.endswith('و') and all(c not in ('و', 'ي') for c in root[:2]):
            groups['حرفان و'].append(root)
        elif root[1] == 'و' and all(c not in ('و', 'ي') for c in [root[0], root[2]]):
            groups['حرف و حرف'].append(root)
        elif root.startswith('وو') and root[2] not in ('ي'):
            groups['وو حرف'].append(root)
        elif root.endswith('وو'):
            groups['حرف وو'].append(root)
        elif root.startswith('و') and root.endswith('و') and root[1] not in ('و', 'ي'):
            groups['و حرف و'].append(root)

        # الشروط المتعلقة بالياء
        elif root.startswith('ي') and root[1] not in ('و', 'ي') and root[2] not in ('و', 'ي'):
            groups['ي حرفان'].append(root)
        elif root.endswith('ي') and all(c not in ('و', 'ي') for c in root[:2]):
            groups['حرفان ي'].append(root)
        elif root[1] == 'ي' and all(c not in ('و', 'ي') for c in [root[0], root[2]]):
            groups['حرف ي حرف'].append(root)
        elif root.startswith('يي') and root[2] not in ('و'):
            groups['ي ي حرف'].append(root)
        elif root.endswith('يي'):
            groups['حرف ي ي'].append(root)
        elif root.startswith('ي') and root.endswith('ي') and root[1] not in ('و', 'ي'):
            groups['ي حرف ي'].append(root)

        # الشروط المتعلقة بالمزج بين الواو والياء
        elif root.startswith('ي') and root.endswith('و') and root[1] not in ('و', 'ي'):
            groups['ي حرف و'].append(root)
        elif root.startswith('و') and root.endswith('ي') and root[1] not in ('و', 'ي'):
            groups['و حرف ي'].append(root)
        elif root.startswith('وي') and root[2] not in ('و', 'ي'):
            groups['و ي حرف'].append(root)
        elif root.startswith('يو') and root[2] not in ('و', 'ي'):
            groups['ي و حرف'].append(root)
        elif root.endswith('وي'):
            groups['حرف و ي'].append(root)
        elif root.endswith('يو'):
            groups['حرف ي و'].append(root)

    # إرجاع القواميس المحدثة
    return groups

def save_roots(groups):
    # حفظ كل مجموعة في ملف نصي
    for group_name, roots in groups.items():
        file_name = f"{group_name.replace(' ', '_')}.txt"
        with open(file_name, 'w', encoding='utf-8') as file:
            for root in roots:
                file.write(f"{root}\n")

# قراءة الجذور من الملف
file_path = 'J:/نظام التصريف والاشتقاق الصرفي/000المعتل000/جذور_الثلاثي_المعتل.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    roots = file.read().splitlines()

# تصنيف الجذور
groups = classify_and_save_roots(roots)

# حفظ الجذور في الملفات المناسبة
save_roots(groups)

# استكمال تحديث الملف الأصلي بالجذور غير المستخدمة
used_roots = [root for group in groups.values() for root in group]
remaining_roots = [root for root in roots if root not in used_roots]

# إعادة كتابة الملف الأصلي بالجذور المتبقية
with open(file_path, 'w', encoding='utf-8') as file:
    for root in remaining_roots:
        file.write(f"{root}\n")
