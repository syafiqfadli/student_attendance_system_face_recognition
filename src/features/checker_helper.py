import os
from src.features.clear_helper import *


def _folder_checker(class_name: str):
    folder_list = (
        "src/encoders/{}".format(class_name),
        "src/attendance/{}".format(class_name),
        "src/captures/classes/{}".format(class_name),
        "src/captures/students/detected/{}".format(class_name),
        "src/captures/students/named/{}".format(class_name)
    )

    for folder in folder_list:

        check_folder = os.path.isdir(folder)

        if not check_folder:
            os.makedirs(folder)


def dataset_checker(class_name: str):
    dataset_path = "src/datasets/{}".format(class_name)
    check_folder = os.path.isdir(dataset_path)

    if not check_folder:
        print("")
        print("No datasets found for this class.")
        return -1

    _folder_checker(class_name)

    return 0
