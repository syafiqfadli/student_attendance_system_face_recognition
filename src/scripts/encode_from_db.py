import face_recognition
import pickle
import os

from pathlib import Path
from src.scripts.clear_helper import *


STUDENTS_IMAGES_DB = Path("src/images_db")


def _files_counter():
    files = 0
    for _, _, filespath in os.walk(STUDENTS_IMAGES_DB):
        files += len(filespath)

    return files


def _show_loading(counter: int, files: int, model: str):
    loading = 0

    loading = ((counter / files) * 100)

    print("[INFO] In training using {}".format(model.upper()))
    print("[INFO] ---------------------")
    print("[INFO] Loading...({}%)".format(round(loading, 2)))


def encode_registered_students(model: str):
    images_db = STUDENTS_IMAGES_DB.glob("*/*")
    encodings_location = Path("src/encoder/students_encoding.pkl")
    encoder_folder = "src/encoder/"
    names = []
    encodings = []
    counter = 0
    files = _files_counter()

    result = clear_folder(encoder_folder)

    if (result == -1):
        return None

    for file_path in images_db:
        counter += 1

        _show_loading(counter, files, model)

        name = file_path.parent.name
        image = face_recognition.load_image_file(file_path)
        face_locations = face_recognition.face_locations(image, model=model)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        for encoding in face_encodings:
            names.append(name)
            encodings.append(encoding)

        clear_screen()

    encoder = {
        "names": names,
        "encodings": encodings
    }

    with encodings_location.open(mode="wb") as f:
        pickle.dump(encoder, f)

    print("[INFO] Training done! {} used.".format(model.upper()))
