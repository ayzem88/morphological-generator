import re
import os

class TextModifier:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.total_modifications = 0  # متغير لتتبع عدد التعديلات

    def modify_files_in_folder(self):
        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                modified_content, modifications = self.clean_text(content)  # تعديل لتعيد عدد التعديلات
                self.total_modifications += modifications  # تحديث العدد الإجمالي للتعديلات
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(modified_content)
        print(f"إجمالي التعديلات: {self.total_modifications}")

    def clean_text(self, content):
        modifications = 0  # عدد التعديلات لهذا المحتوى
        patterns = [
            (r'(\u064B|\u064C|\u064D|\u064E|\u064F|\u0650|\u0651|\u0652)\1+', r'\1'),  # تقليل الحركات المكررة لواحدة
            (r'(?<=\s)(\u064B|\u064C|\u064D|\u064E|\u064F|\u0650|\u0651|\u0652)', '')  # إزالة الحركة الزائدة التي لا تتبع حرفاً
        ]
        for pattern, replacement in patterns:
            new_content, count = re.subn(pattern, replacement, content)  # استخدام subn للحصول على عدد التعديلات
            modifications += count
            content = new_content
        return content, modifications

# استخدام الكلاس
folder_path = r"C:\Users\Aymen\Desktop\المعتل الثلاثي\عينة_تصريف_جاهز_دون_تكرار"
modifier = TextModifier(folder_path)

# تعديل الملفات في المجلد
modifier.modify_files_in_folder()
