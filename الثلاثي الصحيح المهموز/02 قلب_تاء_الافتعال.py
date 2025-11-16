import os

folder_path = r"New folder (2)"

def search_and_replace_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    text = text.replace('صْتَ', 'صْطَ') #اصتبر - اصطبر
    text = text.replace('صْتِ', 'صْطِ') #اصتبر - اصطبر
    text = text.replace('صْتُ', 'صْطُ') #اصتبر - اصطبر
    
    text = text.replace('ضْتَ', 'ضْطَ') #اضترد - اضطرد 
    text = text.replace('ضْتِ', 'ضْطِ') #اضترد - اضطرد 
    text = text.replace('ضْتُ', 'ضْطُ') #اضترد - اضطرد 
	
    text = text.replace('طْتَ', 'طْطَ') #اطترد - اططرد
    text = text.replace('طْتِ', 'طْطِ') #اطترد - اططرد
    text = text.replace('طْتُ', 'طْطُ') #اطترد - اططرد
    
    text = text.replace('ظْتَ', 'ظْظَ') #اظتلم - اظظلم
    text = text.replace('ظْتِ', 'ظْظِ') #اظتلم - اظظلم
    text = text.replace('ظْتُ', 'ظْظُ') #اظتلم - اظظلم

    text = text.replace('دْتَ', 'دْدَ') #ادتكر - اددكر 
    text = text.replace('دْتِ', 'دْدِ') #ادتكر - اددكر  
    text = text.replace('دْتُ', 'دْدُ') #ادتكر - اددكر 
	
    text = text.replace('ذْتَ', 'دْدَ') #اذتخر - اددخر
    text = text.replace('ذْتِ', 'دْدِ') #اذتخر - اددخر
    text = text.replace('ذْتُ', 'دْدُ') #اذتخر - اددخر
    
    text = text.replace('زْتَ', 'زْدَ') #ازتحم - ازدحم
    text = text.replace('زْتِ', 'زْدِ') #ازتحام - ازدحام
    text = text.replace('زْتُ', 'زْدُ') #ازتحم - ازدحم

    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        search_and_replace_in_file(file_path)
