import cv2

# Load the image into imgStudent
imgStudent = cv2.imread('images/yuvaraj.jpg')

# Check if imgStudent is loaded successfully
if imgStudent is None:
    print("Error: Failed to load image")
else:
    print("Dimensions of imgStudent:", imgStudent.shape)
