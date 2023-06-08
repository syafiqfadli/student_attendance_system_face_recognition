import os
import shutil


def clear_folder(folder_path: str):
    try:
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
        return -1


def clear_screen():
    os.system("clear && printf '\e[3J'")  # For MacOS
    # os.system("cls") # For Windows
