# -*- encoding: UTF-8 -*-

''' Walk: Small example to make Nao walk '''
'''       with gait customization        '''
'''       NAO is Keyser Soze             '''
''' This example is only compatible with NAO '''

import argparse
import time
import almath
from naoqi import ALProxy

def main(robotIP, PORT=9559):

    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.5)

    # TARGET VELOCITY
    X         = 1.0
    Y         = 0.0
    Theta     = 0.0
    Frequency = 1.0

    # Defined a limp walk
    try:
        motionProxy.moveToward(X, Y, Theta,[["Frequency", Frequency],
                                            # LEFT FOOT
                                            ["LeftStepHeight", 0.02],
                                            ["LeftTorsoWy", 5.0*almath.TO_RAD],
                                            # RIGHT FOOT
                                            ["RightStepHeight", 0.005],
                                            ["RightMaxStepX", 0.001],
                                            ["RightMaxStepFrequency", 0.0],
                                            ["RightTorsoWx", -7.0*almath.TO_RAD],
                                            ["RightTorsoWy", 5.0*almath.TO_RAD]] )
    except Exception, errorMsg:
        print str(errorMsg)
        print "This example is not allowed on this robot."
        exit()

    time.sleep(4.0)

    try:
        motionProxy.moveToward(X, Y, Theta, [["Frequency", Frequency]])
    except Exception, errorMsg:
        print str(errorMsg)
        print "This example is not allowed on this robot."
        exit()

    time.sleep(4.0)

    # stop walk in the next double support
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
