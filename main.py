from src.features.encode_from_db import encode_registered_students
from src.features.recognize_face import list_students
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


def _display_menu(class_input: str):
    clear_screen()

    print("Class Name [{}]".format(class_input.upper()))
    print("---------------------")
    print("Choose One(1) option:")
    print("")
    print("1. Main Menu")
    print("2. Train Model")
    print("3. Take Attendance")
    print("4. Exit")
    print("")
    print("---------------------")


def _option2(class_input: str):
    clear_screen()

    while (True):
        print("TRAIN MODEL")
        print("-----------")
        encode_registered_students(class_input)
        print("")
        input("[Press Enter key to continue...] ")
        break


def _option3(class_input: str):
    clear_screen()

    while (True):
        print("TAKE ATTENDANCE")
        print("---------------")
        list_students(class_input)
        print("")
        input("[Press Enter key to continue...] ")
        break


def _option_menu(class_input: str):
    while (True):
        _display_menu(class_input)
        user_input = input("Option: ")

        if user_input == "1":
            break

        elif user_input == "2":
            _option2(class_input)

        elif user_input == "3":
            _option3(class_input)

        elif user_input == "4":
            clear_screen()
            print("Program finished.")
            exit()

        else:
            print("\nInvalid option!")
            print("")
            input("[Press Enter key to continue...] ")
            continue


def main():
    try:
        _main_menu()
    except KeyboardInterrupt:
        clear_screen()
        print("Program finished.")
        exit()


if __name__ == "__main__":
    main()
