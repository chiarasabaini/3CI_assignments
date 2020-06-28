# -*- encoding: UTF-8 -*-

''' Walk: Small example to make Nao walk '''
'''       Faster (Step of 6cm)          '''
''' This example is only compatible with NAO '''

import argparse
import time
from naoqi import ALProxy

def main(robotIP, PORT=9559):

    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.5)

    # Initialize the walk process.
    # Check the robot pose and take a right posture.
    # This is blocking called.
    motionProxy.moveInit()

    # TARGET VELOCITY
    X         = 1.0
    Y         = 0.0
    Theta     = 0.0
    Frequency = 1.0

    # Default walk (MaxStepX = 0.04 m)
    try:
        motionProxy.moveToward(X, Y, Theta, [["Frequency", Frequency]])
    except Exception, errorMsg:
        print str(errorMsg)
        print "This example is not allowed on this robot."
        exit()

    time.sleep(3.0)
    print "walk Speed X :",motionProxy.getRobotVelocity()[0]," m/s"

    # Speed walk  (MaxStepX = 0.06 m)
    # Could be faster: see walk documentation
    try:
        motionProxy.moveToward(X, Y, Theta, [["Frequency", Frequency],
                                             ["MaxStepX", 0.06]])
    except Exception, errorMsg:
        print str(errorMsg)
        print "This example is not allowed on this robot."
        exit()

    time.sleep(4.0)
    print "walk Speed X :",motionProxy.getRobotVelocity()[0]," m/s"

    # stop walk on the next double support
    motionProxy.stopMove()

    # Go to rest position
    motionProxy.rest()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
