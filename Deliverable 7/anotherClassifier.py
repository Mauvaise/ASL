import numpy as np
import pickle
from sklearn import neighbors, datasets
import warnings
import glob

warnings.filterwarnings("ignore")


################ Train Data ###################
fileName ='C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/tryData/Glade_train0.p'
f = open(fileName,'r')
train0 = pickle.load(f)
f.close()

fileName ='C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/tryData/Glade_train1.p'
f = open(fileName,'r')
train1 = pickle.load(f)
f.close()

fileName ='C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/tryData/Gottfried_train2.p'
f = open(fileName,'r')
train2 = pickle.load(f)
f.close()

fileName ='C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/tryData/Pakulski_train3.p'
f = open(fileName,'r')
train3 = pickle.load(f)
f.close()

fileName ='C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/tryData/Pakulski_train4.p'
f = open(fileName,'r')
train4 = pickle.load(f)
f.close()

fileName ='C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/tryData/Driscoll_train5.p'
f = open(fileName,'r')
train5 = pickle.load(f)
f.close()

fileName ='C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/tryData/Driscoll_train6.p'
f = open(fileName,'r')
train6 = pickle.load(f)
f.close()

fileName ='C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/tryData/Pornelos_train7.p'
f = open(fileName,'r')
train7 = pickle.load(f)
f.close()

fileName ='C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/tryData/Nguyen_train8.p'
f = open(fileName,'r')
train8 = pickle.load(f)
f.close()

fileName ='C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/tryData/Girdzis_train9.p'
f = open(fileName,'r')
train9 = pickle.load(f)
f.close()

################ Test Data ###################
fileName ='C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/tryData/Glade_test0.p'
f = open(fileName,'r')
test0 = pickle.load(f)
f.close()

fileName ='C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/tryData/Glade_test1.p'
f = open(fileName,'r')
test1 = pickle.load(f)
f.close()

fileName ='C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/tryData/Gottfried_test2.p'
f = open(fileName,'r')
test2 = pickle.load(f)
f.close()

fileName ='C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/tryData/Pakulski_test3.p'
f = open(fileName,'r')
test3 = pickle.load(f)
f.close()

fileName ='C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/tryData/Pakulski_test4.p'
f = open(fileName,'r')
test4 = pickle.load(f)
f.close()

fileName ='C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/tryData/Driscoll_test5.p'
f = open(fileName,'r')
test5 = pickle.load(f)
f.close()

fileName ='C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/tryData/Driscoll_test6.p'
f = open(fileName,'r')
test6 = pickle.load(f)
f.close()

fileName ='C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/tryData/Pornelos_test7.p'
f = open(fileName,'r')
test7 = pickle.load(f)
f.close()

fileName ='C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/tryData/Nguyen_test8.p'
f = open(fileName,'r')
test8 = pickle.load(f)
f.close()

fileName ='C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/tryData/Girdzis_test9.p'
f = open(fileName,'r')
test9 = pickle.load(f)
f.close()




def ReshapeData(set0,set1,set2,set3,set4,set5,set6,set7,set8,set9):
    #print len(set1)
    #print set1.shape
    #print set1.ndim
    X = np.zeros((10000,5*2*3),dtype='f')
    y = np.zeros(10000,dtype='f')
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
                    X[i+2000,n] = set3[j,k,m,i]
                    X[i+3000,n] = set4[j,k,m,i]
                    X[i+4000,n] = set5[j,k,m,i]
                    X[i+5000,n] = set6[j,k,m,i]
                    X[i+6000,n] = set7[j,k,m,i]
                    X[i+7000,n] = set8[j,k,m,i]
                    X[i+8000,n] = set9[j,k,m,i]
                    y[i] = 0
                    y[i+1000] = 1
                    y[i+2000] = 2
                    y[i+3000] = 3
                    y[i+4000] = 4
                    y[i+5000] = 5
                    y[i+6000] = 6
                    y[i+7000] = 7
                    y[i+8000] = 8
                    y[i+9000] = 9
            
                    
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
    #np.absolute(allXCoordinates)
    meanValue = allXCoordinates.mean()
    X[0,::3] = allXCoordinates - meanValue
    
    allYCoordinates = X[0,1::3]
    meanValue = allYCoordinates.mean()
    X[0,1::3] = allYCoordinates - meanValue
    
    allZCoordinates = X[0,2::3]
    meanValue = allZCoordinates.mean()
    X[0,2::3] = allZCoordinates - meanValue
    
    return(X)
    
train0 = ReduceData(train0)
train1 = ReduceData(train1)
train2 = ReduceData(train2)
train3 = ReduceData(train3)
train4 = ReduceData(train4)
train5 = ReduceData(train5)
train6 = ReduceData(train6)
train7 = ReduceData(train7)  
train8 = ReduceData(train8)
train9 = ReduceData(train9)

test0 = ReduceData(test0)
test1 = ReduceData(test1)
test2 = ReduceData(test2)
test3 = ReduceData(test3)
test4 = ReduceData(test4)
test5 = ReduceData(test5)
test6 = ReduceData(test6)
test7 = ReduceData(test7)
test8 = ReduceData(test8)
test9 = ReduceData(test9)

train0 = CenterData(train0)
train1 = CenterData(train1)
train2 = CenterData(train2)
train3 = CenterData(train3)
train4 = CenterData(train4)
train5 = CenterData(train5)
train6 = CenterData(train6)
train7 = CenterData(train7)
train8 = CenterData(train8)
train9 = CenterData(train9)


test0 = CenterData(test0)
test1 = CenterData(test1)
test2 = CenterData(test2)
test3 = CenterData(test3)
test4 = CenterData(test4)
test5 = CenterData(test5)
test6 = CenterData(test6)
test7 = CenterData(test7)
test8 = CenterData(test8)
test9 = CenterData(test9)

trainX, trainy = ReshapeData(train0,train1,train2,train3,train4,train5,train6,train7,train8,train9)
testX, testy = ReshapeData(test0,test1,test2,test3,test4,test5,test6,test7,test8,test9)

clf = neighbors.KNeighborsClassifier(15)
clf.fit(trainX,trainy)
clf.fit(testX,testy)


correct = 0
for i in range(0,10000):
    #for j in range(0,120):
    prediction = clf.predict(testX[i,:])
    #print int(prediction)
    if (prediction == testy[i]):
        correct+=1

print float(correct)/float(10000)

pickle.dump(clf, open('C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/userData/classifier.p','wb'))
print ("done")
    
    