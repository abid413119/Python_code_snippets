from os import listdir, mkdir, rename
from os.path import isfile, join, exists

source_folder = '/home/abid/Downloads'
items_list = listdir(source_folder)
extension_to_folder_mapper = {
    'jpeg jpg png gif svg': 'images', 
    'app dmg pkg': 'applications',
    'txt xlsx xls doc docx pdf': 'documents',
    'py pyc whl sh': 'programming-files',
    'mp3 mp4 mkv': 'media' 
}


def get_file_extension(file_name):
    split_name = file_name.split('.')
    return split_name[-1]


def create_folder(folder_name):
    if not exists(join(source_folder, folder_name)):
        mkdir(join(source_folder, folder_name))
        print('folder created.')


def move_file_to_folder(name, folder_name):
    old_path = join(source_folder, name)
    print(old_path)
    new_path = join(source_folder, folder_name, name)
    print(new_path)
    rename(old_path, new_path)


def map_extension_to_folder(extension, name):
    folder_name = 'others'
    for extension_list, destination_folder in extension_to_folder_mapper.items():
        if extension in extension_list.split(' '):
            folder_name = destination_folder
            break
    create_folder(folder_name)
    move_file_to_folder(name, folder_name)


def main():
    for item_name in items_list:
        if isfile(join(source_folder, item_name)):
            extension = get_file_extension(item_name)
            map_extension_to_folder(extension, item_name)


main()