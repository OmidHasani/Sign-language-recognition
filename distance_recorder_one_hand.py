from cvzone.HandTrackingModule import HandDetector
import cv2
import pandas as pd
import numpy as np
import math
import cv2
import time
from numpy import save
import math

f = "0"

data_number = 0
data_number = int(data_number)

num = 0#NUMBERS OF FRAME
mo = 0#NUMBERS FOR VECTOR DISTANS
fasele = []#LIST OF DISTANCE
data1 = [] #LIST OF 60 FRAME POINTS
ng = ""
ex = 0 #for saving

import numpy as np
import numpy as np
def darsad(ha,point):
    ha = np.array(ha)
    if point<110:
        t = (110-point)
        ha=ha+t
        ha = list(ha)
        point = point+t
       
    if point>110:
        t= (point-110)

        ha=ha-t
        ha = list(ha)
        point = point-t
        
    if point==110:
        return ha,point
 

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)



while True:
    
    # Get image frame
    success, img = cap.read()
    img = cv2.flip(img,1)
    nd=[]
    nd1 =[] 
    
    
    # Find the hand and its landmarks
    hands,img = detector.findHands(img)  # with draw
    # hands = detector.findHands(img, draw=False)  # without draw        
    if len(hands)==1:
        data =[]# handland mark

    
        cv2.circle(img,(50,50),50,(0,0,255),-1) # draw circle red if hands up>>>
        

        
        
        num+=1 #time
        #___________________
        cv2.putText(img,"time:{}".format(num),(30,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1)
        
        ##_________display____________
    
        hand1 = hands[0]
        #============================================== 
        # make list of data_hands point

        
        lmList1=hand1["lmList"]
        data.append(lmList1[0][0:2])
        data.append(lmList1[1][0:2])
        data.append(lmList1[2][0:2])
        data.append(lmList1[3][0:2])
        data.append(lmList1[4][0:2])
        data.append(lmList1[5][0:2])
        data.append(lmList1[6][0:2])
        data.append(lmList1[7][0:2])
        data.append(lmList1[8][0:2])
        data.append(lmList1[9][0:2])
        data.append(lmList1[10][0:2])
        data.append(lmList1[11][0:2])
        data.append(lmList1[12][0:2])
        data.append(lmList1[13][0:2])
        data.append(lmList1[14][0:2])
        data.append(lmList1[15][0:2])
        data.append(lmList1[16][0:2])
        data.append(lmList1[17][0:2])
        data.append(lmList1[18][0:2])
        data.append(lmList1[19][0:2])
        data.append(lmList1[20][0:2])
        print(hand1["bbox"])
        x = hand1["bbox"][0]
        y = hand1["bbox"][1]
       
      
        cv2.circle(img,(hand1["center"][0],hand1["center"][1]),5,(255,0,0),-1)
        cv2.circle(img,(x,y),5,(255,0,0),-1)
        

        #=================================================
        
             


################################################حساب کردن فاصله بردار ها باخودشان 
       
        for m in data:
            for d in data:
                
                rr = int(math.dist(m, d))
                nd.append(rr)
                
                
                
               

        
        f = int(math.dist((x,y), (hand1["center"][0],hand1["center"][1])))        
        ng ,fg = darsad(nd, f)       
        print("++++++++++++++++++==============")
     
 
        
        

        
        data1.append(nd)
        
        
#############################################

      
        
        start = time.time()
        
        
    #________Display image____
    if num ==29:
            cv2.circle(img,(50,50),50,(255,0,0),-1)#  draw circle blue if hand
            mo = 0
            g = np.array(data1)
            save("{}.npy".format(data_number),g)
            data_number+=1
            print(g.shape)
            data1.clear()
            print("data len:",len(data1))

    if num==30:
        
        cv2.circle(img,(50,50),50,(255,0,0),-1)#  draw circle blue if hand
        time.sleep(1) # stop for 2 seconds and
   
        end = time.time()
        
       
       
       

       
        print(len(data1),"len")
        num=0
        data1.clear()
    
    #_______________________
      
 

    cv2.putText(img,"{}".format(f),(100,200),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1)
    cv2.imshow("img",img)
    if cv2.waitKey(1)==ord("q"):
        break


#33333333333sound(f)


cap.release()
cv2.destroyAllWindows()




