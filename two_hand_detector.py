
from cvzone.HandTrackingModule import HandDetector
import cv2
import pandas as pd
import numpy as np
import math
import cv2
import time
from numpy import save
import pickle
filename = "good_two_hand.sav"
data1 = [] 
loaded_model = pickle.load(open(filename, 'rb'))
ers = ""








gbg = 0#n umber of 2hands frame

data1 = [] #LIST OF *


cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)



while True:
    
    # Get image frame
    success, img = cap.read()
    img = cv2.flip(img,1)
    
    
    
    hands,img = detector.findHands(img) 
    if len(hands)==2:
        nd = []
        
        
        data=[]# handland mark
       
    
        cv2.circle(img,(50,50),50,(0,0,255),-1) # draw circle red if hands up>>>
        


        
        gbg+=1 #time
        #___________________
        cv2.putText(img,"time:{}".format(gbg),(30,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1)
        
      
        hand2 = hands[1]
        #============================================== 
        # make list of data_hands point

        
        lmList1=hand2["lmList"]
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
        
        #=================================================

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
       
        for m in data:
            for d in data:
                rr = math.dist(m, d)
                nd.append(int(rr))
                
#############################################
        print(len(nd))
        data1.append(nd)
            



        if gbg ==29:
            print("nd:",nd)
            ggg = np.array(data1)
            print(ggg.shape)
          
            g = np.reshape(ggg,(1,-1))
            ers = loaded_model.predict(g)
            print(ers)
            data1.clear()
            tedad+=1
        

            cv2.circle(img,(50,50),50,(255,0,0),-1)#  draw circle blue if hand
            gbg=0
            time.sleep(1)
        if gbg==30:
        
            cv2.circle(img,(50,50),50,(255,0,0),-1)#  draw circle blue if hand
            time.sleep(1) # stop for 1 seconds and
   

          
           
    

        
  
        

    
    cv2.putText(img,"{}".format(ers),(100,200),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1)
    cv2.imshow("img",img)
    if cv2.waitKey(1)==ord("q"):
        break


#33333333333sound(f)


cap.release()
cv2.destroyAllWindows()




