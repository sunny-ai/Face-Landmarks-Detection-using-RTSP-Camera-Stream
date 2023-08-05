# Face Landmarks Detection using RTSP Camera Stream

This is a Python script that uses the `dlib` library and OpenCV to detect face landmarks from a live camera stream provided by an RTSP URL. The detected landmarks are then visualized on the video feed.

## Prerequisites

Before running the script, make sure you have the following libraries installed:

- `imutils`
- `dlib`
- `opencv-python`

You can install these libraries using `pip`:

```bash
pip install imutils dlib opencv-python

```

## Instructions

1) Download the shape_predictor_68_face_landmarks.dat file and place it in the same directory as this script. This file is a pre-trained model for detecting facial landmarks using the dlib library.

2) Replace the following variables in the script with appropriate values:

     - rtsp_url: Replace this with the RTSP stream URL of your camera. It should look like `rtsp://username:password@ip_address:port/Streaming/Channels/channel_number`. Make sure to replace username, password, ip_address, port, and channel_number with your camera's credentials.

     - output_file: The filename for the output video file that will contain the annotated video with facial landmarks.

     - fps: Frames per second for the output video file.

     - width and height: The dimensions (width and height) for the output video file.
        
3) Run the script:

```bash
python main.py
```
The script will start capturing frames from the RTSP camera stream, detect facial landmarks in each frame, annotate the landmarks on the video feed, and display the annotated video in real-time.


# Note
   - Make sure the shape_predictor_68_face_landmarks.dat file and this script are in the same directory.
   - The script will run until you press the 'q' key. Press 'q' in the video window to stop the script and close the video window.
   - For better results, ensure that the camera has a clear view of the faces and is able to capture them with good lighting conditions.
   - If you encounter any issues, please check if the required libraries are installed and the `shape_predictor_68_face_landmarks.dat` file is present in the correct directory.

