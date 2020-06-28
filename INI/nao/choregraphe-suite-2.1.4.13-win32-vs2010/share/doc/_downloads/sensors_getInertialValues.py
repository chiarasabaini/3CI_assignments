# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
import sys


def main(robotIP):
    PORT = 9559

    # Create proxy to ALMemory
    try:
        memoryProxy = ALProxy("ALMemory", robotIP, PORT)
    except Exception, e:
        print "Could not create proxy to ALMemory"
        print "Error was: ", e

    # Get the Gyrometers Values
    GyrX = memoryProxy.getData("Device/SubDeviceList/InertialSensor/GyrX/Sensor/Value")
    GyrY = memoryProxy.getData("Device/SubDeviceList/InertialSensor/GyrY/Sensor/Value")
    print ("Gyrometers value X: %.3f, Y: %.3f" % (GyrX, GyrY))

    # Get the Accelerometers Values
    AccX = memoryProxy.getData("Device/SubDeviceList/InertialSensor/AccX/Sensor/Value")
    AccY = memoryProxy.getData("Device/SubDeviceList/InertialSensor/AccY/Sensor/Value")
    AccZ = memoryProxy.getData("Device/SubDeviceList/InertialSensor/AccZ/Sensor/Value")
    print ("Accelerometers value X: %.3f, Y: %.3f, Z: %.3f" % (AccX, AccY,AccZ))

    # Get the Compute Torso Angle in radian
    TorsoAngleX = memoryProxy.getData("Device/SubDeviceList/InertialSensor/AngleX/Sensor/Value")
    TorsoAngleY = memoryProxy.getData("Device/SubDeviceList/InertialSensor/AngleY/Sensor/Value")
    print ("Torso Angles [radian] X: %.3f, Y: %.3f" % (TorsoAngleX, TorsoAngleY))


if __name__ == "__main__":
    robotIp = "127.0.0.1"

    if len(sys.argv) <= 1:
        print "Usage python sensors_getInertialValues.py robotIP (optional default: 127.0.0.1)"
    else:
        robotIp = sys.argv[1]

    main(robotIp)
