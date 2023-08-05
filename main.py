from imutils import face_utils
import dlib
import cv2

p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)


fourcc = cv2.VideoWriter_fourcc(*'H264')
output_file = "output.h264"
fps = 30  
width, height = 640, 480 
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Replace the RTSP URL with your camera's RTSP stream URL
rtsp_url = "rtsp://robot:robot1234@192.168.10.188:554/Streaming/Channels/501"
cap = cv2.VideoCapture(rtsp_url)
 
while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Unable to read frame from the RTSP stream. Exiting.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)
    
    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        for (x, y) in shape:
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
    
    out.write(frame)
    cv2.imshow("Output", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
