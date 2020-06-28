/**
* @author Chris Kilner - ckilner@aldebaran-robotics.com
* @author Cyrille Collette - ccollette@aldebaran-robotics.com
* Copyright (c) Aldebaran Robotics 2010-2014 All Rights Reserved.
*/

#include "almotionexample.h"

#include <alvalue/alvalue.h>
#include <alcommon/albroker.h>
#include <alproxies/alrobotpostureproxy.h>
#include <alproxies/almotionproxy.h>
#include <qi/os.hpp>

#include <almath/types/alpose2d.h>
#include <almath/tools/aldubinscurve.h>
#include <almath/tools/almathio.h>
#include <almath/tools/almath.h>
#include <almath/tools/altrigonometry.h>

#include <iostream>

/// <summary>Constructor.</summary>
/// <param name="broker">The broker.</param>
/// <param name="name">The name of the module.</param>
ALMotionExample::ALMotionExample(
    boost::shared_ptr<AL::ALBroker> broker,
    const std::string& name): AL::ALModule(broker, name)
{
  setModuleDescription("A collection of examples showing how "
                       "to talk to the ALMotion module from c++.");

  functionName("cartesianArm1",
               "ALMotionExample",
               "Moves the left arm with Cartesian Control, to one position then back again.");
  BIND_METHOD(ALMotionExample::cartesianArm1);

  functionName("cartesianArm2",
               "ALMotionExample",
               "Moves the left arm with Cartesian Control, "
               "along a trajectory then back to the start.");
  BIND_METHOD(ALMotionExample::cartesianArm2);

  functionName("cartesianFoot",
               "ALMotionExample",
               "Lowers the Torso and moves to the side, then moves the Left Leg left.");
  BIND_METHOD(ALMotionExample::cartesianFoot);

  functionName("cartesianTorso",
               "ALMotionExample",
               "Belly dancing: makes the torso follow a near circular path.");
  BIND_METHOD(ALMotionExample::cartesianTorso);

  functionName("cartesianTorsoArm1",
               "ALMotionExample",
               "Simultaneously controls three effectors: "
               "the Torso, the Left Arm and the Right Arm");
  BIND_METHOD(ALMotionExample::cartesianTorsoArm1);

  functionName("cartesianTorsoArm2",
               "ALMotionExample",
               "Moves the torso while keeping the arms fixed in ROBOT_FRAME.");
  BIND_METHOD(ALMotionExample::cartesianTorsoArm2);

  functionName("collisionDetection",
               "ALMotionExample",
               "Collision detection: Nao bump on his torso and head with his arm.");
  addParam("pChainName",
           "The chain name: could be \"LArm\" or \"RArm\".");
  BIND_METHOD(ALMotionExample::collisionDetection);

  functionName("moveHand",
               "ALMotionExample",
               "Moves the hands using interpolation and "
               "the openHand and closeHand methods.");
  BIND_METHOD(ALMotionExample::moveHand);

  functionName("poseInit",
               "ALMotionExample",
               "Moves Nao to the init pose.");
  BIND_METHOD(ALMotionExample::poseInit);

  functionName("poseZero",
               "ALMotionExample",
               "Moves Nao to the zero pose, where all joints are at angle zero.");
  BIND_METHOD(ALMotionExample::poseZero);

  functionName("setFootStepDance",
               "ALMotionExample",
               "Small example to make Nao execute "
               "The Cha Cha Basic Steps for Men Using setFootStep API.");
  BIND_METHOD(ALMotionExample::setFootStepDance);

  functionName("stiffnessOff",
               "ALMotionExample",
               "Sets the stiffness to the minimum value.");
  BIND_METHOD(ALMotionExample::stiffnessOff);

  functionName("stiffnessOn",
               "ALMotionExample",
               "Sets the stiffness to the maximum value.");
  BIND_METHOD(ALMotionExample::stiffnessOn);

  functionName("move",
               "ALMotionExample",
               "Moves using the moveToward command and shows control of the arms.");
  BIND_METHOD(ALMotionExample::move);

  functionName("moveCustomization",
               "ALMotionExample",
               "Move: Small example to make Nao walk "
               "with gait customization. NAO is Keyser Soze.");
  BIND_METHOD(ALMotionExample::moveCustomization);

  functionName("moveFaster",
               "ALMotionExample",
               "Move: Small example to make Nao walk Faster (Step of 6 cm)");
  BIND_METHOD(ALMotionExample::moveFaster);

  functionName("moveTo",
               "ALMotionExample",
               "Nao walks using the moveTo command and shows odometry.");
  BIND_METHOD(ALMotionExample::moveTo);

  functionName("moveToCustomization",
               "ALMotionExample",
               "Move To: Small example to make Nao Move To "
               "an Objective With customization.");
  BIND_METHOD(ALMotionExample::moveToCustomization);

  functionName("moveToDubinsCurve",
               "ALMotionExample",
               "Move To: Small example to make Nao Walk follow a Dubins Curve.");
  BIND_METHOD(ALMotionExample::moveToDubinsCurve);

  functionName("wbEffectorControlHead",
               "ALMotionExample",
               "Whole body head orientation control.");
  BIND_METHOD(ALMotionExample::wbEffectorControlHead);

  functionName("wbEffectorControlArm",
               "ALMotionExample",
               "Whole body arm position control.");
  addParam("name", "The name of arm: LArm or RArm.");
  BIND_METHOD(ALMotionExample::wbEffectorControlArm);

  functionName("wbEffectorControlConstraint",
               "ALMotionExample",
               "Whole Body balance control.");
  BIND_METHOD(ALMotionExample::wbEffectorControlConstraint);

  functionName("wbFootState",
               "ALMotionExample",
               "Whole body constraints to keep the feet on the plane, "
               "despite conflicting commands.");
  BIND_METHOD(ALMotionExample::wbFootState);

  functionName("wbKick",
               "ALMotionExample",
               "Example of a whole body kick");
  BIND_METHOD(ALMotionExample::wbKick);

  functionName("wbMultipleEffectors",
               "ALMotionExample",
               "Example of a whole body multiple effectors control "
               "\"LArm\", \"RArm\" and \"Torso\".");
  BIND_METHOD(ALMotionExample::wbMultipleEffectors);
}

/// <summary> Destructor. </summary>
ALMotionExample::~ALMotionExample() {}


/// <summary>
/// Cartesian arm 1.
/// Moves the left arm with Cartesian Control, to one position then back again.
/// This example is only compatible with NAO.
/// </summary>
void ALMotionExample::cartesianArm1()
{
  // get a proxy to motion
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();
  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  // Wake up robot
  motionProxy->wakeUp();

  // Send robot to Stand Init
  postureProxy->goToPosture("StandInit", 0.5f);

  // prepare the command
  const std::string effector = "LArm";

  // FRAMES: FRAME_TORSO 0, FRAME_WORLD 1, FRAME_ROBOT 2
  // AXIS MASKS: X 1, Y 2, Z 4, WX 8, WY 16, WZ 32
  int  frame      = 2; // use FRAME_ROBOT
  int  axisMask   = 7; // just control position (X+Y+Z)

  // Since we are in relative, the current position is zero
  // Here we are using the ALValue::array constuctor, as it
  // is easier to use than std::vector when adding multiple items
  const bool useSensorValues = false;
  AL::Math::Transform currentTf =
      AL::Math::Transform(motionProxy->getTransform(effector, frame, useSensorValues));

  AL::Math::Transform targetTf = currentTf;
  targetTf.r1_c4 += 0.03f; //x
  targetTf.r2_c4 += 0.03f; //y

  // make a trajectory by making an array containing the two positions
  // go to the target and back again
  const AL::ALValue path = AL::ALValue::array(targetTf.toVector(), currentTf.toVector());

  // times in seconds, exactly one time per target position in the trajectory
  const AL::ALValue times = AL::ALValue::array(2.0f, 4.0f);

  motionProxy->transformInterpolations(
        effector, frame, path, axisMask, times);

  motionProxy->rest();
}


/// <summary>
/// Cartesian arm 2.
/// Moves the left arm with Cartesian Control, along a trajectory then back to the start.
/// This example is only compatible with NAO.
/// </summary>
void ALMotionExample::cartesianArm2()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();

  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  // Wake up robot
  motionProxy->wakeUp();

  // Send robot to Stand Init
  postureProxy->goToPosture("StandInit", 0.5f);

  // FRAMES: FRAME_TORSO 0, FRAME_WORLD 1, FRAME_ROBOT 2
  // AXIS MASKS: X 1, Y 2, Z 4, WX 8, WY 16, WZ 32
  std::string effector   = "LArm";
  int         frame      = 2;      // use FRAME_ROBOT
  int         axisMask   = 7;      // just control position
  const bool useSensorValues = false;

  const AL::Math::Transform currentTf =
      AL::Math::Transform(motionProxy->getTransform(effector, frame, useSensorValues));

  AL::Math::Transform targetTf1 = currentTf;
  targetTf1.r2_c4 -= 0.05f; //y

  AL::Math::Transform targetTf2 = currentTf;
  targetTf2.r3_c4 += 0.04f; //z

  AL::Math::Transform targetTf3 = currentTf;
  targetTf3.r2_c4 += 0.04f; //y

  AL::Math::Transform targetTf4 = currentTf;
  targetTf4.r3_c4 -= 0.02f; //z

  AL::Math::Transform targetTf5 = currentTf;
  targetTf5.r2_c4 -= 0.05f; //y

  AL::ALValue path = AL::ALValue::array(
        targetTf1.toVector(),
        targetTf2.toVector(),
        targetTf3.toVector(),
        targetTf4.toVector(),
        targetTf5.toVector(),
        currentTf.toVector());

  // time in seconds
  const AL::ALValue times = AL::ALValue::array(0.5f, 1.0f, 2.0f, 3.0f, 4.0f, 4.5f);

  motionProxy->transformInterpolations(
        effector, frame, path, axisMask, times);

  motionProxy->rest();
}


/// <summary> Cartesian foot.
/// Lowers the Torso and moves to the side, then moves the Left Leg left.
/// This example is only compatible with NAO.
/// </summary>
void ALMotionExample::cartesianFoot()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();
  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  // Wake up robot
  motionProxy->wakeUp();

  // Send robot to Stand Init
  postureProxy->goToPosture("StandInit", 0.5f);

  // FRAMES: FRAME_TORSO 0, FRAME_WORLD 1, FRAME_ROBOT 2
  // AXIS MASKS: X 1, Y 2, Z 4, WX 8, WY 16, WZ 32
  std::string effector   = "Torso";
  int         frame      = 1;      // use FRAME_WORLD
  int         axisMask   = 63;     // control all the effector's axes
  float       duration   = 2.0f;   // seconds
  const bool useSensorValues = false;

  const AL::Math::Transform currentTorsoTf =
      AL::Math::Transform(motionProxy->getTransform(effector, frame, useSensorValues));
  const AL::Math::Transform targetTorsoTf =
      currentTorsoTf*AL::Math::Transform(0.0, -0.06f, -0.03f);
  AL::ALValue path = AL::ALValue::array(targetTorsoTf.toVector());

  // Lower the Torso and move to the side
  motionProxy->transformInterpolations(
        effector, frame, path,
        axisMask, duration);

  // LLeg motion to the left
  effector = "LLeg";
  AL::Math::Transform currentLLegTf;
  try
  {
    currentLLegTf = AL::Math::Transform(
          motionProxy->getTransform(effector, frame, useSensorValues));
  }
  catch(const std::exception& e)
  {
    std::cerr << e.what()<< std::endl;
    std::cerr << "This example is not allowed on this robot.\n";
    return;
  }
  const AL::Math::Transform targetLLegTf =
      currentLLegTf*
      AL::Math::Transform(0.0f, 0.04f, 0.0f)*
      AL::Math::Transform::fromRotZ(45.0f*AL::Math::TO_RAD);

  path = AL::ALValue::array(targetLLegTf.toVector());

  motionProxy->transformInterpolations(
        effector, frame, path, axisMask, duration);

  motionProxy->rest();
}


/// <summary>
/// Cartesian torso.
/// Belly dancing: makes the torso follow a near circular path.
/// This example is only compatible with NAO.
/// </summary>
void ALMotionExample::cartesianTorso()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();
  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  // Wake up robot
  motionProxy->wakeUp();

  // Send robot to Stand Init
  postureProxy->goToPosture("StandInit", 0.5f);

  std::string effector   = "Torso";
  int         frame      = 1;       // FRAME_WORLD
  int         axisMask   = 63;      // Full control
  float       dx         = 0.045f;  // relative translation axis X (meters)
  float       dy         = 0.050f;  // relative translation axis Y (meters)
  const bool useSensorValues = false;

  const AL::Math::Transform currentTf =
      AL::Math::Transform(motionProxy->getTransform(effector, frame, useSensorValues));

  AL::Math::Transform target1Tf = currentTf;
  target1Tf.r1_c4 += dx;

  AL::Math::Transform target2Tf = currentTf;
  target2Tf.r2_c4 -= dy;

  AL::Math::Transform target3Tf = currentTf;
  target3Tf.r1_c4 -= dx;

  AL::Math::Transform target4Tf = currentTf;
  target4Tf.r2_c4 += dy;

  AL::Math::Transform target5Tf = currentTf;
  target5Tf.r1_c4 += dx;

  AL::ALValue path = AL::ALValue::array(
    target1Tf.toVector(),
    target2Tf.toVector(),
    target3Tf.toVector(),
    target4Tf.toVector(),
    target5Tf.toVector(),
    currentTf.toVector());

  // Times in seconds
  const AL::ALValue times = AL::ALValue::array(1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f);

  motionProxy->transformInterpolations(
        effector, frame, path, axisMask, times);

  motionProxy->rest();
}

/// <summary> Cartesian torso arm 1.
/// Simultaneously controls three effectors:
/// the Torso, the Left Arm and the Right Arm
/// This example is only compatible with NAO.
/// </summary>
void ALMotionExample::cartesianTorsoArm1()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();
  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  // Wake up robot
  motionProxy->wakeUp();

  // Send robot to Stand Init
  postureProxy->goToPosture("StandInit", 0.5f);

  int   frame       = 1;     // FRAME_WORLD
  int   axisMask    = 63;    // control all the effector axes
  bool  isAbsolute  = false;
  float coef        = 0.5f;  // the time per movement in seconds
  AL::ALValue times = AL::ALValue::array(
        coef, 2.0f*coef, 3.0f*coef, 4.0f*coef);

  // Relative movement between current and desired positions
  float dy         = +0.03f;  // translation axis Y (meters)
  float dz         = -0.03f;  // translation axis Z (meters)
  float dwx        = +8.0f*AL::Math::TO_RAD;  // rotation axis X (radians)

  const bool useSensorValues = false;

  // Motion of Torso with post process
  std::string effector   = "Torso";

  const AL::Math::Transform initTorsoTf =
      AL::Math::Transform(motionProxy->getTransform(effector, frame, useSensorValues));

  const AL::Math::Transform target1TorsoTf =
      initTorsoTf*
      AL::Math::Transform(0.0, -dy, dz)*
      AL::Math::Transform().fromRotX(-dwx);

  const AL::Math::Transform target2TorsoTf =
      initTorsoTf*
      AL::Math::Transform(0.0, dy, dz)*
      AL::Math::Transform().fromRotX(dwx);

  const AL::ALValue pathTorso = AL::ALValue::array(
        target1TorsoTf.toVector(),
        initTorsoTf.toVector(),
        target2TorsoTf.toVector(),
        initTorsoTf.toVector());

  motionProxy->post.transformInterpolations(
        effector, frame, pathTorso,
        axisMask, times);

  // Motion of the Arms one after the other
  axisMask = 7; // control just the position
  times = AL::ALValue::array(1.0f * coef, 2.0f * coef);  // seconds

  // Motion of Right Arm during the first half of the Torso motion
  effector = "RArm";
  const AL::Math::Transform initRArmTf =
      AL::Math::Transform(motionProxy->getTransform(effector, frame, useSensorValues));

  AL::Math::Transform target1RArmTf = initRArmTf;
  target1RArmTf.r2_c4 -= 0.04f;

  const AL::ALValue pathRArm = AL::ALValue::array(
        target1RArmTf.toVector(),
        initRArmTf.toVector());

  // blocking call to position interpolation
  motionProxy->transformInterpolations(
        effector, frame, pathRArm,
        axisMask, times);

  // Motion of Left Arm during the last half of the Torso motion
  effector = "LArm";
  const AL::Math::Transform initLArmTf =
      AL::Math::Transform(motionProxy->getTransform(effector, frame, useSensorValues));

  AL::Math::Transform target1LArmTf = initLArmTf;
  target1LArmTf.r2_c4 += 0.04f;

  const AL::ALValue pathLArm = AL::ALValue::array(
        target1LArmTf.toVector(),
        initLArmTf.toVector());

  // blocking call to position interpolation
  motionProxy->transformInterpolations(
        effector, frame, pathLArm, axisMask, times);

  motionProxy->rest();
}


/// <summary>
/// Cartesian torso arm 2
/// Moves the torso while keeping the arms fixed in FRAME_ROBOT
/// This example is only compatible with NAO.
/// </summary>
void ALMotionExample::cartesianTorsoArm2()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();
  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  // Wake up robot
  motionProxy->wakeUp();

  // Send robot to Stand Init
  postureProxy->goToPosture("StandInit", 0.5f);

  // Motion of Arms with block process
  std::vector<std::string> effectorNames;
  effectorNames.resize(2u);
  effectorNames.at(0) = "LArm";
  effectorNames.at(1) = "RArm";

  const int frame = 2; // FRAME_ROBOT

  // control just the position for both effectors
  AL::ALValue axisMask = AL::ALValue::array(7, 7);

  AL::ALValue timesList = AL::ALValue::array(
        AL::ALValue::array(1.0f),   // LArm in seconds
        AL::ALValue::array(1.0f));  // RArm in seconds

  const bool useSensorValues = false;

  // LArm path
  AL::Math::Transform targetLArmTf =
      AL::Math::Transform(motionProxy->getTransform("LArm", frame, useSensorValues));
  targetLArmTf.r2_c4 -= 0.04f; // y

  // RArm path
  AL::Math::Transform targetRArmTf =
      AL::Math::Transform(motionProxy->getTransform("RArm", frame, useSensorValues));
  targetRArmTf.r2_c4 += 0.04f; // y

  AL::ALValue pathList = AL::ALValue::array(
        AL::ALValue::array(targetLArmTf.toVector()),
        AL::ALValue::array(targetRArmTf.toVector()));

  motionProxy->transformInterpolations(
        effectorNames, frame, pathList,
        axisMask, timesList);

  // Motion of Arms and Torso with block process
  effectorNames.resize(3u);
  effectorNames.at(0) = "LArm";
  effectorNames.at(1) = "RArm";
  effectorNames.at(2) = "Torso";

  targetLArmTf = AL::Math::Transform(
        motionProxy->getTransform("LArm", frame, useSensorValues));

  targetRArmTf = AL::Math::Transform(
        motionProxy->getTransform("RArm", frame, useSensorValues));

  AL::Math::Transform initTorsoTf = AL::Math::Transform(
        motionProxy->getTransform("Torso", frame, useSensorValues));

  AL::Math::Transform targetTorso1Tf = initTorsoTf;
  targetTorso1Tf.r2_c4 += 0.04f; // y

  AL::Math::Transform targetTorso2Tf = initTorsoTf;
  targetTorso2Tf.r1_c4 -= 0.03f; // x

  AL::Math::Transform targetTorso3Tf = initTorsoTf;
  targetTorso3Tf.r2_c4 -= 0.04f; // y

  AL::ALValue pathTorso = AL::ALValue::array(
        targetTorso1Tf.toVector(),
        targetTorso2Tf.toVector(),
        targetTorso3Tf.toVector(),
        initTorsoTf.toVector());

  pathList = AL::ALValue::array(
        targetLArmTf.toVector(),
        targetRArmTf.toVector(),
        pathTorso);

  axisMask = AL::ALValue::array(
        7,   // LArm  control just the position
        7,   // RArm  control just the position
        63); // Torso control all axis


  timesList = AL::ALValue::array(
        AL::ALValue::array(4.0f),                    // LArm  in seconds
        AL::ALValue::array(4.0f),                    // RArm  in seconds
        AL::ALValue::array(1.0f, 2.0f, 3.0f, 4.0f)); // Torso in seconds

  motionProxy->transformInterpolations(
        effectorNames, frame, pathList,
        axisMask, timesList);

  motionProxy->rest();
}


/// <summary>
/// Example showing the effect of collision detection
///  Nao bumps his chest with his left arm with collision detection enabled
///  or disabled.
/// This example is only compatible with NAO.
/// </summary>
void ALMotionExample::collisionDetection(const std::string& pChainName)
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();
  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  if (pChainName != "LArm" && pChainName != "RArm")
  {
    std::cerr << "ERROR: chainName is unknown" << std::endl;
    std::cerr << "Must be LArm or RArm" << std::endl;
    return;
  }

  ////////////////////
  // Initialization //
  ////////////////////

  // Wake up robot
  motionProxy->wakeUp();

  // Send robot to Stand Init
  postureProxy->goToPosture("StandInit", 0.5f);

  // Get the robot configuration.
  AL::ALValue robotConfig = motionProxy->getRobotConfig();
  std::string pRobotName = (std::string) robotConfig[1][0];

  /////////////////////////////////
  // Arm motion bumping on torso //
  /////////////////////////////////

  // Disable collision detection on chainName.
  bool pEnable = false;
  bool success = motionProxy->setCollisionProtectionEnabled(pChainName, pEnable);
  if (!success)
  {
    std::cerr << "Failed to disable collision protection" << std::endl;
  }
  qi::os::msleep(1000u);

  // Make NAO's arm move so that it bumps its torso.
  std::string pTargetName = "Torso";

  xMoveArm(pTargetName, pRobotName, pChainName);
  qi::os::msleep(1000u);

  // Go back to pose init.
  postureProxy->goToPosture("StandInit", 0.5f);

  // Enable collision detection on chainName.
  pEnable = true;
  success = motionProxy->setCollisionProtectionEnabled(pChainName, pEnable);
  if (!success)
  {
    std::cerr << "Failed to enable collision protection" << std::endl;
  }
  qi::os::msleep(1000u);

  // Make NAO's arm move and see that it does not bump on the torso.
  pTargetName = "Torso";
  xMoveArm(pTargetName, pRobotName, pChainName);
  qi::os::msleep(1000u);

  // Go back to pose init.
  postureProxy->goToPosture("StandInit", 0.5f);

  ////////////////////////////////
  // Arm motion bumping on head //
  ////////////////////////////////

  // Disable collision detection on chainName.
  pEnable = false;
  success = motionProxy->setCollisionProtectionEnabled(pChainName, pEnable);
  if (!success)
  {
    std::cerr << "Failed to disable collision protection" << std::endl;
  }
  qi::os::msleep(1000u);

  // Make NAO's arm move so that it bumps its head.
  pTargetName = "Head";
  xMoveArm(pTargetName, pRobotName, pChainName);

  qi::os::msleep(1000u);
  // Go back to pose init.
  postureProxy->goToPosture("StandInit", 0.5f);

  // Enable collision detection on chainName.
  pEnable = true;
  success = motionProxy->setCollisionProtectionEnabled(pChainName, pEnable);
  if (!success)
  {
    std::cerr << "Failed to enable collision protection" << std::endl;
  }
  // Make NAO's arm move and see that it does not bump on the head.
  pTargetName = "Head";
  xMoveArm(pTargetName, pRobotName, pChainName);

  qi::os::msleep(1000u);
  // Go to rest
  motionProxy->rest();
}


void ALMotionExample::xMoveArm(
    const std::string& pTargetName,
    const std::string& pRobotName,
    const std::string& pChainName)
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();

  // Function to make NAO bump on his torso with his arm '''

  // Set the fraction of max speed for the arm movement.
  float pMaxSpeedFraction = 0.5f;

  // Define the final position.
  float shoulderPitchAngle = 0.0f;
  if (pTargetName == "Torso")
  {
    shoulderPitchAngle = 50.0f * AL::Math::TO_RAD;
  }
  else if (pTargetName == "Head")
  {
    shoulderPitchAngle = -50.0f * AL::Math::TO_RAD;
  }
  else
  {
    std::cerr << "ERROR: target is unknown" << std::endl;
    std::cerr << "Must be Torso or Head" << std::endl;
    std::cerr << "---------------------" << std::endl;
    return;
  }

  float ShoulderRollAngle  =    6.0f * AL::Math::TO_RAD;
  float ElbowYawAngle      =    0.0f * AL::Math::TO_RAD;
  float ElbowRollAngle     = -150.0f * AL::Math::TO_RAD;

  AL::ALValue pTargetAngles;

  if (pChainName == "LArm")
  {
    pTargetAngles.arrayPush(shoulderPitchAngle);
    pTargetAngles.arrayPush(+ShoulderRollAngle);
    pTargetAngles.arrayPush(+ElbowYawAngle);
    pTargetAngles.arrayPush(+ElbowRollAngle);
  }
  else if (pChainName == "RArm")
  {
    pTargetAngles.arrayPush(shoulderPitchAngle);
    pTargetAngles.arrayPush(-ShoulderRollAngle);
    pTargetAngles.arrayPush(-ElbowYawAngle);
    pTargetAngles.arrayPush(-ElbowRollAngle);
  }
  else
  {
    std::cerr << "ERROR: chainName is unknown" << std::endl;
    std::cerr << "Must be LArm or RArm" << std::endl;
    std::cerr << "---------------------" << std::endl;
    return;
  }

  // Set the target angles according to the robot version.
  if (pRobotName == "naoH25" ||
      pRobotName == "naoAcademics" ||
      pRobotName == "naoT14")
  {
    pTargetAngles.arrayPush(0.0f);
    pTargetAngles.arrayPush(0.0f);
  }
  else if (pRobotName == "naoH21" ||
           pRobotName == "naoRobocup")
  {
    // Do nothing
  }
  else if (pRobotName == "naoT2")
  {
    return;
  }
  else
  {
    std::cerr << "ERROR: Your robot is unknown" << std::endl;
    std::cerr << "This test is not available for your Robot" << std::endl;
    std::cerr << "---------------------" << std::endl;
    return;
  }

  // Move the arm to the final position.
  motionProxy->angleInterpolationWithSpeed(
        pChainName, pTargetAngles, pMaxSpeedFraction);
}


/// <summary> Move hand. </summary>
void ALMotionExample::moveHand()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();

  //bool MOVE_HAND_BY_INTERPOLATION = true;
  bool MOVE_HAND_BY_INTERPOLATION = false;

  // Get the Type of Nao
  AL::ALValue robotConfig = motionProxy->getRobotConfig();
  bool robotHasHands = (bool) robotConfig[1][7];

  if (!robotHasHands)
  {
    std::cerr << "ERROR : Your robot doesn't have Hands" << std::endl;
    std::cerr << "This test is not availbale for your Robot" << std::endl;
    return;  // no hands
  }

  if (MOVE_HAND_BY_INTERPOLATION)
  {
    // control of the hands using interpolation
    std::string handName   = "LHand";
    float stiffness        = 1.0f;  // max stiffness
    float time             = 1.0f;  // seconds
    float maxSpeedFraction = 0.5f;  // half of max speed

    // turn stiffness on for the LHand
    motionProxy->stiffnessInterpolation(handName, stiffness, time);
    // interpolate to an "angle" of 1.0
    // the hands use the same API as other joints, but the angle
    // of 1.0 doesn't correspond to a real angle. It means
    // fully open.
    motionProxy->angleInterpolationWithSpeed(handName, 1.0, maxSpeedFraction);
    // interpolate to an "angle" of 0.0
    motionProxy->angleInterpolationWithSpeed(handName, 0.0, maxSpeedFraction);
    // at this point, stiffness is still on. It is usally good practice
    // to reducte the stiffness for the hands as it isn't required to
    // maintain the closed position
  }
  else
  {
    // NOTE that open and close Hand methods put Stiffness to 0.0
    // after execution.

    // Close hands
    std::string handName = "RHand";
    motionProxy->closeHand(handName);
    handName = "LHand";
    motionProxy->closeHand(handName);

    qi::os::msleep(2000u);

    // Open hands
    handName = "RHand";
    motionProxy->openHand(handName);
    handName = "LHand";
    motionProxy->openHand(handName);

    qi::os::msleep(2000u);

    // Close hands
    handName = "RHand";
    motionProxy->closeHand(handName);
    handName = "LHand";
    motionProxy->closeHand(handName);
  }
}

/// <summary> Moves Robot to the init pose. </summary>
void ALMotionExample::poseInit()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();

  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  motionProxy->wakeUp();

  std::string posture = "StandInit";
  const float maxSpeedFraction = 0.2f;

  postureProxy->applyPosture(posture, maxSpeedFraction);

  motionProxy->rest();
}

/// <summary>
/// Moves robot to the zero pose, where all joints are at angle zero
/// </summary>
void ALMotionExample::poseZero()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();

  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  motionProxy->wakeUp();

  std::string posture = "StandZero";
  const float maxSpeedFraction = 0.3f;

  postureProxy->applyPosture(posture, maxSpeedFraction);

  motionProxy->rest();
}

/// <summary>
/// Small example to make Nao execute
/// The Cha Cha Basic Steps for Men
/// Using setFootStep API
/// http://www.dancing4beginners.com/cha-cha-steps.htm
/// This example is only compatible with NAO.
/// </summary>
void ALMotionExample::setFootStepDance()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();
  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  // Wake up robot
  motionProxy->wakeUp();

  // Send robot to Stand Init
  postureProxy->goToPosture("StandInit", 0.5f);

  ///////////////////////////////
  // First we defined each step
  ///////////////////////////////
  std::vector<std::vector<std::string> > legNameList;
  std::vector<std::string> llegName;
  llegName.push_back("LLeg");
  std::vector<std::string> rlegName;
  rlegName.push_back("RLeg");

  std::vector<AL::ALValue> footStepsList;

  // 1) Step forward with your left foot
  legNameList.push_back(llegName);
  footStepsList.push_back(AL::ALValue::array(AL::ALValue::array(0.06, 0.1, 0.0)));

  // 2) Sidestep to the left with your left foot
  legNameList.push_back(llegName);
  footStepsList.push_back(AL::ALValue::array(AL::ALValue::array(0.00f, 0.16f, 0.0f)));

  // 3) Move your right foot to your left foot
  legNameList.push_back(rlegName);
  footStepsList.push_back(AL::ALValue::array(AL::ALValue::array(0.00f, -0.1f, 0.0f)));

  // 4) Sidestep to the left with your left foot
  legNameList.push_back(llegName);
  footStepsList.push_back(AL::ALValue::array(AL::ALValue::array(0.00f, 0.16f, 0.0f)));

  // 5) Step backward & left with your right foot
  legNameList.push_back(rlegName);
  footStepsList.push_back(AL::ALValue::array(AL::ALValue::array(-0.04f, -0.1f, 0.0f)));

  // 6)Step forward & right with your right foot
  legNameList.push_back(rlegName);
  footStepsList.push_back(AL::ALValue::array(AL::ALValue::array(0.00f, -0.16f, 0.0f)));

  // 7) Move your left foot to your right foot
  legNameList.push_back(llegName);
  footStepsList.push_back(AL::ALValue::array(AL::ALValue::array(0.00f, 0.1f, 0.0f)));

  // 8) Sidestep to the right with your right foot
  legNameList.push_back(rlegName);
  footStepsList.push_back(AL::ALValue::array(AL::ALValue::array(0.00f, -0.16f, 0.0f)));

  const std::vector<float> stepFrequency(1, 0.8f);
  const bool clearExisting = false;
  ///////////////////////////////
  // Send Foot step
  ///////////////////////////////
  const unsigned int nbStepDance = 2u; // defined the number of cycle to make

  for (unsigned int j=0; j<nbStepDance; ++j)
  {
    for (unsigned int i=0; i<footStepsList.size(); ++i)
    {
      try
      {
        motionProxy->setFootStepsWithSpeed(
              legNameList.at(i),
              footStepsList.at(i),
              stepFrequency,
              clearExisting);
      }
      catch(const std::exception& e)
      {
        std::cerr << e.what()<< std::endl;
        std::cerr << "This example is not allowed on this robot.\n";
        return;
      }
    }
  }

  motionProxy->waitUntilMoveIsFinished();

  motionProxy->rest();
}


/// <summary>
/// Sets the stiffness to the minimum value.
/// This example is only compatible with NAO.
/// </summary>

void ALMotionExample::stiffnessOff()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();

  // We use the "Body" name to signify the collection of all joints
  const std::string names = "Body";
  float stiffnessLists = 0.0f;
  float timeLists      = 1.0f;

  // the interpolation command will assume that the same value is desired
  // for all joints in the collection "Body"
  motionProxy->stiffnessInterpolation(names, stiffnessLists, timeLists);

  // print motion state
  std::cout << motionProxy->getSummary() << std::endl;
}

/// <summary> Sets the stiffness to the maximum value. </summary>
void ALMotionExample::stiffnessOn()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();

  // We use the "Body" name to signify the collection of all joints
  const std::string names = "Body";
  float stiffnessLists = 1.0f;
  float timeLists      = 1.0f;

  // the interpolation command will assume that the same value is desired
  // for all joints in the collection "Body"
  motionProxy->stiffnessInterpolation(names, stiffnessLists, timeLists);

  // print motion state
  std::cout << motionProxy->getSummary() << std::endl;
}

/// <summary>
/// Moves using the moveToward command and shows control of the arms.
/// This example is only compatible with NAO.
///</summary>
void ALMotionExample::move()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();

  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  // Wake up robot
  motionProxy->wakeUp();

  // Send robot to Stand Init
  postureProxy->goToPosture("StandInit", 0.5f);

  // Enable arm control by Motion algorithm
  motionProxy->setMoveArmsEnabled(true, true);
  // or disable
  // motionProxy->setMoveArmsEnabled(false, false)

  // Enable FOOT CONTACT PROTECTION
  motionProxy->setMotionConfig(AL::ALValue::array(
                           AL::ALValue::array(
                             "ENABLE_FOOT_CONTACT_PROTECTION", true)));
  // or disable
  // motionProxy->setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", false]])
  AL::ALValue moveConfig;

  // set the target velocity (backwards)
  float x     = -0.5f;
  float y     =  0.0f;
  float theta =  0.0f;
  AL::ALValue frequency = AL::ALValue::array("Frequency", 0.0f); // low speed
  moveConfig.arrayPush(frequency);

  motionProxy->moveToward(x, y, theta, moveConfig);
  qi::os::msleep(4000u);

  // set the target velocity (forwards)
  x         = 0.8f;
  y         = 0.0f;
  theta     = 0.0f;
  moveConfig.clear();
  frequency[1]  = 1.0f; // Max speed
  moveConfig.arrayPush(frequency);

  motionProxy->moveToward(x, y, theta, moveConfig);
  qi::os::msleep(4000u);

  // set the target velocity (forwards, right, turn)
  x         =  0.2f;
  y         = -0.5f;
  theta     =  0.2f;

  motionProxy->moveToward(x, y, theta, moveConfig);
  qi::os::msleep(2000u);

  // Now, we will show how to control the arms while
  // walkking.
  //
  // First, deactivate the automatic left arm motion
  motionProxy->setMoveArmsEnabled(false, true);

  // Prepare a trajectory for the joints of the left arm
  AL::ALValue jointNames = AL::ALValue::array(
        "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll");
  AL::ALValue arm1 = AL::ALValue::array(
        -40.0f * AL::Math::TO_RAD,  // "LShoulderPitch"
        +25.0f * AL::Math::TO_RAD,  // "LShoulderRoll"
        +00.0f * AL::Math::TO_RAD,  // "LElbowYaw"
        -40.0f * AL::Math::TO_RAD); // "LElbowRoll"
  AL::ALValue arm2 = AL::ALValue::array(
        -40.0f * AL::Math::TO_RAD,  // "LShoulderPitch"
        +50.0f * AL::Math::TO_RAD,  // "LShoulderRoll"
        +00.0f * AL::Math::TO_RAD,  // "LElbowYaw"
        -80.0f * AL::Math::TO_RAD); // "LElbowRoll"

  // Blocking interpolations using a fraction of max speed
  // These can be stacked up one after the other.
  const float fractionMaxSpeed = 0.6f;
  motionProxy->angleInterpolationWithSpeed(jointNames, arm1, fractionMaxSpeed);
  motionProxy->angleInterpolationWithSpeed(jointNames, arm2, fractionMaxSpeed);
  motionProxy->angleInterpolationWithSpeed(jointNames, arm1, fractionMaxSpeed);

  // reactivate the left arm
  motionProxy->setMoveArmsEnabled(true, true);

  qi::os::msleep(2000u);

  // End Walk by setting a target velocity of zero
  x = 0.0f;
  y = 0.0f;
  theta = 0.0f;
  motionProxy->moveToward(x, y, theta);

  // Go to rest robot
  motionProxy->rest();
}


/// <summary>
/// Move: Small example to make Nao walk
///       with gait customization
/// NAO is Keyser Soze
/// This example is only compatible with NAO.
/// </summary>
void ALMotionExample::moveCustomization()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();

  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  // Wake up robot
  motionProxy->wakeUp();

  // Send robot to Stand Init
  postureProxy->goToPosture("StandInit", 0.5f);

  // set the target velocity (backwards)
  float x         = 1.0f;
  float y         = 0.0f;
  float theta     = 0.0f;

  motionProxy->moveToward(x, y, theta, AL::ALValue::array(
                      AL::ALValue::array("Frequency", 1.0f),
                      // LEFT FOOT
                      AL::ALValue::array("LeftStepHeight", 0.02f),
                      AL::ALValue::array("LeftTorsoWy", 5.0f*AL::Math::TO_RAD),
                      // RIGHT FOOT
                      AL::ALValue::array("RightStepHeight", 0.005f),
                      AL::ALValue::array("RightMaxStepX", 0.001f),
                      AL::ALValue::array("RightMaxStepFrequency", 0.0f),
                      AL::ALValue::array("RightTorsoWx", -7.0f*AL::Math::TO_RAD),
                      AL::ALValue::array("RightTorsoWy", 5.0f*AL::Math::TO_RAD)));

  qi::os::msleep(3000u);

  motionProxy->moveToward(
        x, y, theta,
        AL::ALValue::array(AL::ALValue::array("Frequency", 1.0f)));
  qi::os::msleep(3000u);

  // stop walk in the next double support
  motionProxy->stopMove();

  // Go to rest robot
  motionProxy->rest();
}


/// <summary>
/// Move: Small example to make Nao walk
///       Faster (Step of 6 cm)
/// This example is only compatible with NAO.
/// </summary>
void ALMotionExample::moveFaster()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();

  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  // Wake up robot
  motionProxy->wakeUp();

  // Send robot to Stand Init
  postureProxy->goToPosture("StandInit", 0.5f);

  // Initialize the move process.
  // Check the robot pose and take a right posture.
  // This is blocking called.
  motionProxy->moveInit();

  // set the target velocity (backwards)
  float x         = 1.0f;
  float y         = 0.0f;
  float theta     = 0.0f;
  float frequency = 1.0f;

  // Default walk (MaxStepX = 0.04 m)
  motionProxy->moveToward(
        x, y, theta,
        AL::ALValue::array(AL::ALValue::array("Frequency", frequency)));

  qi::os::msleep(3000u);
  std::cout << "walk speed x: " << motionProxy->getRobotVelocity()[0] << " m/s" << std::endl;

  // Speed walk (MaxStepX = 0.06 m)
  // Could be faster: see walk documentation
  motionProxy->moveToward(x, y, theta, AL::ALValue::array(
                      AL::ALValue::array("Frequency", frequency),
                      AL::ALValue::array("MaxStepX", 0.06f)));
  qi::os::msleep(4000u);
  std::cout << "walk speed x: " << motionProxy->getRobotVelocity()[0] << " m/s" << std::endl;

  // stop walk in the next double support
  motionProxy->stopMove();

  // Go to rest robot
  motionProxy->rest();
}


/// <summary>
/// Nao walks using the moveTo command and shows odometry.
/// This example is only compatible with NAO.
/// </summary>
void ALMotionExample::moveTo()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();

  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  // Wake up robot
  motionProxy->wakeUp();

  // Send robot to Stand Init
  postureProxy->goToPosture("StandInit", 0.5f);

  //// Enable arms control by Motion algorithm
  motionProxy->setMoveArmsEnabled(true, true);
  // or disable
  // motionProxy->setMoveArmsEnabled(false, false)

  // Enable foor contact protection
  motionProxy->setMotionConfig(AL::ALValue::array(
                           AL::ALValue::array("ENABLE_FOOT_CONTACT_PROTECTION", true)));
  // or disable
  //  motionProxy->setMotionConfig(AL::ALValue::array(
  //    AL::ALValue::array("ENABLE_FOOT_CONTACT_PROTECTION", false)));

  // store Nao's position before the walk
  const bool useSensor = false;
  const AL::Math::Pose2D worldToRobotInit =
      AL::Math::Pose2D(motionProxy->getRobotPosition(useSensor));

  const float x     = 0.3f;
  const float y     = 0.1f;
  const float theta = AL::Math::PI/2.0f;
  motionProxy->moveTo(x, y, theta);
  motionProxy->waitUntilMoveIsFinished();

  // store Nao's position after the walk
  const AL::Math::Pose2D worldToRobotAfter =
      AL::Math::Pose2D(motionProxy->getRobotPosition(useSensor));

  // compute Nao's displacement
  AL::Math::Pose2D robotMove =
      AL::Math::pose2DInverse(worldToRobotInit)*worldToRobotAfter;

   // return an angle between ]-PI, PI]
   robotMove.theta = AL::Math::modulo2PI(robotMove.theta);
   std::cout << "Robot Move: " << robotMove << std::endl;

  // Go to rest robot
  motionProxy->rest();
}


/// <summary>
/// Move To: Small example to make Nao Walk To an Objective
///          With customization
/// This example is only compatible with NAO.
/// </summary>
void ALMotionExample::moveToCustomization()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();

  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  // Wake up robot
  motionProxy->wakeUp();

  // Send robot to Stand Init
  postureProxy->goToPosture("StandInit", 0.5f);

  float x     = 0.2f;
  float y     = 0.0f;
  float theta = 0.0f;

  // This example show customization for the both foot
  // with all the possible gait parameters
  motionProxy->moveTo(x, y, theta, AL::ALValue::array(
                  AL::ALValue::array("MaxStepX", 0.02f),         // step of 2 cm in front
                  AL::ALValue::array("MaxStepY", 0.16f),         // default value
                  AL::ALValue::array("MaxStepTheta", 0.4f),      // default value
                  AL::ALValue::array("MaxStepFrequency", 0.0f),  // low frequency
                  AL::ALValue::array("StepHeight", 0.01f),       // step height of 1 cm
                  AL::ALValue::array("TorsoWx", 0.0f),           // default value
                  AL::ALValue::array("TorsoWy", 0.1f)));         // torso bend 0.1 rad in front

  // This example show customization for the both foot
  // with just one gait parameter, in this case, the other
  // parameters are set to the default value
  motionProxy->moveTo(x, y, theta, AL::ALValue::array(
                  AL::ALValue::array("StepHeight", 0.04f))); // step height of 4 cm

  // Go to rest robot
  motionProxy->rest();
}


/// <summary>
/// Move To: Small example to make Nao Walk follow
///          a Dubins Curve
/// This example is only compatible with NAO.
/// </summary>
void ALMotionExample::moveToDubinsCurve()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();

  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  // Wake up robot
  motionProxy->wakeUp();

  // Send robot to Stand Init
  postureProxy->goToPosture("StandInit", 0.5f);

  // first we defined the goal
  const AL::Math::Pose2D goal = AL::Math::Pose2D(0.0f , -0.4f, 0.0f);

  // We get the dubins solution (control points) by
  // calling an almath function
  const float circleRadius = 0.04f;

  // Warning: the circle warning use by dubins curve
  //           have to be 4*CircleRadius < norm(goal)
  const std::vector<AL::Math::Pose2D> dubinsSolutionAbsolute =
      AL::Math::getDubinsSolutions(goal, circleRadius);

  // moveTo With control Points use relative commands but
  // getDubinsSolution return absolute position
  // So, we compute dubinsSolution in relative way
  std::vector<AL::Math::Pose2D> dubinsSolutionRelative;
  dubinsSolutionRelative.push_back(dubinsSolutionAbsolute[0]);

  for (unsigned int i=0; i<dubinsSolutionAbsolute.size()-1; ++i)
  {
    dubinsSolutionRelative.push_back(
          dubinsSolutionAbsolute[i].inverse() *
          dubinsSolutionAbsolute[i+1]);
  }

  // create a vector of moveTo with dubins Control Points
  AL::ALValue moveToTargets;
  for (unsigned int i=0; i<dubinsSolutionRelative.size(); ++i)
  {
    moveToTargets.arrayPush(
          AL::ALValue::array(
            dubinsSolutionRelative.at(i).x,
            dubinsSolutionRelative.at(i).y,
            dubinsSolutionRelative.at(i).theta));
  }

  // Initialized the Walk process and be sure the robot is ready to walk
  // without this call, the first getRobotPosition() will not refer to the position
  // of the robot before the walk process
  motionProxy->moveInit();

  // get robot position before move
  const AL::Math::Pose2D robotPositionBeforeCommand =
      AL::Math::Pose2D(motionProxy->getRobotPosition(false));

  motionProxy->moveTo(moveToTargets);

  // With MoveTo control Points, it's also possible to customize the gait parameters
  // motionProxy->moveTo(
  //       moveToTargets, AL::ALValue::array(
  //         AL::ALValue::array("StepHeight", 0.001f),
  //         AL::ALValue::array("MaxStepX", 0.06f),
  //         AL::ALValue::array("MaxStepFrequency", 1.0f)));

  // get robot position after move
  const AL::Math::Pose2D robotPositionAfterCommand =
      AL::Math::Pose2D(motionProxy->getRobotPosition(false));

  // compute and print the robot motion
  AL::Math::Pose2D robotMoveCommand =
      AL::Math::pose2DInverse(robotPositionBeforeCommand)*
      robotPositionAfterCommand;
  std::cout << "The Robot Move Command: " << robotMoveCommand << std::endl;

  // Go to rest robot
  motionProxy->rest();
}


/// <summary>
/// Whole Body effector control head.
/// Example of a whole body head orientation control
/// This example is only compatible with NAO.
/// </summary>
void ALMotionExample::wbEffectorControlHead()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();
  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  // Wake up robot
  motionProxy->wakeUp();

  // Send robot to Stand Init
  postureProxy->goToPosture("StandInit", 0.5f);

  std::string effectorName = "Head";

  // Active Head tracking.
  bool isEnabled    = true;
  motionProxy->wbEnableEffectorControl(effectorName, isEnabled);

  // Example showing how to set orientation target for Head tracking.
  // The 3 coordinates are absolute head orientation in FRAME_ROBOT.
  // Rotations in radians around x, y and z axis.

  // WX Axis Head Orientation feasible movement = [-20.0, +20.0] degrees
  // WY Axis Head Orientation feasible movement = [-75.0, +70.0] degrees
  // WZ Axis Head Orientation feasible movement = [-30.0, +30.0] degrees
  AL::ALValue targetCoordinateList = AL::ALValue::array(
        AL::ALValue::array(+20.0f * AL::Math::TO_RAD,  00.0f                   ,  00.0f                   ),   // target 0
        AL::ALValue::array(-20.0f * AL::Math::TO_RAD,  00.0f                   ,  00.0f                   ),   // target 1
        AL::ALValue::array( 00.0f                   , +70.0f * AL::Math::TO_RAD,  00.0f                   ),   // target 2
        AL::ALValue::array( 00.0f                   , +70.0f * AL::Math::TO_RAD, +30.0f * AL::Math::TO_RAD),   // target 3
        AL::ALValue::array( 00.0f                   , +70.0f * AL::Math::TO_RAD, -30.0f * AL::Math::TO_RAD),   // target 4
        AL::ALValue::array( 00.0f                   , -75.0f * AL::Math::TO_RAD,  00.0f                   ),   // target 5
        AL::ALValue::array( 00.0f                   , -75.0f * AL::Math::TO_RAD, +30.0f * AL::Math::TO_RAD),   // target 6
        AL::ALValue::array( 00.0f                   , -75.0f * AL::Math::TO_RAD, -30.0f * AL::Math::TO_RAD),   // target 7
        AL::ALValue::array( 00.0f                   ,  00.0f                   ,  00.0f                   ));  // target 8

  // loop along the orientation trajectory
  for (unsigned int i = 0; i < targetCoordinateList.getSize(); ++i)
  {
    // send the command
    motionProxy->wbSetEffectorControl(effectorName, targetCoordinateList[i]);
    // wbSetEffectorControl is a non blocking function, so
    // sleep to allow the head to go to its target.
    // The recommended minimum period between two successives set commands is 0.2 s.
    qi::os::msleep(3000u);
  }

  // Disactivate effector control for the Head
  isEnabled = false;
  motionProxy->wbEnableEffectorControl(effectorName, isEnabled);

  // Go to rest robot
  motionProxy->rest();
}

/// <summary>
/// Whole Body effector control arm.
/// This example is only compatible with NAO.
/// </summary>
void ALMotionExample::wbEffectorControlArm(const std::string& pEffectorName)
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();
  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  // Wake up robot
  motionProxy->wakeUp();

  // Send robot to Stand Init
  postureProxy->goToPosture("StandInit", 0.5f);

  float coef = 1.0f;
  if (pEffectorName == "LArm")
  {
    coef = +1.0f;
  }
  else if (pEffectorName == "RArm")
  {
    coef = -1.0f;
  }
  else
  {
    std::cerr << "Unsupported effector name: " << pEffectorName << std::endl;
    return;
  }

  int  frame      = 2;     // FRAME_ROBOT
  bool useSensors = false; // get the "command" position

  std::vector<float> effectorInit =
      motionProxy->getPosition(pEffectorName, frame, useSensors);

  // Activate effector control for the Left Arm
  bool isEnabled = true;
  motionProxy->wbEnableEffectorControl(pEffectorName, isEnabled);

  // Example showing how to set position target for LArm.
  // The 3 coordinates are absolute LArm position in FRAME_ROBOT.
  // Positions are in meters along the x, y and z axis.
  // X Axis LArm Position feasible movement = [ +0.00, +0.12] meters
  // Y Axis LArm Position feasible movement = [ -0.05, +0.10] meters
  // Z Axis LArm Position feasible movement = [ -0.10, +0.10] meters

  // start with relative coordinates
  AL::ALValue targetCoordinateList = AL::ALValue::array(
        AL::ALValue::array(0.12f, +0.00f*coef, +0.00f),   // target 0
        AL::ALValue::array(0.12f, +0.00f*coef, -0.10f),   // target 1
        AL::ALValue::array(0.12f, +0.05f*coef, -0.10f),   // target 1
        AL::ALValue::array(0.12f, +0.05f*coef, +0.10f),   // target 2
        AL::ALValue::array(0.12f, -0.10f*coef, +0.10f),   // target 3
        AL::ALValue::array(0.12f, -0.10f*coef, -0.10f),   // target 4
        AL::ALValue::array(0.12f, +0.00f*coef, -0.10f),   // target 5
        AL::ALValue::array(0.12f, +0.00f*coef, +0.00f),   // target 6
        AL::ALValue::array(0.00f, +0.00f*coef, +0.00f));  // target 7

  for (unsigned int i = 0; i < targetCoordinateList.getSize(); ++i)
  {
    // loop around the x, y, z
    for (unsigned int c = 0; c < 3; ++c)
    {
      // make the cordinates absolute by adding to the init position
      targetCoordinateList[i][c] =
          static_cast<float>(targetCoordinateList[i][c]) + effectorInit[c];
    }

    // wbSetEffectorControl is a non blocking function
    motionProxy->wbSetEffectorControl(pEffectorName, targetCoordinateList[i]);
    // sleep to allow LArm to go to its target.
    // The recommended minimum period between two successives set commands is 0.2 s.
    qi::os::msleep(4000u);
  }

  // Disactivate effector control.
  isEnabled = false;
  motionProxy->wbEnableEffectorControl(pEffectorName, isEnabled);

  // Go to rest robot
  motionProxy->rest();
}


/// <summary>
/// Whole Body effector control constraint.
/// Balance Constraints
/// This example is only compatible with NAO.
/// </summary>
void ALMotionExample::wbEffectorControlConstraint()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();
  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  // Wake up robot
  motionProxy->wakeUp();

  // Send robot to Stand Init
  postureProxy->goToPosture("StandInit", 0.5f);

  // Activate Whole Body Balancer.
  bool isEnabled  = true;
  motionProxy->wbEnable(isEnabled);

  // Legs are constrained in position
  std::string stateName  = "Fixed"; // Fixed position
  std::string supportLeg = "Legs";  // Both Legs
  motionProxy->wbFootState(stateName, supportLeg);

  // Add a blance constraint. This will keep the center of mass
  // within the support polygon
  motionProxy->wbEnableBalanceConstraint(isEnabled, supportLeg);

  // Now, cause some problems by doing a joint interpolation
  // of the knees, bending them to 40 degrees. Without the
  // constraints added above, Nao would fall down.
  AL::ALValue names      = AL::ALValue::array("LKneePitch", "RKneePitch");
  AL::ALValue angleLists = AL::ALValue::array(
        AL::ALValue::array(0.0f, 40.0f * AL::Math::TO_RAD),   // LKneePitch trajectory
        AL::ALValue::array(0.0f, 40.0f * AL::Math::TO_RAD));  // RKneePitch trajectory

  AL::ALValue timeLists  = AL::ALValue::array(
        AL::ALValue::array(5.0f, 10.0f),   // LKneePitch times
        AL::ALValue::array(5.0f, 10.0f));  // RKneePitch times

  bool isAbsolute = true;  // absolute knee angles
  motionProxy->angleInterpolation(names, angleLists, timeLists, isAbsolute);

  // Disactivate Whole Body Balancer
  isEnabled  = false;
  motionProxy->wbEnable(isEnabled);

  // Go to rest robot
  motionProxy->rest();
}

/// <summary>
/// Whole body constraints to keep the feet on the plane,
/// despite conflicting commands.
/// This example is only compatible with NAO.
/// </summary>
void ALMotionExample::wbFootState()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();
  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  // Wake up robot
  motionProxy->wakeUp();

  // Send robot to Stand Init
  postureProxy->goToPosture("StandInit", 0.5f);

  // Activate Whole Body Balancer
  bool isEnabled  = true;
  motionProxy->wbEnable(isEnabled);

  // Add a constraint to the legs, that allows no vertical movement
  // and keeps the orientation of the feet flat.
  std::string stateName  = "Plane";  // on the plane
  std::string supportLeg = "Legs";   // both legs
  motionProxy->wbFootState(stateName, supportLeg);

  // Now, cause some problems by starting a HipYawPitch angleInterpolation
  // This twists the legs drastically. Without the constraints added above
  // Nao would fall down.
  AL::ALValue names = "LHipYawPitch";
  AL::ALValue angleLists = AL::ALValue::array(
        -45.0f * AL::Math::TO_RAD,
        +10.0f * AL::Math::TO_RAD,
        +00.0f * AL::Math::TO_RAD);

  const AL::ALValue timeLists  = AL::ALValue::array(3.0f, 6.0f, 9.0f);
  const bool isAbsolute = true;  // absolute angles
  motionProxy->angleInterpolation(names, angleLists, timeLists, isAbsolute);

  // Disactivate Whole Body Balancer
  isEnabled  = false;
  motionProxy->wbEnable(isEnabled);

  // Go to rest robot
  motionProxy->rest();
}


AL::ALValue computePath(
    boost::shared_ptr<AL::ALMotionProxy> pMotionProxy,
    const std::string& pEffectorName,
    int pFrame)
{
    const float dx  = 0.05f; // translation axis X (meters)
    const float dz  = 0.05f; // translation axis Z (meters)
    const float dwy = 5.0f*AL::Math::TO_RAD; // rotation axis Y (radian)

    const bool useSensorValues = false;

    const AL::Math::Transform initTf = AL::Math::Transform(
            pMotionProxy->getTransform(pEffectorName, pFrame, useSensorValues));

    const AL::Math::Transform target1Tf =
        initTf*
        AL::Math::Transform(-dx, 0.0, dz)*
        AL::Math::Transform::fromRotY(dwy);

    const AL::Math::Transform target2Tf =
        initTf*
        AL::Math::Transform(dx, 0.0, dz);

    return AL::ALValue::array(target1Tf.toVector(),
                              target2Tf.toVector(),
                              initTf.toVector());
}

/// <summary>
/// Example of a whole body kick
/// This example is only compatible with NAO.
/// </summary>
void ALMotionExample::wbKick()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();
  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  // Wake up robot
  motionProxy->wakeUp();

  // Send robot to Stand Init
  postureProxy->goToPosture("StandInit", 0.5f);

  // Activate Whole Body Balancer.
  bool isEnabled  = true;
  motionProxy->wbEnable(isEnabled);

  // Legs are constrained fixed
  std::string stateName  = "Fixed";
  std::string supportLeg = "Legs";
  motionProxy->wbFootState(stateName, supportLeg);

  // Constraint Balance Motion
  bool isEnable = true;
  supportLeg    = "Legs";
  motionProxy->wbEnableBalanceConstraint(isEnable, supportLeg);

  // Com go to LLeg
  supportLeg = "LLeg";
  float duration = 2.0f;
  motionProxy->wbGoToBalance(supportLeg, duration);

  // RLeg is free
  stateName  = "Free";
  supportLeg = "RLeg";
  motionProxy->wbFootState(stateName, supportLeg);

  // RLeg is optimized
  std::string effectorName = "RLeg";
  int axisMask = 63; // all axis
  int frame    = 1;  // FRAME_WORLD

  // Motion of the RLeg

  AL::ALValue times = AL::ALValue::array(2.0f, 2.7f, 4.5f);

  AL::ALValue path = computePath(motionProxy, effectorName, frame);

  motionProxy->transformInterpolations(
        effectorName, frame, path,
        axisMask, times);

  // Example showing how to Enable Effector Control as an Optimization.
  bool isActive = false;
  motionProxy->wbEnableEffectorOptimization(effectorName, isActive);

  // Com go to LLeg
  supportLeg = "RLeg";
  duration   = 2.0f;
  motionProxy->wbGoToBalance(supportLeg, duration);

  // RLeg is free
  stateName  = "Free";
  supportLeg = "LLeg";
  motionProxy->wbFootState(stateName, supportLeg);

  effectorName = "LLeg";
  path = computePath(motionProxy, effectorName, frame);
  motionProxy->transformInterpolations(
        effectorName, frame, path,
        axisMask, times);

  qi::os::msleep(1000u);

  // Disactivate Head tracking
  isEnabled    = false;
  motionProxy->wbEnable(isEnabled);

  // send robot to rest
  motionProxy->rest();
}


/// <summary>
/// Example of a whole body multiple effectors control "LArm", "RArm" and "Torso"
/// This example is only compatible with NAO.
/// </summary>
void ALMotionExample::wbMultipleEffectors()
{
  boost::shared_ptr<AL::ALMotionProxy> motionProxy = getParentBroker()->getMotionProxy();
  boost::shared_ptr<AL::ALRobotPostureProxy> postureProxy =
      getParentBroker()->getSpecialisedProxy<AL::ALRobotPostureProxy>("ALRobotPosture");

  // Wake up robot
  motionProxy->wakeUp();

  // Send robot to Stand Init
  postureProxy->goToPosture("StandInit", 0.5f);

  // Activate Whole Body Balancer
  bool isEnabled  = true;
  motionProxy->wbEnable(isEnabled);

  // Legs are constrained fixed
  std::string stateName  = "Fixed";
  std::string supportLeg = "Legs";
  motionProxy->wbFootState(stateName, supportLeg);

  // Constraint Balance Motion.
  bool isEnable = true;
  supportLeg    = "Legs";
  motionProxy->wbEnableBalanceConstraint(isEnable, supportLeg);

  // end initialize whole body, define arms motions

  const bool useSensorValues = false;

  AL::ALValue effectorList = AL::ALValue::array("LArm", "RArm");

  int frame = 2; // FRAME_ROBOT

  // pathLArm
  const AL::Math::Transform initLArmTf =
      AL::Math::Transform(motionProxy->getTransform("LArm", frame, useSensorValues));

  AL::Math::Transform targetLArm1Tf = initLArmTf;
  targetLArm1Tf.r2_c4 += 0.08f; // y
  targetLArm1Tf.r3_c4 += 0.14f; // z

  AL::Math::Transform targetLArm2Tf = initLArmTf;
  targetLArm2Tf.r2_c4 -= 0.05f; // y
  targetLArm2Tf.r3_c4 -= 0.07f; // z

  AL::ALValue pathLArm = AL::ALValue::array(
        targetLArm1Tf.toVector(),
        targetLArm2Tf.toVector(),
        targetLArm1Tf.toVector(),
        targetLArm2Tf.toVector(),
        targetLArm1Tf.toVector());

  // pathRArm
  const AL::Math::Transform initRArmTf =
      AL::Math::Transform(motionProxy->getTransform("RArm", frame, useSensorValues));

  AL::Math::Transform targetRArm1Tf = initRArmTf;
  targetRArm1Tf.r2_c4 += 0.05f; // y
  targetRArm1Tf.r3_c4 -= 0.07f; // z

  AL::Math::Transform targetRArm2Tf = initRArmTf;
  targetRArm2Tf.r2_c4 -= 0.08f; // y
  targetRArm2Tf.r3_c4 += 0.14f; // z

  AL::ALValue pathRArm = AL::ALValue::array(
        targetRArm1Tf.toVector(),
        targetRArm2Tf.toVector(),
        targetRArm1Tf.toVector(),
        targetRArm2Tf.toVector(),
        targetRArm1Tf.toVector(),
        targetRArm2Tf.toVector());

  AL::ALValue pathList = AL::ALValue::array(pathLArm, pathRArm);

  AL::ALValue axisMaskList = AL::ALValue::array(
        7,  // translation for "LArm"
        7); // translation for "RArm"

  float k = 1.5f;
  AL::ALValue timesList = AL::ALValue::array(
        AL::ALValue::array(k*1.0f, k*2.0f, k*3.0f, k*4.0f, k*5.0f),
        AL::ALValue::array(k*1.0f, k*2.0f, k*3.0f, k*4.0f, k*5.0f, k*6.0f));

  motionProxy->transformInterpolations(
        effectorList, frame, pathList,
        axisMaskList, timesList);

  effectorList = AL::ALValue::array("Torso", "LArm", "RArm");

  float dy = 0.06f;
  float dz = 0.06f;

  // pathTorso
  const AL::Math::Transform initTorsoTf =
      AL::Math::Transform(motionProxy->getTransform("Torso", frame, useSensorValues));

  AL::Math::Transform targetTorso1Tf = initTorsoTf;
  targetTorso1Tf.r2_c4 += dy;
  targetTorso1Tf.r3_c4 -= dz;

  AL::Math::Transform targetTorso2Tf = initTorsoTf;
  targetTorso2Tf.r2_c4 -= dy;
  targetTorso2Tf.r3_c4 -= dz;

  k = 0.5f;
  AL::ALValue pathTorso;
  AL::ALValue durationTorso;
  unsigned int duration = 1u;
  for (unsigned int i=0; i<3; ++i)
  {
    pathTorso.arrayPush(targetTorso1Tf.toVector());
    durationTorso.arrayPush(k*duration);
    ++duration;

    pathTorso.arrayPush(initTorsoTf.toVector());
    durationTorso.arrayPush(k*duration);
    ++duration;

    pathTorso.arrayPush(targetTorso2Tf.toVector());
    durationTorso.arrayPush(k*duration);
    ++duration;

    pathTorso.arrayPush(initTorsoTf.toVector());
    durationTorso.arrayPush(k*duration);
    ++duration;
  }

  pathList = AL::ALValue::array(
        pathTorso,
        AL::ALValue::array(
          motionProxy->getTransform("LArm", frame, useSensorValues)),
        AL::ALValue::array(
          motionProxy->getTransform("RArm", frame, useSensorValues)));

  axisMaskList = AL::ALValue::array(63, 7, 7);

  timesList  = AL::ALValue::array(
                durationTorso,             // for "Torso" in seconds
                AL::ALValue::array(k*12),  // for "LArm" in seconds
                AL::ALValue::array(k*12)); // for "RArm" in seconds

  motionProxy->transformInterpolations(
        effectorList, frame, pathList,
        axisMaskList, timesList);

  // Disactivate Head tracking.
  isEnabled = false;
  motionProxy->wbEnable(isEnabled);

  // Go to rest robot
  motionProxy->rest();
}
