import cv2

# Trained data set
trainedDataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video = cv2.VideoCapture('video/yuva.mp4')

while True:
    success, frame = video.read()

    if success:
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert frame to grayscale
        faces = trainedDataset.detectMultiScale(gray_image)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (250, 0, 0), 3)
        cv2.imshow('video', frame)
        cv2.waitKey(1)
    else:
        print("Video complete or frame null")
        break

cv2.destroyAllWindows()  # Close all OpenCV windows
