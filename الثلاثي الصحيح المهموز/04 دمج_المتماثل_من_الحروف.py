import os
import re

folder_path = r"New folder"

def search_and_replace_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    pattern = re.compile(r'(\w)ْ\1([َُِ])')
    def merge_match(match):
        char = match.group(1)  # الحصول على الحرف
        vowel = match.group(2)  # الحصول على الحركة (ضمة، فتحة، كسرة)
        return f'{char}ّ{vowel}'  # دمج الحرفين بشدة ونقل الحركة

    text = re.sub(pattern, merge_match, text)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        search_and_replace_in_file(file_path)
