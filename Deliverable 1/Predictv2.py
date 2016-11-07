import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors, datasets

iris = datasets.load_iris()

trainX = iris.data[::2,1:3]
trainy = iris.target[::2]

testX = iris.data[1::2,1:3]
testy = iris.target[1::2]

colors = np.zeros((3,3), dtype='f')
colors[0,:] = [1,0.5,0.5]
colors[1,:] = [0.5,1,0.5]
colors[2,:] = [0.5,0.5,1]

clf = neighbors.KNeighborsClassifier(15)
clf.fit(trainX,trainy)

#actualClass = testy[32]
#prediction = clf.predict(testX[32,1:3])
#print actualClass, prediction

plt.figure()
[numItems,numFeatures] = iris.data.shape
for i in range(0,numItems/2):
    itemClass = int(trainy[i])
    currColor = colors[itemClass,:]
    plt.scatter(trainX[i,0], trainX[i,1], facecolor=currColor, s=50, lw=2)
    
counter = 0
for i in range(0,numItems/2):
    itemClass = testy[i]
    currColor = colors[itemClass,:]
    prediction = int(clf.predict(testX[i,:]))
    if (prediction == itemClass):
        counter+=1
    edgeColor = colors[prediction,:] 
    plt.scatter(testX[i,0], testX[i,1], facecolor=currColor, s=50, lw=2, edgecolor=edgeColor)

accuracy = float(counter)/len(testX)*100
print accuracy
print counter
plt.show()