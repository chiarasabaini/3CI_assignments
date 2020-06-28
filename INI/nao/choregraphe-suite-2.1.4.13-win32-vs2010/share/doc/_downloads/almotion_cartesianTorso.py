# -*- encoding: UTF-8 -*-

'''Cartesian control: Torso trajectory'''

import argparse
import motion
import almath
from naoqi import ALProxy

def main(robotIP, PORT=9559):
    ''' Example showing a path of five positions
    Needs a PoseInit before execution
    '''

    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.5)

    effector   = "Torso"
    frame      =  motion.FRAME_WORLD
    axisMask   = almath.AXIS_MASK_ALL # full control
    useSensorValues = False

    # Define the changes relative to the current position
    dx         = 0.045 # translation axis X (meter)
    dy         = 0.050 # translation axis Y (meter)

    path = []
    currentTf = motionProxy.getTransform(effector, frame, useSensorValues)

    # point 1
    targetTf  = almath.Transform(currentTf)
    targetTf.r1_c4 += dx
    path.append(list(targetTf.toVector()))

    # point 2
    targetTf  = almath.Transform(currentTf)
    targetTf.r2_c4 -= dy
    path.append(list(targetTf.toVector()))

    # point 3
    targetTf  = almath.Transform(currentTf)
    targetTf.r1_c4 -= dx
    path.append(list(targetTf.toVector()))

    # point 4
    targetTf  = almath.Transform(currentTf)
    targetTf.r2_c4 += dy
    path.append(list(targetTf.toVector()))

    # point 5
    targetTf  = almath.Transform(currentTf)
    targetTf.r1_c4 += dx
    path.append(list(targetTf.toVector()))

    # point 6
    path.append(currentTf)

    times = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0] # seconds

    motionProxy.transformInterpolations(effector, frame, path, axisMask, times)

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
