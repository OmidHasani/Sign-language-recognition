from cvzone.HandTrackingModule import HandDetector
import cv2
import pandas as pd
import numpy as np
import math
import cv2
import time

import math
hand2= []
hand1 = []
filename = "good1.sav"
filename1 = "good_two_hand.sav"
import pickle
ers = " "
loaded_model = pickle.load(open(filename, 'rb'))
loaded_modelk = pickle.load(open(filename1, 'rb'))

datatwo = []


gbg = 0
num = 0#NUMBERS OF FRAME


data1 = [] #LIST OF 60 FRAME POINTS





cap = cv2.VideoCapture(1)
detector = HandDetector(detectionCon=0.8, maxHands=2)
detector1 = HandDetector(detectionCon=0.8, maxHands=2)
v = 20


while True:
    
    # Get image frame
    success, img = cap.read()
    img = cv2.flip(img,1)
    success, img1 = cap.read()
    img1 = cv2.flip(img1,1)
   
    
    
    # Find the hand and its landmarks
    hands,img = detector.findHands(img)  # with draw
    # hands = detector.findHands(img, draw=False)  # without draw     
    if len(hands)==0:
        num=0
        data1.clear()
        gbg=0
        datatwo.clear()
           
   
    if len(hands)==2:
        data1.clear()
        num = 0
       # data1.clear()
        nd = []
        
        
        data=[]# handland mark
       
    
        cv2.circle(img,(50,50),50,(0,0,255),-1) # draw circle red if hands up>>>
        


        
        gbg+=1 #time
        #___________________
        cv2.putText(img,"time:{}".format(gbg),(80,100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1)
        
       
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

        datatwo.append(nd)
     
            



        if gbg ==29:
         
            ggg = np.array(datatwo)
           
            g = np.reshape(ggg,(1,-1))
            ers = loaded_modelk.predict(g)
            print(ers[0])
            datatwo.clear()
            
        

            cv2.circle(img,(50,50),50,(255,0,0),-1)#  draw circle blue if hand
            gbg=0
            time.sleep(1)

        if gbg==30:
        
            cv2.circle(img,(50,50),50,(255,0,0),-1)#  draw circle blue if hand
            time.sleep(1) # stop for 2 seconds and
   
            
    if len(hands)==1:
        data =[]# handland mark
        nd=[]
        gbg=0
        datatwo.clear()
           
    
        cv2.circle(img,(50,50),50,(0,0,255),-1) # draw circle red if hands up>>>
        

        
        
    
        
    
        hands = hands[0]
      

        x= hands["bbox"][0]-v
        y= hands["bbox"][1]-v
        w = (hands["center"][0]-hands["bbox"][0])+hands["center"][0]+v
        h = (hands["center"][1]-hands["bbox"][1])+hands["center"][1]+v
        img1= cv2.rectangle(img1,(x,y), (w,h), (0,0,255), 2)
        imgh = img1[y:h, x:w]

        if imgh.shape[0] and imgh.shape[1]>0:
            imgh = cv2.resize(imgh,(200,200))
            cv2.imwrite("imgh0.png",imgh)
            hand1,imgh = detector1.findHands(imgh) 
            cv2.imshow("png",imgh)
            cv2.imwrite("imgh1.png",imgh)
            data =[]# handland mark
            

    
            
          

        
        
          
      
            if len(hand1)>0:
                cv2.putText(img,"{}".format(ers[0]),(100,200),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1)
                cv2.putText(img,"time:{}".format(num),(80,100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1)

                
                cv2.imshow("img",img)
                cv2.waitKey(1)
                cv2.circle(img,(50,50),50,(0,0,255),-1) # draw circle red if hands up>>>
                
               
              
                cv2.waitKey(1)
                hand2 = hand1[0]
                num+=1 #t
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
                
                    


            
                for m in data:
                    for d in data:
                        rr = math.dist(m, d)
                        nd.append(int(rr))
           
                data1.append(nd)
       

            
                
                start = time.time()
                
                
            #________Display image____
        if num ==29:
                cv2.circle(img,(50,50),50,(255,0,0),-1)#  draw circle blue if hand
               
                g = np.array(data1)
                #print(g.shape)
           
                if(g.shape==(29,441)):
                    g = np.reshape(g,(1,-1))
                    ers = loaded_model.predict(g)
                    print(ers[0])
           
                data1.clear()
            

        if num==30:
            
            cv2.circle(img,(50,50),50,(255,0,0),-1)#  draw circle blue if hand
            time.sleep(1) # stop for 1 seconds and
    
            end = time.time()
                    
                
                
                

                
                
            num=0
            data1.clear()
        
                #_______________________
        
    cv2.putText(img,"{}".format(ers[0]),(100,200),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1)    
    if len(hand1)<1:

        
        cv2.imshow("img",img1)
        if cv2.waitKey(1)==ord("q"):
            break
    if len(hands)==2 or len(hands)==0 :
        cv2.imshow("img",img)
        if cv2.waitKey(1)==ord("q"):
            break




cap.release()
cv2.destroyAllWindows()




