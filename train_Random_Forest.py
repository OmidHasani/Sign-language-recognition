import numpy as np
import pandas as pd
import glob

num = 0

from numpy import load
from sklearn.model_selection import train_test_split

import pickle
 

from sklearn import preprocessing


import pickle

print("Start Train....")
label = []
data = []
for ithem in glob.glob("C://Users//Win10//Desktop//code_fasele_mohem - Copy (2)//data_ two_hand//*//*"):
    num+=1
    print(ithem)
    arr = load(ithem)
    print(arr.shape)
  
    
    data.append(arr)
    l = ithem.split("\\")[1]
    print(l)
    label.append(l)

#========================================================
print(data)
data = np.array(data)

print(data.shape,"data_shape")
label = np.array(label)
print(label)
print(label.shape)
print(data)

from sklearn.ensemble import RandomForestClassifier
X_train, X_test, y_train, y_test = train_test_split(data,label, test_size=0.3)
print(X_train.shape,"x_train")
X_train = np.reshape(X_train,(20,29*1764))
print(X_test.shape,"x_test")
X_test= np.reshape(X_test,(X_test.shape[0],29*1764))


rf =RandomForestClassifier(n_estimators=1000,random_state=42)


rf.fit(X_train,y_train)

a = rf.score(X_test, y_test)
b = rf.score(X_train, y_train)
print("train:",b)
print("test:",a)



filename = 'good_two_hand.sav'
pickle.dump(rf, open(filename, 'wb'))

print(label)
