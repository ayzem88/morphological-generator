import os

folder_path = r"New folder (2)"

def search_and_replace_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    text = text.replace('طْطَ', 'طَّ') # اطترد - اططرد - اطَّرد
    text = text.replace('طْطِ', 'طِّ') 
    text = text.replace('طْطُ', 'طُّ') 
	
    text = text.replace('ظْظَ', 'ظَّ') # اظتلم - اظظلم - اظَّلم
    text = text.replace('ظْظِ', 'ظَّ') 
    text = text.replace('ظْظُ', 'ظَّ') 
	
    text = text.replace('دْدَ', 'دَّ') #ادتهن - اددهن - ادَّهن
    text = text.replace('دْدِ', 'دِّ') 
    text = text.replace('دْدُ', 'دُّ') 
    
    text = text.replace('ذْذَ', 'دَّ') #اذتخر - ادَّخر
    text = text.replace('ذْذِ', 'دِّ') #اذتكر - ادَّكر
    text = text.replace('زْتُ', 'دُّ')

    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        search_and_replace_in_file(file_path)
