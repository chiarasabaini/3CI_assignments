# -*- encoding: UTF-8 -*-

'''Move To: Small example to make Nao Move To an Objective '''
'''         With customization '''
''' This example is only compatible with NAO '''

import argparse
from naoqi import ALProxy

def main(robotIP, PORT=9559):

    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.5)

    x     = 0.2
    y     = 0.0
    theta = 0.0

    # This example show customization for the both foot
    # with all the possible gait parameters
    try:
        motionProxy.moveTo(x, y, theta,
            [ ["MaxStepX", 0.02],         # step of 2 cm in front
              ["MaxStepY", 0.16],         # default value
              ["MaxStepTheta", 0.4],      # default value
              ["MaxStepFrequency", 0.0],  # low frequency
              ["StepHeight", 0.01],       # step height of 1 cm
              ["TorsoWx", 0.0],           # default value
              ["TorsoWy", 0.1] ])         # torso bend 0.1 rad in front
    except Exception, errorMsg:
        print str(errorMsg)
        print "This example is not allowed on this robot."
        exit()

    # This example show customization for the both foot
    # with just one gait parameter, in this case, the other
    # parameters are set to the default value
    try:
        motionProxy.moveTo(x, y, theta, [ ["StepHeight", 0.04] ]) # step height of 4 cm
    except Exception, errorMsg:
        print str(errorMsg)
        print "This example is not allowed on this robot."
        exit()

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
