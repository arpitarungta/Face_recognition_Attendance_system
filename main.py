import cv2
import pickle
import numpy as np
import os

# Initialize video capture and face detector
video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces_data = []
i = 0
name = input("ENTER YOUR NAME: ").strip()

if not name:
    print("Name cannot be empty. Exiting.")
    exit()

while True:
    ret, frame = video.read()
    if not ret:
        print("Failed to access the camera.")
        break

    # Convert to grayscale for detection
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(grey, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        crop_img = frame[y:y + h, x:x + w]
        resized_img = cv2.resize(crop_img, (50, 50))

        # Save frames periodically
        if len(faces_data) < 100 and i % 10 == 0:
            faces_data.append(resized_img)

        i += 1

        # Display data on screen
        cv2.putText(frame, f"Captured: {len(faces_data)}/100", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (50, 50, 255), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 2)

    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q') or len(faces_data) == 100:
        break

video.release()
cv2.destroyAllWindows()

if len(faces_data) < 100:
    print("Insufficient data collected. Exiting.")
    exit()

# Reshape and save data
faces_data = np.asarray(faces_data)
faces_data = faces_data.reshape(faces_data.shape[0], -1)

# Ensure the data directory exists
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

names_file = os.path.join(data_dir, 'names.pkl')
faces_file = os.path.join(data_dir, 'faces_data.pkl')

# Save names
if os.path.exists(names_file):
    with open(names_file, 'rb') as f:
        names = pickle.load(f)
else:
    names = []

names.extend([name] * 100)
with open(names_file, 'wb') as f:
    pickle.dump(names, f)

# Save faces data
if os.path.exists(faces_file):
    with open(faces_file, 'rb') as f:
        faces = pickle.load(f)
    faces = np.vstack((faces, faces_data))
else:
    faces = faces_data

with open(faces_file, 'wb') as f:
    pickle.dump(faces, f)

print("Data saved successfully!")
