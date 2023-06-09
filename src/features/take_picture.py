import cv2
import keyboard


def take_picture(class_name: str):
    windows_title = "Student Attendance System"
    cam = cv2.VideoCapture(0)

    result, image = cam.read()

    if result:
        print("[INFO] Taking picture...")

        cv2.imshow(windows_title, image)

        if keyboard.read_key() == "p":
            cv2.imwrite(
                "src/captures/classes/{}/{}.jpg".format(class_name), image)
            cv2.destroyWindow(windows_title)

    else:
        print("[INFO] No image detected. Please! try again")
