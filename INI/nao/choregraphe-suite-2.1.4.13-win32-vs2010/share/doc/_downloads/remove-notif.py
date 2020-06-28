# -*- encoding: UTF-8 -*- 
#!/usr/bin/env python

from naoqi import ALProxy

ROBOT_IP = "127.0.0.1"

alnotificationmanager = ALProxy("ALNotificationManager", ROBOT_IP, 9559)

# add new notification
notificationId = alnotificationmanager.add({"message": "Hello World!", "severity": "info", "removeOnRead": True})

print "Notification ID: " + str(notificationId)

# delete the notification
alnotificationmanager.remove(notificationId)
