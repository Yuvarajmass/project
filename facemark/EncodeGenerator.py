import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-c3cc2-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendancerealtime-c3cc2.appspot.com"
})


#importing the student image
folderpath = 'images'
pathList = os.listdir(folderpath)
print(pathList)
imgList = []
studentIds =[]
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderpath,path)))
    studentIds.append(os.path.splitext(path)[0])


    fileName = f'{folderpath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
 #   print(path)
  #  print(os.path.splitext(path)[0])
print(studentIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

        return encodeList

print("encoding started..." )
encodeListknown = findEncodings(imgList)
encodeListknownWithIds =[encodeListknown,studentIds]
print("encoding complete")

file = open("EncodeFile.p",'wb')
pickle.dump(encodeListknownWithIds,file)
file.close()
print("file saved")

