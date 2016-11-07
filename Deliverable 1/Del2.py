#import Leap
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
matplotlib.interactive(True)
fig = plt.figure( figsize=(8,6) )
ax = fig.add_subplot( 111, projection='3d' )
plt.draw()
#controller = Leap.Controller()
#for i in range (1, 500):
#    frame = controller.frame()
#    if not frame.hands.is_empty: 
#        hand = frame.hands[0]
#        fingers = hand.fingers
#        indexFingerList = fingers.finger_type(Leap.Finger.TYPE_INDEX)
#        indexFinger = indexFingerList[0]
#        distalPhalange = indexFinger.bone(Leap.Bone.TYPE_DISTAL)
#        tip = distalPhalange.next_joint
#        print tip
while True:
    pass


    
    