import cv2
import numpy as np
import csv
import face_recognition
from datetime import datetime

# Load known faces
anshus_image = face_recognition.load_image_file("faces/WhatsApp Image 2024-03-12 at 21.10.26_efa8962c.jpg")
anshus_encoding = face_recognition.face_encodings(anshus_image)[0]

rohan_image = face_recognition.load_image_file("faces/download.jpeg")
rohan_encoding = face_recognition.face_encodings(rohan_image)[0]

known_face_encoding = [anshus_encoding, rohan_encoding]
known_face_names = ["Batman", "Rohan"]

# List of expected students
student = known_face_names.copy()

# Get the current date and time
now = datetime.now()
current_date = now.strftime("%d-%m-%y")

f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

# Initialize VideoCapture outside the loop
video_capture = cv2.VideoCapture(0)  # 0 is for webcam number
video_capture.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # Set maximum buffer size

while True:
    # Read frame from video
    ret, frame = video_capture.read()

    # Skip frames to make video less laggy
    for i in range(5):
        video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        if name in known_face_names:
            font = cv2.FONT_ITALIC
            bottomleftcorner = (10,100)
            font_scale =1.5
            fontcolor=(0,0,0)
            thickness = 3
            linetype =2
            cv2.putText(frame,name+" Present",bottomleftcorner,font,font_scale,fontcolor,thickness,linetype)

        if name in student:
            student.remove(name)
            current_date = now.strftime("%H-%M-%S")
            lnwriter.writerow([name,current_date])
    cv2.imshow("Attendance ", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
