# DeskGuardian

DeskGuardian is a posture alert system designed to detect when a user leans too close to their screen for extended periods. It provides alerts to assist mechanism in maintaining a healthy viewing distance, aiming to reduce digital eye strain and improve posture.

## Features

- **Face Distance Estimation**: Utilizes MediaPipe Face Detection to estimate the distance of the user based on the bounding box size of the face relative to the frame.
- **Privacy-Centric**: All video processing is performed locally on the device. No video data is recorded, saved, or transmitted to external servers.
- **Customizable Alerts**: Includes settings for sensitivity thresholds, time buffers before triggering alerts, and cooldown periods between alerts.
- **Posture History**: Visualizes a timeline of posture events to track behavior over time.

## Technology Stack

- **Python 3.11**
- **Streamlit**: Interactive web-based user interface.
- **OpenCV**: Image processing and video capture.
- **MediaPipe**: Efficient face detection.
- **Pygame**: Audio alert management.

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/abhi3114-glitch/DeskGaurdian.git
    cd DeskGaurdian
    ```

2.  **Set up a Virtual Environment (Recommended)**:
    It is highly recommended to use Python 3.11 for compatibility.
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the Application**:
    ```bash
    streamlit run app.py
    ```

2.  **Interface Controls**:
    - **Distance Sensitivity**: Adjust the threshold ratio. A higher value makes the system more sensitive, triggering alerts at a further distance.
    - **Time Buffer**: Set the duration the user must be "too close" before an alert is triggered.
    - **Start Camera**: Begins the webcam feed and monitoring process.

3.  **Permissions**:
    Ensure the application has permission to access the webcam.

## Troubleshooting

- **Installation Issues**: If you encounter errors regarding missing distributions (e.g., for MediaPipe), please ensure you are running Python 3.11.
- **Camera Access**: If the camera fails to initialize, verify that no other application (like Zoom or Teams) is currently using the webcam.
