import Leap
import matplotlib.pyplot as plt
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
xMin = -1000.0
xMax = 1000.0
yMin = 0
yMax = 1000.0
xPt = 0
yPt = yMax/2
pt, = plt.plot(xPt,yPt,'ko',markersize=20)
controller = Leap.Controller()
for i in range (1, 500):
    frame = controller.frame()
    if not frame.hands.is_empty:
        hand = frame.hands[0]
        fingers = hand.fingers
        indexFingerList = fingers.finger_type(Leap.Finger.TYPE_INDEX)
        indexFinger = indexFingerList[0]
        distalPhalange = indexFinger.bone(Leap.Bone.TYPE_DISTAL)
        tip = distalPhalange.next_joint
        x = tip.x*1.5
        y = tip.y*1.5
        if (x < xMin):
            xMin = x
        if (x > xMax):
            xMax = x
        if (y < yMin):
            yMin = y
        if (y > yMax):
            yMax = y
        print tip
        pt.set_xdata(x)
        pt.set_ydata(y)
    ax.set_xlim(xMin,xMax)
    ax.set_ylim(yMin,yMax)
    plt.pause(0.0001)
    plt.draw()