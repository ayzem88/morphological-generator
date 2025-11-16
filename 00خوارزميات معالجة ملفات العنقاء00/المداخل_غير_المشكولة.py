import re
import os

class TextModifier:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.replacement_rules = []
        self.deletion_rules = []

    def modify_files_in_folder(self):
        entries_file_path = os.path.join(self.folder_path, 'مداخل.txt')
        with open(entries_file_path, 'w', encoding='utf-8') as entries_file:
            for filename in os.listdir(self.folder_path):
                file_path = os.path.join(self.folder_path, filename)
                if os.path.isfile(file_path) and filename != 'مداخل.txt':
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        extracted_entries = self.extract_partial_voweled_entries(content)
                        for entry in extracted_entries:
                            entries_file.write(f"{entry}\n")

    def extract_partial_voweled_entries(self, content):
        # نمط للبحث عن المداخل التي لا تحتوي على تشكيل كامل وتنتهي بنقطتين
        pattern = r'^([^أ-ي\s]*[أ-ي]+(?:[ًٌٍَُِّ]*[أ-ي]+)*[ًٌٍَُِّ]*):'
        partial_voweled_entries = re.findall(pattern, content, flags=re.MULTILINE)
        # استبعاد المداخل المشكولة بالكامل
        filtered_entries = [entry for entry in partial_voweled_entries if not re.match(r'^[\u0621-\u064Aًٌٍَُِّ]+:$', entry)]
        return filtered_entries

folder_path = r"C:\Users\Aymen\Desktop\المعتل الثلاثي\التصريف_مشترك_جاهز_دون_تكرار"
modifier = TextModifier(folder_path)
modifier.modify_files_in_folder()
