import re
import os

class TextModifier:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def modify_files_in_folder(self):
        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.readlines()

                modified_content = []
                moved_parts = []
                for line in content:
                    # تحديث النمط ليشمل السطور التي تنتهي بنقطتين دون نص بعدها
                    if re.match(r'^[^:\n]+:\s*$', line.strip()):
                        moved_parts.append(line)
                    else:
                        modified_content.append(line)

                with open(file_path, 'w', encoding='utf-8') as file:
                    file.writelines(modified_content + moved_parts)

# مثال على الاستخدام
folder_path = r"C:\Users\Aymen\Desktop\المعتل الثلاثي\التصريف_مشترك_جاهز_دون_تكرار"
modifier = TextModifier(folder_path)
modifier.modify_files_in_folder()
