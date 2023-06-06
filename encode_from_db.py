import local_path
import face_recognition
import pickle

from pathlib import Path

DEFAULT_ENCODINGS_PATH = local_path.DEFAULT_ENCODINGS_PATH
STUDENTS_IMAGES_DB = local_path.STUDENTS_IMAGES_DB

def encode_registered_students(
    model: str = "hog", 
    encodings_location: Path = DEFAULT_ENCODINGS_PATH, 
    images_db: Path = STUDENTS_IMAGES_DB,
):
    names = []
    encodings = []
    
    print("In training...")
    
    for filepath in images_db:
        name = filepath.parent.name
        image = face_recognition.load_image_file(filepath)
        face_locations = face_recognition.face_locations(image, model=model)
        face_encodings = face_recognition.face_encodings(image, face_locations)
        
        for encoding in face_encodings:
            names.append(name)
            encodings.append(encoding)
            
    name_encodings = {"names": names, "encodings": encodings}
    
    with encodings_location.open(mode="wb") as f:
        pickle.dump(name_encodings, f)
        
    print("New encoded file created!")

encode_registered_students()