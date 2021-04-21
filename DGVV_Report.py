import os
import ctypes

print('Укажите путь до директории с файлами')
directory = str(input())
print('Укажите символы окончания всех файлов')
member_trigger = str(input())
cmd = ("cd" + " " + '"' + "C:\\Program Files\\7-Zip" + '"' + " " + "&& 7z x" + " " + directory + " " + "-o" + '"' +
       directory + '"' + " " + "&& cd" + " " + '"' + directory + '"' + " " + "&& DEL /Q *.7z")
os.system(cmd)


for filename in os.listdir(directory):
    if filename.endswith(member_trigger):
        first_path_of_file = list(filename)
        second_path_of_file = list(filename)
        third_path_of_file = list(filename)
        stop_trigger = (filename.index('m'))
        del first_path_of_file[stop_trigger:]
        new_name_f = ''.join(map(str, first_path_of_file))
        del second_path_of_file[:stop_trigger]
        new_spof = second_path_of_file
        add_stop_trigger = (second_path_of_file.index('_'))
        del new_spof[add_stop_trigger:]
        new_name_s = ''.join(map(str, new_spof))
        third_trigger = (filename.index('_'))
        del third_path_of_file [:third_trigger]
        new_end_file = ''.join(map(str, third_path_of_file))
        new_file_name = (new_name_s + new_name_f + new_end_file)
        print(new_file_name)
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_file_name))
ctypes.windll.user32.MessageBoxW(0, "Операция замены успешно выполнена", "Поздравляем", 1)






