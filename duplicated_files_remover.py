import os
import sys

def main(folder_path: str):
    print('====================')
    duplicates: list[str] = []
    for filename in os.listdir(folder_path):
        if 'kopia' in filename:
            duplicates.append(filename)
            print(filename)

    if not duplicates:
        print('No duplicates found')
        return
    print('====================')
    print(f'{len(duplicates)} duplicates found')

    while True:
        confirm = input('Are you sure you want to delete these files? (y/n): ')
        if confirm.lower() in ['y', 'yes', 'n', 'no']:
            break
        print('Invalid input')
    if confirm.lower() not in  ['y', 'yes']:
        print('Exiting...')
        return

    print('Deleting duplicates...')
    for duplicate in duplicates:
        os.remove(os.path.join(folder_path, duplicate))
    print('Duplicates deleted')


if __name__ == '__main__':
    path_exist = False
    folder_path = ''
    if sys.argv and len(sys.argv) >= 2:
        if os.path.exists(sys.argv[1]):
            path_exist = True
            folder_path = sys.argv[1]

    while not path_exist:
        folder_path = input('Enter the folder path: ')
        if os.path.exists(folder_path):
            path_exist = True
        print('Invalid path')

    main(folder_path)