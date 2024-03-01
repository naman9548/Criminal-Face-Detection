Facial Recognition and Criminal Detection System

Overview:
This project implements a simple facial recognition system using the face_recognition library in Python. The system detects faces in live video streams, matches them against a database of known faces, and alerts authorities via email if a recognized face is identified, thus serving as a basic criminal detection system.

Components:


Dependencies:


face_recognition: A Python library for facial recognition.
cv2: OpenCV library for image and video processing.
numpy: Library for numerical computing.
smtplib: Library for sending emails.
geocoder: Library for retrieving geolocation information.
geopy: Library for geocoding and reverse geocoding.

Functionality:


Facial Encoding:

The system first loads encoding images of known faces from a specified directory using the load_encoding_images method.
Each face image is encoded into a numerical representation using face_recognition.face_encodings.

Face Detection:

The system captures video frames from a webcam using OpenCV.
It detects faces in each frame using face_recognition.face_locations.
For each detected face, it computes its encoding and compares it with the known face encodings to identify matches.

Alerting Authorities:

If a recognized face is detected, an email alert is generated and sent to specified authorities using the smtplib library.
The alert contains information about the matched person and their location obtained via reverse geocoding.

Usage:


Ensure all dependencies are installed (pip install -r requirements.txt).
Place encoding images of known faces in the images/ directory.
Run the script (python main.py).
Detected faces will be displayed on the video stream with corresponding names if recognized.
Email alerts will be sent if recognized faces are detected.

Project Structure:


main.py: Main script implementing the facial recognition system.
images/: Directory containing encoding images of known faces.
README.md: Documentation providing an overview of the project, usage instructions, and setup details.
Setup:

Installation:


Clone the repository: git clone <repository_url>
Install dependencies: pip install -r requirements.txt

Configuration:


Add encoding images of known faces to the images/ directory.
Update email credentials and recipient addresses in the main.py script.

Execution:


Run the script: python main.py

Note:

Ensure that proper permissions and access are granted for email sending (e.g., enabling less secure app access for Gmail).
Use the system responsibly and comply with legal and ethical considerations regarding privacy and surveillance.


Author: Naman Deol

Contributions: Contributions are welcome! Please submit issues or pull requests for any enhancements or bug fixes.

Contact: https://www.linkedin.com/in/naman-deol-b1a581232/
