import cv2

cascase_path = 'haarcascade_fullbody.xml'
classifier = cv2.CascadeClassifier(cascase_path)
path = r'C:\Users\abhis\Downloads\video2.mp4'      # 0 for webcam, path to video file.
video = cv2.VideoCapture(path)

while True:
    status, image= video.read()
    if not status:
        print('Could not read frame')
        break

    # Logic
    image = cv2.resize(image, (0,0), fx=0.4, fy=0.4)   
    detection = classifier.detectMultiScale(image, 
                                            scaleFactor=25,
                                            minNeighbors=10,
                                            minSize=(20,20))   

    if len(detection) > 0:
        print(f'Found {len(detection)} people')
        for (x, y, w, h) in detection:
            cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2) 
              
    # img_edge = cv2.Canny(image, 100, 200)           # --> for edge detection

    cv2.imshow('video', image)
    if cv2.waitKey(1) == ord('q'):    # if 'q' is pressed then break
        break
video.release()         #release video capture object
cv2.destroyAllWindows   #close all windows