import face_recognition
import pickle
import os

from pathlib import Path
from src.features.clear_helper import *

FACE_MODEL = "hog"


def _files_counter(class_name: str):
    students_dataset = Path("src/datasets/{}".format(class_name))
    files = 0

    for _, _, filespath in os.walk(students_dataset):
        files += len(filespath)

    return files


def _show_loading(counter: int, files: int):
    loading = 0

    loading = ((counter / files) * 100)

    print("[INFO] In training session")
    print("[----] -------------------")
    print("[INFO] Loading...({}%)".format(round(loading, 2)))


def encode_registered_students(class_name: str):
    students_dataset = Path("src/datasets/{}".format(class_name))
    encoding_file = Path(
        "src/encoders/{}/students_encoding.pkl".format(class_name))
    students_ds = students_dataset.glob("*/*")
    encoder_folder = "src/encoders/{}".format(class_name)
    names = []
    encodings = []
    counter = 0
    files = _files_counter(class_name)

    result = clear_folder(encoder_folder)

    if (result == -1):
        return None

    for file_path in students_ds:
        counter += 1

        _show_loading(counter, files)

        name = file_path.parent.name
        image = face_recognition.load_image_file(file_path)
        face_locations = face_recognition.face_locations(
            image, model=FACE_MODEL)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        for encoding in face_encodings:
            names.append(name)
            encodings.append(encoding)

        clear_screen()

    encoder = {
        "names": names,
        "encodings": encodings
    }

    with encoding_file.open(mode="wb") as f:
        pickle.dump(encoder, f)

    print("[INFO] Training done!")
