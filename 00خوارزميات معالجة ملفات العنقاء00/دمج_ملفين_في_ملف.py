import os

def read_file_content(file_path):
    content_dict = {}
    current_tag = ""
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('#'):
                current_tag = line.strip()
                if current_tag not in content_dict:
                    content_dict[current_tag] = line  # حفظ الوسم مع المحتوى
            else:
                content_dict[current_tag] += line
    return content_dict

def read_file_content_without_tags(file_path):
    content_dict = {}
    current_tag = ""
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('#'):
                current_tag = line.strip()
                if current_tag not in content_dict:
                    content_dict[current_tag] = ""
            else:
                content_dict[current_tag] += line
    return content_dict

def merge_files(file1_path, file2_path, output_file_path):
    content1 = read_file_content(file1_path)
    content2 = read_file_content_without_tags(file2_path)  # قراءة المحتوى من الملف 2 دون الوسوم
    for tag, content in content2.items():
        if tag in content1 and content.strip():
            content1[tag] = content1[tag].rstrip() + "\n\n" + content.strip() + "\n\n"
        elif content.strip():
            content1[tag] = content.strip() + "\n\n"
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for content in content1.values():
            output_file.write(content)

def process_directory(dir1_path, dir2_path, output_dir_path):
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)
    
    files1 = os.listdir(dir1_path)
    files2 = os.listdir(dir2_path)
    
    for file1 in files1:
        if file1 in files2:
            file1_path = os.path.join(dir1_path, file1)
            file2_path = os.path.join(dir2_path, file1)
            output_file_path = os.path.join(output_dir_path, file1)
            merge_files(file1_path, file2_path, output_file_path)
            print(f"تم دمج الملف {file1} بنجاح وحفظه في {output_file_path}.")

dir1_path = r"الرباعي_الصحيح_كامل"
dir2_path = r"الرباعي_المعتل_كامل"
output_dir_path = "الرباعي_كامل"

process_directory(dir1_path, dir2_path, output_dir_path)
