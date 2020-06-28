# -*- encoding: UTF-8 -*-

'''Cartesian control: Multiple Effector Trajectories'''
''' This example is only compatible with NAO '''

import argparse
import motion
import almath
from naoqi import ALProxy

def main(robotIP, PORT=9559):
    ''' Move the torso and keep arms fixed in nao space
    Warning: Needs a PoseInit before executing
    '''

    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.5)

    frame      = motion.FRAME_ROBOT
    useSensorValues = False

    effectorList = ["LArm", "RArm"]

    # Motion of Arms with block process
    axisMaskList = [almath.AXIS_MASK_VEL, almath.AXIS_MASK_VEL]

    timesList    = [[1.0], [1.0]] # seconds

    # LArm path
    pathLArm = []
    targetTf  = almath.Transform(motionProxy.getTransform("LArm", frame, useSensorValues))
    targetTf.r2_c4 -= 0.04 # y
    pathLArm.append(list(targetTf.toVector()))

    # RArm path
    pathRArm = []
    targetTf  = almath.Transform(motionProxy.getTransform("RArm", frame, useSensorValues))
    targetTf.r2_c4 += 0.04 # y
    pathRArm.append(list(targetTf.toVector()))

    pathList = []
    pathList.append(pathLArm)
    pathList.append(pathRArm)

    motionProxy.transformInterpolations(effectorList, frame, pathList,
                                       axisMaskList, timesList)

    effectorList = ["LArm", "RArm", "Torso"]

    # Motion of Arms and Torso with block process
    axisMaskList = [almath.AXIS_MASK_VEL,
                    almath.AXIS_MASK_VEL,
                    almath.AXIS_MASK_ALL]

    timesList    = [[4.0],                  # LArm  in seconds
                    [4.0],                  # RArm  in seconds
                    [1.0, 2.0, 3.0, 4.0]]   # Torso in seconds

    # LArm path
    pathLArm = []
    pathLArm.append(motionProxy.getTransform("LArm", frame, useSensorValues))

    # RArm path
    pathRArm = []
    pathRArm.append(motionProxy.getTransform("RArm", frame, useSensorValues))

    # Torso path
    pathTorso = []
    currentTf = motionProxy.getTransform("Torso", frame, useSensorValues)

    # 1
    targetTf  = almath.Transform(currentTf)
    targetTf.r2_c4 += 0.04 # y
    pathTorso.append(list(targetTf.toVector()))

    # 2
    targetTf  = almath.Transform(currentTf)
    targetTf.r1_c4 -= 0.03 # x
    pathTorso.append(list(targetTf.toVector()))

    # 3
    targetTf  = almath.Transform(currentTf)
    targetTf.r2_c4 -= 0.04 # y
    pathTorso.append(list(targetTf.toVector()))

    # 4
    pathTorso.append(currentTf)

    pathList = []
    pathList.append(pathLArm)
    pathList.append(pathRArm)
    pathList.append(pathTorso)

    motionProxy.transformInterpolations(effectorList, frame, pathList,
                                       axisMaskList, timesList)

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
