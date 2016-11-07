import numpy as np
import pickle
from sklearn import neighbors, datasets
import warnings
warnings.filterwarnings("ignore")

fileName ='C:/Users/Kalista13/Documents/HCI/Deliverable 5/userData/train2.dat'
f = open(fileName,'r')
train2 = pickle.load(f)
f.close()

fileName ='C:/Users/Kalista13/Documents/HCI/Deliverable 5/userData/train3.dat'
f = open(fileName,'r')
train3 = pickle.load(f)
f.close()

fileName ='C:/Users/Kalista13/Documents/HCI/Deliverable 5/userData/test2.dat'
f = open(fileName,'r')
test2 = pickle.load(f)
f.close()

fileName ='C:/Users/Kalista13/Documents/HCI/Deliverable 5/userData/test3.dat'
f = open(fileName,'r')
test3 = pickle.load(f)
f.close()

#print train2.shape
#
#print train2


def ReshapeData(set1,set2):
    #print len(set1)
    #print set1.shape
    #print set1.ndim
    X = np.zeros((2000,5*2*3),dtype='f')
    y = np.zeros(2000,dtype='f')
    for i in range(0,1000):
        n = 0
        for j in range(0,5):
            for k in range(0,2):
                for m in range (0,3):
                    print set1.shape
#                    print set1
                    #print sum(len(x) for x in set1)
#                    print set1[j,k,m,i]
#                    print sum(len(x) for x in set1)
                    X[i,n] = set1[j,k,m,i]
                    X[i+1000,n] = set2[j,k,m,i]
                    y[i] = 2
                    y[i+1000] = 3
                    n+=1
    return X,y

      
def ReduceData(X):
    X = np.delete(X,1,1)
    X = np.delete(X,1,1)
    X = np.delete(X,0,2)
    X = np.delete(X,0,2)
    X = np.delete(X,0,2)
    
    return X
    
def CenterData(X):
    allXCoordinates = X[0,::3]
    meanValue = allXCoordinates.mean()
    X[0,::3] = allXCoordinates - meanValue
    
    allYCoordinates = X[0,1::3]
    meanValue = allYCoordinates.mean()
    X[0,1::3] = allYCoordinates - meanValue
    
    allZCoordinates = X[0,2::3]
    meanValue = allZCoordinates.mean()
    X[0,2::3] = allZCoordinates - meanValue

    
    return(X)     
#print type(train2)  
train2 = ReduceData(train2)
train3 = ReduceData(train3)
test2 = ReduceData(test2)
test3 = ReduceData(test3)

train2 = CenterData(train2)
train3 = CenterData(train3)
test2 = CenterData(test2)
test3 = CenterData(test3)                   

                                                                            
trainX, trainy = ReshapeData(train2,train3)
testX, testy = ReshapeData(test2,test3)

print testX, testy

clf = neighbors.KNeighborsClassifier(15)
clf.fit(trainX,trainy)
clf.fit(testX,testy)


correct = 0
for i in range(0,2000):
    #for j in range(0,120):
    prediction = clf.predict(testX[i,:])
    #print int(prediction)
    if (prediction == testy[i]):
        correct+=1

print float(correct)/float(2000)


#print trainX
#print trainy
#print trainX.shape
#print trainy.shape
#
#print testX
#print testy
#print testX.shape
#print testy.shape