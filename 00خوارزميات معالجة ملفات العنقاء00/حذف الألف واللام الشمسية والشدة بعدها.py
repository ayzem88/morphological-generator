import re
import os

class TextModifier:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.replacement_rules = []

    def add_rule(self, pattern, replacement):
        self.replacement_rules.append((pattern, replacement))

    def modify_file_content(self, content):
        modified_content = content
        for pattern, replacement in self.replacement_rules:
            modified_content = re.sub(pattern, replacement, modified_content, flags=re.MULTILINE)
        return modified_content

    def modify_files_in_folder(self):
        for filename in os.listdir(self.folder_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(self.folder_path, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                modified_content = self.modify_file_content(content)
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(modified_content)

folder_path = "New folder"
modifier = TextModifier(folder_path)
modifier.add_rule(r'^(ال)([أ-ي])\u0651', r'\2')  # هذه القاعدة تستهدف "ال" والشدة بعدها مباشرة في أول السطر
modifier.add_rule(r'(\s)([أ-ي])\u0651', r'\1\2') # لحذف الشدة التي قبلها فراغ دون حرف
modifier.modify_files_in_folder()
