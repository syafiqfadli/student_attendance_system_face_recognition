import cv2
import os
import shutil
import random

folderPath = "src/students_in_class/students"

def extract_face():
    imagePath = "src/students_in_class/class/real_2018.jpg"
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=4,
    )

    print("[INFO] Found {0} faces!".format(len(faces)))
    
    for (x, y, w, h) in faces:
        randomNum = random.randint(0, 10000)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cropped_image = image[y:y + h, x:x + w] 
        cv2.imwrite('src/students_in_class/students/' + str(randomNum) + '_face.jpg', cropped_image) 
        
    print("[INFO] {0} images saved locally.".format(len(faces))) 
    
    status = cv2.imwrite('src/students_in_class/class/detected_class.jpg', image)
    
    print("[INFO] Image detected_class.jpg written to filesystem: ", status)

def main():
    for filename in os.listdir(folderPath):
        file_path = os.path.join(folderPath, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    extract_face()
    
main()