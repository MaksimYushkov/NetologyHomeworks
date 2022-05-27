# import os
# base_path = os.getcwd()
# dir_name = 'Task3'
# full_path = os.path.join(base_path, dir_name)
# files = os.listdir(full_path)
# print(full_path)
# print(files)

files = ['1.txt', '2.txt', '3.txt']


def sort_files(files_list):
    files_dict = {}
    new_files_order = []
    for file in files_list:
        with open(file, encoding='utf-8') as file_txt:
            count = 0
            for line in file_txt:
                count += 1
            files_dict[file] = count
    files_ = sorted(list(files_dict.values()))
    for file in files_:
        for key, value in files_dict.items():
            if file == value:
                new_files_order.append(key)
    return new_files_order


def wr_new_file(files_list):
    iter_count = 0
    for file in files_list:
        iter_count += 1
        with open(file, encoding='utf-8') as file_txt, open('4.txt', 'a+', encoding='utf-8') as file_fin:
            text = file_txt.readlines()
            count = len(text)
            file_fin.write(file + '\n')
            file_fin.write(str(count) + '\n')
            for line in text:
                file_fin.write(line)
            if iter_count != len(files_list):
                file_fin.write('\n')
            else:
                pass


wr_new_file(sort_files(files))
