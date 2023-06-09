import os
from src.features.clear_helper import *

def _folder_checker(class_name: str):
    folder_list = (
        "src/encoders/{}".format(class_name),
        "src/captures/classes/{}".format(class_name),
        "src/captures/students/detected/{}".format(class_name),
        "src/captures/students/named/{}".format(class_name)
    )

    for folder in folder_list:

        check_folder = os.path.isdir(folder)

        if not check_folder:
            os.makedirs(folder)


def dataset_checker(class_name: str):
    detected_students_folder = "src/captures/students/detected/{}".format(
        class_name)
    named_students_folder = "src/captures/students/named/{}".format(
        class_name)
    dataset_path = "src/datasets/{}".format(class_name)
    check_folder = os.path.isdir(dataset_path)

    if not check_folder:
        print("")
        print("No datasets found for this class.")
        return -1

    _folder_checker(class_name)

    result_detected = clear_folder(detected_students_folder)
    result_named = clear_folder(named_students_folder)

    if (result_detected == -1 or result_named == -1):
        return -1

    return 1