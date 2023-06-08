import cv2
import os
import shutil
import random

from src.scripts.clear_helper import *


def _extract_students_faces():
    image_path = "src/students_in_class/class/real_2018.jpg"
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=4,
    )

    print("[INFO] Found {0} faces!".format(len(faces)))

    for (x, y, w, h) in faces:
        random_num = random.randint(0, 10000)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cropped_image = image[y:y + h, x:x + w]
        cv2.imwrite('src/students_in_class/students/detected/' +
                    str(random_num) + '_face.jpg', cropped_image)

    print("[INFO] {0} images saved locally.".format(len(faces)))
    print("")


def save_images():
    detected_students_folder = "src/students_in_class/students/detected/"

    result = clear_folder(detected_students_folder)

    if (result == -1):
        return None

    _extract_students_faces()
