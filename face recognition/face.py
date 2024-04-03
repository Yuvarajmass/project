import cv2

# Trained data set
trainedDataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read an image
img = cv2.imread('image/yuvaraj.jpg')
#convert into grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=trainedDataset.detectMultiScale(gray)
print(faces)
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(250,0,0),3)
cv2.imshow('yuvaraj', img)
#cv2.imshow('Gray', gray)


# Wait for a key press (use lowercase 'w' in waitKey)
cv2.waitKey(0)

