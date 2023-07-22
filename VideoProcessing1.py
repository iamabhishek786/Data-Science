import cv2

path = r'C:\Users\abhis\Downloads\video1.mp4'      # 0 for webcam, path to video file.
video = cv2.VideoCapture(path)

while True:
    status, image= video.read()
    if not status:
        print('Could not read frame')
        break

    # Logic
    '''image = cv2.resize(image, (0,0), fx=0.4, fy=0.4)        
    img_edge = cv2.Canny(image, 100, 200)'''            #for edge detection

    image = cv2.resize(image, (0,0), fx=0.4, fy=0.4) 
    cv2.imshow('video', image)
    if cv2.waitKey(1)==ord('q'):    # if 'q' is pressed then break
        break
video.release()         #release video capture object
cv2.destroyAllWindows   #close all windows