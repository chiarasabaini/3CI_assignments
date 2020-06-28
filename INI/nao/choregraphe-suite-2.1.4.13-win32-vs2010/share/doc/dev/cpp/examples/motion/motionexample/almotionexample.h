/**
* @author Chris Kilner - ckilner@aldebaran-robotics.com
* @author Cyrille Collette - ccollette@aldebaran-robotics.com
* Copyright (c) Aldebaran Robotics 2010-2014 All Rights Reserved.
*/

#ifndef MOTIONEXAMPLE_ALMOTIONEXAMPLE_H
#define MOTIONEXAMPLE_ALMOTIONEXAMPLE_H

#include <boost/shared_ptr.hpp>
#include <alcommon/almodule.h>
#include <string>

namespace AL
{
  class ALBroker;
}

/// <summary>
/// ALMotionExample.
/// A collection of examples showing how to talk to the ALMotion module from c++.
/// </summary>
class ALMotionExample : public AL::ALModule
{
public:
  /// <summary> Constructor. </summary>
  /// <param name="broker"> The broker. </param>
  /// <param name="name"> The name of the module </param>
  ALMotionExample(boost::shared_ptr<AL::ALBroker> broker, const std::string& name);

  /// <summary> Finaliser. </summary>
  virtual ~ALMotionExample();

  /// <summary>
  /// Cartesian arm 1.
  /// Moves the left arm with Cartesian Control, to one position then back again.
  /// </summary>
  void cartesianArm1();

  /// <summary>
  /// Cartesian arm 2.
  /// Moves the left arm with Cartesian Control, along a trajectory then back to the start.
  /// </summary>
  void cartesianArm2();

  /// <summary> Cartesian foot.
  /// Lowers the Torso and moves to the side, then moves the Left Leg left.
  /// </summary>
  void cartesianFoot();

  /// <summary>
  /// Cartesian torso.
  /// Belly dancing: makes the torso follow a near circular path.
  /// </summary>
  void cartesianTorso();

  /// <summary> Cartesian torso arm 1.
  /// Simultaneously controls three effectors :
  /// the Torso, the Left Arm and the Right Arm
  /// </summary>
  void cartesianTorsoArm1();

  /// <summary>
  /// Cartesian torso arm 2
  /// Moves the torso while keeping the arms fixed in nao space
  /// </summary>
  void cartesianTorsoArm2();

  /// <summary>
  /// Collision detection
  /// Nao bump on his torso and head with his arm
  /// </summary>
  void collisionDetection(const std::string& pChainName);

  /// <summary> Move hand. </summary>
  void moveHand();

  /// <summary> Moves Nao to the init pose. </summary>
  void poseInit();

  /// <summary>
  /// Moves Nao to the zero pose, where all joints are at angle zero
  /// </summary>
  void poseZero();

  /// <summary>
  /// Small example to make Nao execute
  /// The Cha Cha Basic Steps for Men
  /// Using setFootStep API
  /// http://www.dancing4beginners.com/cha-cha-steps.htm
  /// </summary>
  void setFootStepDance();

  /// <summary> Sets the stiffness to the minimum value. </summary>
  void stiffnessOff();

  /// <summary> Sets the stiffness to the maximum value. </summary>
  void stiffnessOn();

  /// <summary> Moves using the moveToward command and shows control of the arms. </summary>
  void move();

  /// <summary>
  /// Move: Small example to make Nao walk
  ///       with gait customization
  /// NAO is Keyser Soze
  /// </summary>
  void moveCustomization();

  /// <summary>
  /// Move: Small example to make Nao walk
  ///       Faster (Step of 6 cm)
  /// </summary>
  void moveFaster();

  /// <summary> Nao walks using the moveTo command and shows odometry. </summary>
  void moveTo();

  /// <summary>
  /// Move To: Small example to make Nao Walk To an Objective
  ///          With customization
  /// </summary>
  void moveToCustomization();

  /// <summary>
  /// Move To: Small example to make Nao Walk follow
  ///          a Dubins Curve
  /// </summary>
  void moveToDubinsCurve();

  /// <summary>
  /// Whole Body effector control head.
  /// Example of a whole body head orientation control
  /// </summary>
  void wbEffectorControlHead();

  /// <summary>
  /// Whole Body effector control arm.
  /// </summary>
  void wbEffectorControlArm(const std::string& pName);

  /// <summary>
  /// Whole Body effector control constraint.
  /// Balance Constraints
  /// </summary>
  void wbEffectorControlConstraint();

  /// <summary>
  /// Whole body constraints to keep the feet on the plane,
  /// despite conflicting commands.
  /// </summary>
  void wbFootState();

  /// <summary>
  /// Example of a whole body kick
  /// </summary>
  void wbKick();

  /// <summary>
  /// Example of a whole body multiple effectors control "LArm", "RArm" and "Torso"
  /// </summary>
  void wbMultipleEffectors();

protected:

  void xMoveArm(
    const std::string& pTargetName,
    const std::string& pRobotName,
    const std::string& pChainName);
};

#endif  // MOTIONEXAMPLE_ALMOTIONEXAMPLE_H

