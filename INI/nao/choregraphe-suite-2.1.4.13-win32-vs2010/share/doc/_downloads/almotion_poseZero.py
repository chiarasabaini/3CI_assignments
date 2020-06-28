# -*- encoding: UTF-8 -*-

''' PoseZero: Set all the motors of the body to zero. '''

import argparse
from naoqi import ALProxy

def main(robotIP, PORT=9559):

    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to Stand Zero
    postureProxy.goToPosture("StandZero", 0.5)

    # We use the "Body" name to signify the collection of all joints and actuators
    #pNames = "Body"

    # Get the Number of Joints
    #numBodies = len(motionProxy.getBodyNames(pNames))

    # We prepare a collection of floats
    #pTargetAngles = [0.0] * numBodies

    # We set the fraction of max speed
    #pMaxSpeedFraction = 0.3

    # Ask motion to do this with a blocking call
    #motionProxy.angleInterpolationWithSpeed(pNames, pTargetAngles, pMaxSpeedFraction)

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
