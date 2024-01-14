# Advanced 🙂Face Recognition System for 🧑‍🎓Student Attendance

This project is an advanced face recognition system designed for managing student attendance in educational institutions. The system utilizes **Python 3.8.5** along with the **OpenCV library** for face detection and recognition. It offers a range of features for managing student data, capturing attendance through face recognition, and generating attendance reports.

## 💻 Requirements

- **Python 3.8.5**

## 🧐 Algorithms Used

- **Haarcascade OpenCV (Object Detection)**
- **LBPH OpenCV (Face Recognition)**

## ✈️ Features

- **Real-time Face Detection**: The system can detect faces in real-time using the Haarcascade OpenCV algorithm.
- **Face Recognition**: It uses LBPH OpenCV for recognizing individual faces based on trained samples.
- **Login Security System**: Includes a login system with username and password for secure access.
- **Student Management System**:
  - **Save**: Allows saving student information such as name, ID, and photo samples.
  - **Take Photo Samples**: Captures multiple photos of students for training the recognition model.
  - **Update**: Allows updating student information.
  - **Delete**: Removes a student from the system.
  - **Clear**: Clears all student data.
- **Train Photo Samples**: Trains the recognition model using the captured photo samples.
- **Take Attendance with Face Detection**: Marks attendance by detecting faces in a classroom setting.
- **Attendance Report**:
  - **Excel File**: Generates an Excel file containing attendance records.
  - **MySQL Database**: Stores attendance records in a MySQL database.
- **Developer Page**: Provides information about the developers and contributors.
- **Help Desk**: Offers assistance and support for using the system.
- **Exit System**: Allows users to securely log out of the system.

## 👌Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

## 💻 Usage
1. Navigate to the project directory:

    ```bash
    cd your-repository

2. Run the main application:

    ```bash
    python main.py

3. Access the application at http://localhost:5000 in your web browser.

## 📷 Demo
Here's a brief demonstration of the face recognition system in action:

<img align="center" src="FRAS Video.gif" alt="GIF Title" width="1000" height="500">

## ❤️ Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any problems or have suggestions for improvements.
