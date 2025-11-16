import re

# فتح وقراءة الملف
try:
    with open(r"J:\نظام التصريف والاشتقاق الصرفي\الرباعي_الصحيح_كامل\سبرر.txt", "r", encoding="utf-8") as file:
        content = file.readlines()

    # إعداد ملف النتيجة لكتابة الكلمات المطابقة
    with open(r"J:\نظام التصريف والاشتقاق الصرفي\نتيجة.txt", "w", encoding="utf-8") as result_file:
        for line in content:
            # البحث عن النمط في كل سطر
            # هذا النمط يبحث عن أي حرف عربي متبوعًا بسكون ثم نفس الحرف متبوعًا بفتحة، ضمة أو كسرة
            matches = re.findall(r'(\w)(ْ)\1[َُِ]', line)
            if matches:
                # كتابة السطر في الملف إذا تم العثور على مطابقة
                result_file.write(line)

    print("تمت العملية بنجاح، وتم كتابة النتائج في ملف 'نتيجة.txt'.")
except Exception as e:
    print(f"حدث خطأ أثناء محاولة قراءة الملف أو كتابة النتائج: {e}")
