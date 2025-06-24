# 👁️‍🗨️ Face Recognition Attendance System

This project is a **Face Recognition-based Attendance System** that captures and verifies faces in real-time using a webcam and records attendance in structured Excel files. It bridges the gap between intelligent local detection and automated attendance logging. The system uses face encoding to identify individuals and stores the records securely and efficiently.

---

## 📂 Project Structure

FACE_RECOGNITION_ATTENDANCE/
├── attendance_folder/ # Stores generated attendance Excel sheets
├── data/ # Stores face encodings and labels
│ ├── faces_data.pkl
│ └── names.pkl
├── background.png # Background image for GUI (optional)
├── app.py # Streamlit or Flask app interface
├── main.py # Main script for running face detection and attendance
├── test.py # Test script for debugging or preview

---

## 🚀 Features

- 🎥 Real-time face detection using webcam
- 🧠 Face encoding and recognition using `face_recognition` library
- 📝 Auto-generates timestamped Excel attendance sheets
- 💾 Saves known faces and names using `pickle`
- 🌐 Simple GUI (Streamlit or Flask-based)

---

## 📦 Requirements

Install Python dependencies with:

```bash
pip install -r requirements.txt
If requirements.txt is missing, install manually:
pip install opencv-python face_recognition numpy pandas streamlit


🧠 How It Works
->Load Known Faces from data/ (stored via .pkl)
->Open Webcam and detect faces in real-time
->Match Faces with known encodings
->Log Attendance in an Excel sheet with name and time
->Save Record in attendance_folder/

## 📦 Requirements

Install the required Python packages using:

```bash
pip install -r requirements.txt

🖥️ How to Run
Run the system in either of these ways:

1. Main script (console-based):
python main.py

2. Web-based UI (if using Streamlit):
streamlit run app.py