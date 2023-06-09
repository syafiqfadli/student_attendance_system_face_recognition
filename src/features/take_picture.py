import cv2


def take_picture(class_name: str):
    windows_title = "Student Attendance System"
    frameWidth = 640
    frameHeight = 480

    cam = cv2.VideoCapture(0)
    cam.set(3, frameWidth)
    cam.set(4, frameHeight)
    cam.set(10, 150)

    if not cam.isOpened():
        print("[INFO] Camera Error")
        return None
    
    print("[INFO] Taking picture...")
    
    while True:
        _, image = cam.read()
        
        cv2.imshow(windows_title, image)

        key = cv2.waitKey(1)

        if key % 256 == 32:  # Spacebar
            cv2.imwrite(
                "src/captures/classes/{0}/{1}.jpg".format(class_name, class_name), image)

            print("[INFO] Picture captured.")
            break
    
    cam.release()
    cv2.destroyAllWindows()

