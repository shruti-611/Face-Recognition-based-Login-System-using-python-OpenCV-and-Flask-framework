"""
$hruti Gujar
"""

import cv2, os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd


name , Id = '',''
dic = {
    'Name' : name,
    'Ids' : Id
}
def store_data():
    global name,Id,dic
    name = str(input("Enter Name  "))
   
    Id  = str(input("Enter Id   "))
   
    dic = {
        'Ids' : Id,
        'Name': name
    }
    c = dic
    return  c


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def TakeImages():
    dict1 = store_data()
    

    if (name.isalpha() and is_number(Id)):
   
        if Id == '1':
            fieldnames = ['Name','Ids']
            with open('Profile.csv','w') as f:
                writer = csv.DictWriter(f, fieldnames =fieldnames)
                writer.writeheader()
                writer.writerow(dict1)
        else:
            fieldnames = ['Name','Ids']
            with open('Profile.csv','a+') as f:
                writer = csv.DictWriter(f, fieldnames =fieldnames)
                #writer.writeheader()
                writer.writerow(dict1)
        cam = cv2.VideoCapture(0)

       
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                # Incrementing sample number
                sampleNum = sampleNum + 1
             
                cv2.imwrite("TrainingImage\ " + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
              
            cv2.imshow('Cpaturing Face for Login ', img)
        
           
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
          
            elif sampleNum > 60:
                break
            
        
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for Name : " + name + " with ID  " + Id
        print(res)
        print(' Images save location is TrainingImage\ ')
      
        
    else:
        if(name.isalpha()):
            print('Enter Proper Id')
        elif(is_number(Id)):
            print('Enter Proper name')
        else:
            print('Enter Proper Id and Name')
                    
        

TakeImages()

