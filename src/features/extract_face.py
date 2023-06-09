import cv2
import os
import random

from src.features.clear_helper import *


def _extract_students_faces(class_name: str):
    folder_path = "src/captures/classes/{}/".format(class_name)
    folder_list = os.listdir(folder_path)

    if len(folder_list) == 0:
        print("[INFO] No class image taken yet. Take class picture first.")
        return None

    image_path = folder_path + folder_list[0]

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=4,
    )

    for (x, y, w, h) in faces:
        random_num = random.randint(0, 10000)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cropped_image = image[y:y + h, x:x + w]
        cv2.imwrite('src/captures/students/detected/{}/'.format(class_name) +
                    str(random_num) + '_face.jpg', cropped_image)

    cv2.imwrite(
        "src/captures/classes/{}/_detected_class.jpg".format(class_name), image)


def save_extracted_images(class_name: str):
    detected_students_folder = "src/captures/students/detected/{}".format(
        class_name)

    result = clear_folder(detected_students_folder)

    if (result == -1):
        return None

    _extract_students_faces(class_name)
