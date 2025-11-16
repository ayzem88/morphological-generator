import re
import os

class TextModifier:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.rules = []

    def add_rule(self, pattern, replacement):
        self.rules.append((pattern, replacement))

    def apply_rules(self, text):
        for pattern, replacement in self.rules:
            text = re.sub(pattern, replacement, text)
        return text

    def modify_files_in_folder(self):
        for file_name in os.listdir(self.folder_path):
            if file_name.endswith('.txt'):  # تأكد من أن الملف نصي
                file_path = os.path.join(self.folder_path, file_name)
                self.modify_text(file_path)

    def modify_text(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        modified_text = self.apply_rules(text)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_text)

folder_path = r"New folder"
modifier = TextModifier(folder_path)
modifier.add_rule(r'(?<!^)ءِ(?!$)', 'ئِ') # الهمزة المكسورة دائما
modifier.add_rule(r'(?<!^)ءِّ(?!$)', 'ئِّ') # الهمزة المشددة المكسورة دائما
modifier.add_rule(r'(?<=ِ)ء', 'ئ') # الهمزة المكسور ما قبلها دائما
modifier.add_rule(r'يء', 'يئ') # الهمزة التي قبلها ياء دون تشكيل
modifier.add_rule(r'يْء', 'يْئ') # الهمزة التي قبلها ياء دون تشكيل
modifier.add_rule(r'(?<=[َُِْ])ءُ', 'ؤُ') # الهمزة عليها ضمة وما قبلها عليه فتحة أو ضمة أو سكون
modifier.add_rule(r'(?<=ُ)ء', 'ؤ') # إذا كانت الهمزة عليها سكون أو فتحة أو ضمة، وما قبلها عليه  ضمة
modifier.add_rule(r'اءُ', 'اؤُ')  # تحويل الهمزة إلى ؤُ إذا كانت مسبوقة بألف دون حركة وعليها ضمة
modifier.add_rule(r'(?<=َ)ءُّ', 'ؤُّ')  # إذا كانت الهمزة عليها شدة وضمة وقبلها فتحة
modifier.add_rule(r'(?<=[َْ])ءَ', 'أَ') # إذا كانت الهمزة عليها فتحة وما قبلها عليه فتحة أو سكون
modifier.add_rule(r'(?<=[َْ])ءَّ', 'أَّ') # إذا كانت الهمزة عليها فتحة وشدة وما قبلها عليه فتحة أو سكون
modifier.add_rule(r'أَا', 'آ')  # استبدال "أَا" بـ "آ"
modifier.add_rule(r'أا', 'آ')  # استبدال "أا" بـ "آ"
modifier.add_rule(r'(?<=َ)ءْ', 'أْ') # إذا كانت الهمزة عليها سكون وما قبلها عليه فتحة
modifier.add_rule(r'ِء(\s|$)', 'ئ\g<1>') # الهمزة في نهاية الكلمة مسبوقة بكسرة تتحول إلى ئ
modifier.add_rule(r'ُء(\s|$)', 'ؤ\g<1>') # الهمزة في نهاية الكلمة مسبوقة بضمة تتحول إلى ؤ
modifier.add_rule(r'(?<=َ)ء', 'أ')  # لو وجدنا همزة دون حركة (ء) وقبلها فتحة نقلب الهمزة (أ) مثل (صَدَأ)

#modifier.add_rule(r'َءَ(\s|$)', 'أَ\g<1>') # الهمزة المتطرفة عليها فتحة وقبلها فتحة تتحول إلى أَ
#modifier.add_rule(r'ء(?=\s|$)', 'أ')  # إذا كانت الهمزة في نهاية الكلمة أو قبل مسافة أو نهاية السطر وما قبلها حرف عليه فتحة

modifier.modify_files_in_folder()
