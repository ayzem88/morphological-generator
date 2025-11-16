import os

def apply_morphological_balance(root, pattern):
    pattern_list = list(pattern)
    f_index = pattern.find('ف')
    a_index = pattern.find('ع')
    l_indexes = [i for i, letter in enumerate(pattern) if letter == 'ل']
    if f_index != -1:
        pattern_list[f_index] = root[0]
    if a_index != -1:
        pattern_list[a_index] = root[1]
    if len(l_indexes) == 2:  
        if l_indexes[0] != -1 and len(root) > 2:
            pattern_list[l_indexes[0]] = root[2]
        if l_indexes[1] != -1 and len(root) > 3:
            pattern_list[l_indexes[1]] = root[3]
    elif len(l_indexes) == 3:  
        if l_indexes[0] != -1 and len(root) > 2:
            pattern_list[l_indexes[0]] = root[2]
        if l_indexes[1] != -1 and len(root) > 3:
            pattern_list[l_indexes[1]] = root[3]
        if l_indexes[2] != -1 and len(root) > 4:
            pattern_list[l_indexes[2]] = root[4]
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
roots_file_path = r"New Text Document.txt"
weights_file_path = "أوزان_الرباعي.txt"
output_dir = "New folder"
process_roots_with_weights_and_save(roots_file_path, weights_file_path, output_dir)
