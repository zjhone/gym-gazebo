
"use strict";

let WheelDropEvent = require('./WheelDropEvent.js');
let ScanAngle = require('./ScanAngle.js');
let Led = require('./Led.js');
let DigitalOutput = require('./DigitalOutput.js');
let BumperEvent = require('./BumperEvent.js');
let ControllerInfo = require('./ControllerInfo.js');
let CliffEvent = require('./CliffEvent.js');
let KeyboardInput = require('./KeyboardInput.js');
let PowerSystemEvent = require('./PowerSystemEvent.js');
let RobotStateEvent = require('./RobotStateEvent.js');
let Sound = require('./Sound.js');
let ButtonEvent = require('./ButtonEvent.js');
let ExternalPower = require('./ExternalPower.js');
let DigitalInputEvent = require('./DigitalInputEvent.js');
let DockInfraRed = require('./DockInfraRed.js');
let SensorState = require('./SensorState.js');
let VersionInfo = require('./VersionInfo.js');
let MotorPower = require('./MotorPower.js');
let AutoDockingActionResult = require('./AutoDockingActionResult.js');
let AutoDockingAction = require('./AutoDockingAction.js');
let AutoDockingActionFeedback = require('./AutoDockingActionFeedback.js');
let AutoDockingResult = require('./AutoDockingResult.js');
let AutoDockingGoal = require('./AutoDockingGoal.js');
let AutoDockingActionGoal = require('./AutoDockingActionGoal.js');
let AutoDockingFeedback = require('./AutoDockingFeedback.js');

module.exports = {
  WheelDropEvent: WheelDropEvent,
  ScanAngle: ScanAngle,
  Led: Led,
  DigitalOutput: DigitalOutput,
  BumperEvent: BumperEvent,
  ControllerInfo: ControllerInfo,
  CliffEvent: CliffEvent,
  KeyboardInput: KeyboardInput,
  PowerSystemEvent: PowerSystemEvent,
  RobotStateEvent: RobotStateEvent,
  Sound: Sound,
  ButtonEvent: ButtonEvent,
  ExternalPower: ExternalPower,
  DigitalInputEvent: DigitalInputEvent,
  DockInfraRed: DockInfraRed,
  SensorState: SensorState,
  VersionInfo: VersionInfo,
  MotorPower: MotorPower,
  AutoDockingActionResult: AutoDockingActionResult,
  AutoDockingAction: AutoDockingAction,
  AutoDockingActionFeedback: AutoDockingActionFeedback,
  AutoDockingResult: AutoDockingResult,
  AutoDockingGoal: AutoDockingGoal,
  AutoDockingActionGoal: AutoDockingActionGoal,
  AutoDockingFeedback: AutoDockingFeedback,
};
