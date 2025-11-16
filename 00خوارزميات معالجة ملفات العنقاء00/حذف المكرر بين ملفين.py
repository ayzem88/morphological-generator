def read_and_clean_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        # قراءة الملف وحذف الرموز
        content = file.read().replace(':', '').replace(',', '')
    # تحويل المحتوى إلى قائمة من الكلمات
    return content.split()

def compare_and_extract_duplicates(file1, file2):
    # قراءة وتنظيف الملفات
    list1 = read_and_clean_file(file1)
    list2 = read_and_clean_file(file2)

    # إيجاد الكلمات المكررة
    duplicates = list(set(list1) & set(list2))

    # إزالة الكلمات المكررة من القائمة الثانية
    list2 = [word for word in list2 if word not in duplicates]

    # إعادة كتابة الملف الثاني بدون الكلمات المكررة
    with open(file2, 'w', encoding='utf-8') as file:
        file.write('\n'.join(list2))
    
    # كتابة الكلمات المكررة في ملف جديد
    with open('J:\\مكرر.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(duplicates))

# تنفيذ الدالة
compare_and_extract_duplicates('أوزان_الرباعي.txt', 'New Text Document.txt')
