import os

print('Укажите путь до директории с файлами')
directory = str(input())
print('Укажите символы окончания всех файлов')
member_trigger = str(input())
oms_to_zip = ('ren' + " " + '"' + directory + '\*.*' + '"' + " " + '*.zip')
os.system(oms_to_zip)
os.system("pause")
