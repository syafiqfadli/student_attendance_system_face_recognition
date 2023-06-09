from src.features.encode_from_db import encode_registered_students
from src.features.recognize_face import list_students
from src.features.take_picture import take_picture
from src.features.clear_helper import *


def _folder_checker(class_name: str):
    folder_list = (
        "src/encoders/{}".format(class_name),
        "src/captures/students/detected/{}".format(class_name),
        "src/captures/students/named/{}".format(class_name)
    )

    for folder in folder_list:

        check_folder = os.path.isdir(folder)

        if not check_folder:
            os.makedirs(folder)


def _dataset_checker(class_name: str):
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


def _display_menu(class_name: str):
    clear_screen()

    print("Class Name [{}]".format(class_name.upper()))
    print("---------------------")
    print("Choose One(1) option:")
    print("")
    print("1. Main Menu")
    print("2. Take Picture")
    print("3. Train Model")
    print("4. Take Attendance")
    print("5. Exit")
    print("")
    print("---------------------")


def _option2(class_name: str):
    clear_screen()

    print("TAKE PICTURE")
    print("------------")
    take_picture(class_name)
    print("")
    input("[Press Enter key to continue...] ")


def _option3(class_name: str):
    clear_screen()

    print("TRAIN MODEL")
    print("-----------")
    encode_registered_students(class_name)
    print("")
    input("[Press Enter key to continue...] ")


def _option4(class_name: str):
    clear_screen()

    print("TAKE ATTENDANCE")
    print("---------------")
    list_students(class_name)
    print("")
    input("[Press Enter key to continue...] ")


def _option_menu(class_name: str):
    while (True):
        _display_menu(class_name)
        user_input = input("Option: ")

        if user_input == "1":
            break

        elif user_input == "2":
            _option2(class_name)

        elif user_input == "3":
            _option3(class_name)

        elif user_input == "4":
            _option4(class_name)

        elif user_input == "5":
            clear_screen()
            print("Program finished.")
            exit()

        else:
            print("\nInvalid option!")
            print("")
            input("[Press Enter key to continue...] ")
            continue


def _main_menu():
    while (True):
        clear_screen()

        print("MAIN MENU")
        print("---------")
        class_input = str(input("Enter class name: ")).upper()

        if (class_input == ""):
            continue

        dataset_result = _dataset_checker(class_input)

        if (dataset_result == -1):
            print("")
            is_continue = str(input("Continue? [y/n]: ")).lower()

            if (is_continue == "y" or is_continue == ""):
                continue
            else:
                clear_screen()
                print("Program finished.")
                break

        clear_screen()
        _option_menu(class_input)


def main():
    try:
        _main_menu()
    except KeyboardInterrupt:
        clear_screen()
        print("Program finished.")
        exit()


if __name__ == "__main__":
    main()
