import face_recognition
import cv2
import os
import glob
import numpy 
import smtplib
import geocoder
from geopy.geocoders import Nominatim

mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.starttls()
mail.login('sendermail@gmail.com', 'xxxxxxxxxxxxxx')
SUBJECT='CRIMINAL DETECTION ALERT'
TEXT = 'Person matched in CCTV is '
loc= Nominatim(user_agent="GetLoc")
g = geocoder.ip('me')
locname = loc.reverse(g.latlng)
face_name=" "
temp_face_name=" "

class SimpleFacerec: 
    def __init__(self):
        self.encoded_face = []
        self.known_face = []
        self.frame_resizing = 0.25

    def load_encoding_images(self, images_path):
        images_path = glob.glob(os.path.join(images_path, "*.*"))
        print("{} encoding images found.".format(len(images_path)))
        
        for img_path in images_path:
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)
            # Get encoding
            img_encoding = face_recognition.face_encodings(rgb_img)[0]

            # Store file name and file encoding
            self.encoded_face.append(img_encoding)
            self.known_face.append(filename)
        print("Encoding images loaded")

    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            
            matches = face_recognition.compare_faces(self.encoded_face, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(self.encoded_face, face_encoding)
            best_match_index = numpy.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face[best_match_index]
            face_names.append(name)

        # Convert to numpy array to adjust coordinates with frame resizing quickly
        face_locations = numpy.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names

ob=SimpleFacerec()
ob.load_encoding_images("images/")
capture=cv2.VideoCapture(0)
while True:
    ret, frame=capture.read()

    face_location, face_name=ob.detect_known_faces(frame)
    for face_loc, name in zip(face_location, face_name):
        y1, x2, y2, x1= face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0),2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
        if face_name!=temp_face_name and face_name!=" ":
            temp="Person matched in CCTV is "+ ' '.join(face_name)
            print(temp)
            TEXT= TEXT + ' '.join(face_name)+ '\nLocation: ' + (locname.address)
            message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
            if ' '.join(face_name)!="Unknown":
                mail.sendmail('sendermail@gmail.com', 'receivermail@gmail.com', message)
            temp_face_name=face_name
    cv2.imshow("Frame",frame)
    cv2.waitKey(1)
