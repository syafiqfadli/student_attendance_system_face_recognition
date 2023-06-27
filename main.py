import time

from src.features.encode_from_db import encode_registered_students
from src.features.recognize_face import take_attendance
from src.features.take_picture import take_picture
from src.features.checker_helper import dataset_checker
from src.features.create_attendance import *
from src.features.clear_helper import *


def _clear_captures(class_name: str):
    class_folder = "src/captures/classes/{}".format(class_name)
    detected_students_folder = "src/captures/students/detected/{}".format(
        class_name)
    named_students_folder = "src/captures/students/named/{}".format(
        class_name)

    clear_folder(class_folder)
    clear_folder(detected_students_folder)
    clear_folder(named_students_folder)


def _start_system(class_name: str):
    time_interval = 10
    system_repeat = 0
    encoder_folder = "src/encoders/{}".format(class_name)
    dir = os.listdir(encoder_folder)

    clear_screen()

    if len(dir) == 0:
        encode_registered_students(class_name)

    time.sleep(2)

    clear_folder("src/attendance/{}".format(
        class_name))

    create_attendance_csv(class_name)

    while system_repeat < 5:
        clear_screen()
        _clear_captures(class_name)

        take_picture(class_name)
        clear_screen()

        students = take_attendance(class_name)
        check_attendance(class_name, students, system_repeat+1)

        time.sleep(time_interval)
        system_repeat += 1

    chart_loc = generate_chart(class_name)
    clear_screen()
    print("Attendance chart generated at", chart_loc)
    print("Program finished.")
    exit()


def _main_menu():
    while (True):
        clear_screen()

        print("MAIN MENU")
        print("---------")
        class_input = str(input("Enter class name: ")).upper()

        if (class_input == ""):
            continue

        dataset_result = dataset_checker(class_input)

        if (dataset_result == -1):
            print("")
            is_continue = str(input("Continue? [y/n]: ")).lower()

            if (is_continue == "y" or is_continue == ""):
                continue
            else:
                clear_screen()
                print("Program finished.")
                break

        _start_system(class_input)


def main():
    try:
        _main_menu()
    except KeyboardInterrupt:
        clear_screen()
        print("Program finished.")
        exit()


if __name__ == "__main__":
    main()
