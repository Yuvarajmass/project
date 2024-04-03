import cv2

# Trained data set
trainedDataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(0)

while True:
    success, frame = video.read()

    if success:
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert frame to grayscale
        faces = trainedDataset.detectMultiScale(gray_image)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (250, 0, 0), 3)
        cv2.imshow('video', frame)
        key = cv2.waitKey(1)
        if key == 81 or key == 113:  # Check for 'Q' or 'q' key press
            break
    else:
        print("Video complete or frame null")
        break

