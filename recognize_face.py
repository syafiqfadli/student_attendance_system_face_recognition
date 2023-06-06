import local_path
import face_recognition
import pickle

from collections import Counter
from pathlib import Path

DEFAULT_ENCODINGS_PATH = local_path.DEFAULT_ENCODINGS_PATH
STUDENTS_IMAGES_DB = local_path.STUDENTS_IMAGES_DB


def get_students():
    extensions = ('*.jpg', '*.jpeg', '*.png')
    all_files = []
    
    for ext in extensions:
        all_files.extend(Path("src/students_in_class/students").glob(ext))
        
    return all_files

def _recognize_face(unknown_encoding, loaded_encodings):
    boolean_matches = face_recognition.compare_faces(loaded_encodings["encodings"], unknown_encoding)
    
    votes = Counter(
        name
        for match, name in zip(boolean_matches, loaded_encodings["names"])
        if match
    )
    
    if votes:
        return votes.most_common(1)[0][0]
    
def recognize_faces(
    image_location: str,
    model: str = "cnn",
    encodings_location: Path = DEFAULT_ENCODINGS_PATH,
):    
    with encodings_location.open(mode="rb") as f:
        loaded_encodings = pickle.load(f)

    input_image = face_recognition.load_image_file(image_location)
    
    input_face_locations = face_recognition.face_locations(input_image, model=model)
    
    input_face_encodings = face_recognition.face_encodings(input_image, input_face_locations)
    
    
    for _, unknown_encoding in zip(input_face_locations, input_face_encodings):
        name = _recognize_face(unknown_encoding, loaded_encodings)
        
        if not name:
            name = "Unknown"
            
        print(name)

def main():
    students_in_class = get_students()
    
    print("Student list present in class ({0} students):".format(len(students_in_class)))
    
    for student_image in students_in_class:
        recognize_faces(student_image)
        
main()
