import numpy as np
import pickle
from sklearn import neighbors, datasets
import warnings
import glob
import collections

warnings.filterwarnings("ignore")
path = 'C:/Users/Kalista13/Documents/HCI/Deliverable 6/userData/*.p'
fileTrain = 'train'
fileTest = 'test'
trainKeys = ['train0', 'train1', 'train2', 'train3','train4', 'train5', 'train6', 'train7', 'train8', 'train9']
testKeys = ['test0', 'test1', 'test2', 'test3','test4','test5', 'test6', 'test7','test8', 'test9']
trainDict= {key: [] for key in trainKeys}
testDict = {key: [] for key in testKeys}
#trainDict = {}
#testDict = {}
#  
trainCounter = [0]*10
testCounter = [0]*10

trainSignsArray = [0]*10
testSignsArray = [0]*10

for filename in glob.glob(path):    
    if (fileTrain in filename):
        currentKey = fileTrain + filename[-3] 
        trainIndex = int(filename[-3])                
        f = open(filename,'r')
        trainDict[currentKey].append(pickle.load(f))
        f.close
              
    elif (fileTest in filename):
        currentKey = fileTest + filename[-3] 
        testIndex = filename[-3]
        testCounter[int(testIndex)]+=1   
        f = open(filename,'r')
        testDict.setdefault(currentKey, []).append(pickle.load(f))
        f.close


for key, value in sorted(trainDict.items()):
    sign = int(key[-1])
    vals = np.array(value)
    signArray = np.concatenate((vals), axis=3)
    trainSignsArray[sign] = signArray
    #print key, signArray.shape 
    
for key, value in sorted(testDict.items()):
    sign = int(key[-1])
    vals = np.array(value)
    signArray = np.concatenate((vals), axis=3)
    testSignsArray[sign] = signArray
    #print key, signArray.shape 
    #print sign
#print signArray 
#print signArray[3].shape

def ReshapeData(signs,signSum):
    X = np.zeros((signSum,5*2*3),dtype='f')
    y = np.zeros(signSum,dtype='f')
    offset = 0
    #y = [0]*signSum
    #print signSum
    for s in range(0, len(signs)):
        sign = signs[s]
        currentSize = np.size(sign,3)
        #print 'offset: ' + str(offset) + ' for sign ' + str(s)
        for i in range(0,currentSize):
            n = 0
            for j in range(0,5):
                for k in range(0,2):
                    for m in range (0,3):
                        #print sign.shape    
                        X[i+offset,n] = sign[j,k,m,i]
                        y[i+offset] = s
                        #print s
                        n+=1
        offset+=currentSize    
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

for i in range (0,len(trainSignsArray)):
    trainSignsArray[i] = ReduceData(trainSignsArray[i])
    trainSignsArray[i] = CenterData(trainSignsArray[i])

for i in range (0,len(testSignsArray)):
    testSignsArray[i] = ReduceData(testSignsArray[i])
    testSignsArray[i] = CenterData(testSignsArray[i])   

trainSignSum = 0
for point in testSignsArray:
    trainSignSum += np.size(point,3)

testSignSum = 0
for point in testSignsArray:
    testSignSum += np.size(point,3)
    

trainX, trainy = ReshapeData(trainSignsArray, trainSignSum)                                        


testX, testy = ReshapeData(testSignsArray, testSignSum)


#print trainy #testX, testy
clf = neighbors.KNeighborsClassifier(15)
clf.fit(trainX,trainy)
clf.fit(testX,testy)


correct = 0
#print "Still running..."
for i in range(0,testSignSum):
    prediction = int(clf.predict(testX[i,:]))
    if (prediction == testy[i]):
        correct+=1
    #print '...'

print float(correct)/float(testSignSum)



pickle.dump(clf, open('C:/Users/Kalista13/Documents/HCI/Deliverable 6/userData/classifier.p','wb'))
