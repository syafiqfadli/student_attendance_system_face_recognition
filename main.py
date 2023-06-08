from src.scripts.encode_from_db import encode_registered_students
from src.scripts.recognize_face import list_students
from src.scripts.clear_helper import *

detected_students_folder = "src/students_in_class/students/detected/"
named_students_folder = "src/students_in_class/students/named/"
model_input = ""


def _display_menu():
    clear_screen()

    print("Current Model [{}]".format(model_input.upper()))
    print("---------------------")
    print("Choose One(1) option:")
    print("")
    print("1. Encode pkl file from DB")
    print("2. Take Attendance")
    print("3. Change Model")
    print("4. Exit")
    print("")
    print("---------------------")


def _option1():
    clear_screen()

    while (True):
        print("ENCODE FROM DB")
        print("--------------")
        encode_registered_students(model_input)
        print("")
        input("[Press Enter key to continue...] ")
        break


def _option2():
    clear_screen()

    while (True):
        print("TAKE ATTENDANCE")
        print("---------------")
        list_students(model_input)
        print("")
        input("[Press Enter key to continue...] ")
        break


def _option4():
    clear_screen()
    exit()


def _option_menu():
    while (True):
        _display_menu()
        user_input = input("Option: ")

        if user_input == "1":
            _option1()

        elif user_input == "2":
            _option2()

        elif user_input == "3":
            break

        elif user_input == "4":
            _option4()

        else:
            print("\nInvalid option!")
            print("")
            input("[Press Enter key to continue...] ")
            continue


while (True):
    clear_screen()

    result_detected = clear_folder(detected_students_folder)
    result_named = clear_folder(named_students_folder)

    if (result_detected == -1 or result_named == -1):
        break

    print("MODEL SELECT")
    print("------------")
    model_input = str(input("Enter model (hog/cnn): ")).lower()

    if (model_input != "hog" and model_input != "cnn"):
        print("")
        print("Invalid model!")
        print("")
        input("[Press Enter key to continue...] ")
        clear_screen()
    else:
        clear_screen()
        _option_menu()
