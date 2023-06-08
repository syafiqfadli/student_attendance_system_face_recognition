import face_recognition
import pickle

from collections import Counter
from pathlib import Path
from PIL import Image, ImageDraw
from src.scripts.clear_helper import *
from src.scripts.extract_face import save_images


BOUNDING_BOX_COLOR = "blue"
TEXT_COLOR = "white"


def _draw_name_box(draw, bounding_box, name):
    top, right, bottom, left = bounding_box
    draw.rectangle(((left, top), (right, bottom)), outline=BOUNDING_BOX_COLOR)
    text_left, text_top, text_right, text_bottom = draw.textbbox(
        (left, top), name
    )
    draw.rectangle(
        ((text_left, text_top), (text_right, text_bottom)),
        fill="blue",
        outline="blue",
    )
    draw.text(
        (text_left, text_top),
        name,
        fill="white",
    )


def _get_students():
    extensions = ('*.jpg', '*.jpeg', '*.png')
    all_files = []

    for ext in extensions:
        all_files.extend(
            Path("src/students_in_class/students/detected").glob(ext))

    return all_files


def _recognize_face(unknown_encoding, loaded_encodings):
    boolean_matches = face_recognition.compare_faces(
        loaded_encodings["encodings"], unknown_encoding)

    votes = Counter(
        name
        for match, name in zip(boolean_matches, loaded_encodings["names"])
        if match
    )

    if votes:
        return votes.most_common(1)[0][0]


def _recognize_students_faces(
    image_location: str,
    model: str,
    index: int
):
    encodings_location = Path("src/encoder/students_encoding.pkl")

    with encodings_location.open(mode="rb") as f:
        loaded_encodings = pickle.load(f)

    input_image = face_recognition.load_image_file(image_location)

    input_face_locations = face_recognition.face_locations(
        input_image, model=model)

    input_face_encodings = face_recognition.face_encodings(
        input_image, input_face_locations)

    pillow_image = Image.fromarray(input_image)
    draw = ImageDraw.Draw(pillow_image)

    for bounding_box, unknown_encoding in zip(input_face_locations, input_face_encodings):
        name = _recognize_face(unknown_encoding, loaded_encodings)

        if not name:
            name = "Unknown_{} - TAKE ACTION".format(index)

        _draw_name_box(draw, bounding_box, name)
        pillow_image.save('src/students_in_class/students/named/' +
                          name + '_face.jpg')
        print("{0}. {1}".format(index, name))

    del draw


def list_students(model: str):
    save_images()

    counter = 0
    encoder_folder = "src/encoder"
    named_students_folder = "src/students_in_class/students/named/"
    students_in_class = _get_students()
    dir = os.listdir(encoder_folder)

    if len(dir) == 0:
        print("[INFO] No encoder file created yet.")
        return None

    if len(students_in_class) == 0:
        print("[INFO] No students recorded yet.")
        return None

    result = clear_folder(named_students_folder)

    if (result == -1):
        return None

    print("Student list present in class ({0} students):".format(
        len(students_in_class)))
    print("")

    for student_image in students_in_class:
        counter += 1
        _recognize_students_faces(student_image, model, counter)
