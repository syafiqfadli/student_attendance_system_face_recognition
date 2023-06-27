import cv2 as cv
import time


def take_picture(class_name: str):
    windows_title = "Student Attendance System"
    frame_width = 640
    frame_height = 480
    device = 0

    cam = cv.VideoCapture(device)
    cam.set(3, frame_width)
    cam.set(4, frame_height)
    cam.set(10, 150)

    if not cam.isOpened():
        print("[INFO] Camera Error")
        return None

    print("[INFO] Taking picture...")

    while True:
        result, image = cam.read()

        if not result:
            print("[INFO] No camera found.")
            break

        cv.imshow(windows_title, image)

        # time.sleep(10)

        # cv.imwrite(
        #     "src/captures/classes/{0}/{1}.jpg".format(class_name, class_name), image)

        # print("[INFO] Picture captured.")
        # break
        key = cv.waitKey(1)

        if key % 256 == 32:  # Spacebar
            cv.imwrite(
                "src/captures/classes/{0}/{1}.jpg".format(class_name, class_name), image)

            print("[INFO] Picture captured.")
            break

    cam.release()
    cv.destroyAllWindows()
    cv.waitKey(1)
