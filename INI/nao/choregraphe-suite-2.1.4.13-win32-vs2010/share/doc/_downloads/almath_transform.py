# -*- encoding: UTF-8 -*-

''' Example showing how to use almath with python and send the results to
    the robot by using a proxy to ALMotion '''

import argparse
import time

from naoqi import ALProxy

import almath

def main(robotIP, PORT=9559):

    # Create a proxy to ALMotion.
    try:
        motionProxy = ALProxy("ALMotion", robotIP, PORT)
    except Exception,e:
        print "Could not create proxy to ALMotion"
        print "Error was: ",e

    # Create a proxy to ALRobotPosture.
    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    except Exception,e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ",e

    # WakeUp
    motionProxy.wakeUp()

    # Stand up.
    postureProxy.goToPosture("StandInit", 0.3)

    chainName = "RArm"
    frame = 1 # FRAME_WORLD
    useSensors = True

    ##############################################
    # Retrieve a transform matrix using ALMotion #
    ##############################################

    # Retrieve current transform from ALMotion.
    # Convert it to a transform matrix for ALMath.
    origTransform = almath.Transform(
        motionProxy.getTransform(chainName, frame, useSensors))

    # Visualize the transform using overriden print from ALMath
    print "Original transform"
    print origTransform

    ##########################################################
    # Use almath to do some computations on transform matrix #
    ##########################################################

    # Compute a transform corresponding to the desired move
    # (here, move the chain for 5cm along the Z axis and the X axis).
    moveTransform = almath.Transform.fromPosition(0.05, 0.0, 0.05)

    # Compute the corresponding target transform.
    targetTransform = moveTransform * origTransform

    # Visualize it.
    print "Target transform"
    print targetTransform

    ##############################################
    # Send a transform to the robot via ALMotion #
    ##############################################

    # Convert it to a tuple.
    targetTransformList = list(targetTransform.toVector())

    # Send the target transform to NAO through ALMotion.
    fractionOfMaxSpeed = 0.5
    axisMask = almath.AXIS_MASK_VEL # Translation X, Y, Z
    motionProxy.setTransforms(
        chainName,
        frame,
        targetTransformList,
        fractionOfMaxSpeed,
        axisMask)

    time.sleep(2.0)
    motionProxy.rest()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
