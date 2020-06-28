# -*- encoding: UTF-8 -*-

'''Walk To: Small example to make Nao Walk follow'''
'''         a Dubins Curve '''

import argparse
import almath as m #python's wrapping of almath
from naoqi import ALProxy

def main(robotIP, PORT=9559):

    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.5)

    # first we defined the goal
    goal = m.Pose2D(0.0, -0.4, 0.0)

    # We get the dubins solution (control points) by
    # calling an almath function

    circleRadius = 0.04
    # Warning : the circle use by dubins curve
    #           have to be 4*CircleRadius < norm(goal)
    dubinsSolutionAbsolute = m.getDubinsSolutions(goal, circleRadius)

    # moveTo With control Points use relative commands but
    # getDubinsSolution return absolute position
    # So, we compute dubinsSolution in relative way
    dubinsSolutionRelative = []
    dubinsSolutionRelative.append(dubinsSolutionAbsolute[0])
    for i in range(len(dubinsSolutionAbsolute)-1):
        dubinsSolutionRelative.append(
                dubinsSolutionAbsolute[i].inverse() *
                dubinsSolutionAbsolute[i+1])

    # create a vector of moveTo with dubins Control Points
    moveToTargets = []
    for i in range(len(dubinsSolutionRelative)):
        moveToTargets.append(
            [dubinsSolutionRelative[i].x,
             dubinsSolutionRelative[i].y,
             dubinsSolutionRelative[i].theta] )

    # Initialized the Move process and be sure the robot is ready to move
    # without this call, the first getRobotPosition() will not refer to the position
    # of the robot before the move process
    motionProxy.moveInit()

    # get robot position before move
    robotPositionBeforeCommand  = m.Pose2D(motionProxy.getRobotPosition(False))

    motionProxy.moveTo( moveToTargets )

    # With MoveTo control Points, it's also possible to customize the gait parameters
    # motionProxy.moveTo(moveToTargets,
    #                    [["StepHeight", 0.001],
    #                     ["MaxStepX", 0.06],
    #                     ["MaxStepFrequency", 1.0]])

    # get robot position after move
    robotPositionAfterCommand = m.Pose2D(motionProxy.getRobotPosition(False))

    # compute and print the robot motion
    robotMoveCommand = m.pose2DInverse(robotPositionBeforeCommand)*robotPositionAfterCommand
    print "The Robot Move Command: ", robotMoveCommand

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
