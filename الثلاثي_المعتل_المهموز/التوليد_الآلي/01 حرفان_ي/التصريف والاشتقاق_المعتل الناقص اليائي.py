import os

def apply_morphological_balance(root, pattern):
    if len(root) != 3:  
        raise ValueError("الجذر يجب أن يتكون من 3 حروف فقط")
    pattern_list = list(pattern)
    f_index = pattern.find('ف')
    a_indexes = [i for i, letter in enumerate(pattern) if letter == 'ع']
    l_indexes = [i for i, letter in enumerate(pattern) if letter == 'ل']

    # استبدال حرف "ف" بالحرف الأول من الجذر
    if f_index != -1:
        pattern_list[f_index] = root[0]
    
    # استبدال جميع تكرارات "ع" بالحرف الثاني من الجذر
    for a_index in a_indexes:
        if a_index != -1:
            pattern_list[a_index] = root[1]

    # استبدال حرف "ل" بالحرف الثالث من الجذر، مع الأخذ بعين الاعتبار للتكرار
    for l_index in l_indexes:
        if l_index != -1:
            pattern_list[l_index] = root[2]

    result = ''.join(pattern_list)
    return result

def process_header(root, header):
    return apply_morphological_balance(root, header)

def process_weights_line(line, root):
    parts = line.split(':')
    header = process_header(root, parts[0].strip()) + ': ' if len(parts) > 0 else ''
    weights = parts[1].split('،') if len(parts) > 1 else []
    processed_weights = []
    for weight in weights:
        processed_weight = apply_morphological_balance(root, weight.strip())
        processed_weights.append(processed_weight)
    return header + '، '.join(processed_weights)

def process_roots_with_weights_and_save(roots_file_path, weights_file_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(weights_file_path, 'r', encoding='utf-8') as file:
        lines_with_comments = file.readlines()
    with open(roots_file_path, 'r', encoding='utf-8') as file:
        roots = file.read().splitlines()
    for root in roots:
        output_path = os.path.join(output_dir, f'{root}.txt')
        with open(output_path, 'w', encoding='utf-8') as output_file:
            for line in lines_with_comments:
                if line.strip().startswith('#') or ':' not in line:
                    output_file.write(line)
                else:
                    modified_line = process_weights_line(line, root)
                    output_file.write(modified_line + '\n')


roots_file_path = r"حرفان_ي.txt"
weights_file_path = "أوزان_الثلاثي_الناقص_اليائي.txt"
output_dir = "ألفاظ مولدة آليا"
process_roots_with_weights_and_save(roots_file_path, weights_file_path, output_dir)
