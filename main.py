import numpy as np
import face_recognition
import cv2
import os
from googleapiclient.discovery import build
from datetime import datetime
from datetime import datetime
from google.oauth2 import service_account
from gsheet import timetable
from datetime import datetime

from gsheet import  timetable , monday, tuesday, wednesday, friday,thursday

path = 'KnownFaces'
images = []
classNames = []
myList = os.listdir(path)
#print(myList)

for cls in myList:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])
#print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncodings(images)
#print("Finding end ")

cap = cv2.VideoCapture(0)
caunt = 0
while (caunt <= 10):
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        caunt =caunt  + 1
        facesCurFrame = face_recognition.face_locations(imgS)
        encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
           # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex]
               # print(name)

                #img = cv2.flip(img, 1)
                y1, x2, y2, x1 = faceLoc

               # img = cv2.flip(img, 1)
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                #img = cv2.flip(img, 1)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                # img = cv2.flip(img , 1)
                if caunt ==10 :
                 match name :
                        case "Temurmalik":
                          match datetime.today().isoweekday():
                             case 1:
                               print(" | ".join([x[0] for x in monday()]))
                             case 2 :
                                 print(" | ".join([x[0]for x in tuesday()]))
                             case 3:
                                 print(" | ".join([x[0] for x in wednesday()]))
                             case 4 :
                                 print(" | ".join([x[0] for x in thursday()]))
                             case 5:
                                 print(" | ".join([x[0] for x in friday()]))
                             case 6:
                                 print("Today is day off!!")
                             case 7:
                                 print("Today is day off!!!")
                        case "Nuriddinxo'ja":
                            match datetime.today().isoweekday():
                                case 4:
                                 print(" | ".join([x[0] for x in monday()]))


a = cv2.imshow("Face recognition by Tmk", img)

      #  cv2.waitKey(1)

#print("If you wont to see an other day ps enter the day name  ")
option = input("If you wont to see an other day ps enter the day name:   " )
match option.upper():
    case "MONDAY":
      print(" | ".join([x[0] for x in monday()]))
    case "TUESDAY":
      print(" | ".join([x[0] for x in tuesday()]))
    case "WEDNESDAY":
      print(" | ".join([x[0] for x in wednesday()]))
    case "THURSDAY":
      print(" | ".join([x[0] for x in thursday()]))
    case "FRIDAY":
      print(" | ".join([x[0] for x in friday()]))

      