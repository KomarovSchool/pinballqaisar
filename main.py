#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

LEFT_MOTOR_PORT = Port.B
RIGHT_MOTOR_PORT = Port.C

LEFT_TOUCH_PORT = Port.S1
RIGHT_TOUCH_PORT = Port.S4


left_motor = Motor(LEFT_MOTOR_PORT)
right_motor = Motor(RIGHT_MOTOR_PORT)

left_button = TouchSensor(LEFT_TOUCH_PORT)
right_button = TouchSensor(RIGHT_TOUCH_PORT)

left_motor.run_until_stalled(-300, then=Stop.BRAKE, duty_limit=20)
right_motor.run_until_stalled(-300, then=Stop.BRAKE, duty_limit=20)
left_motor.reset_angle(0)
right_motor.reset_angle(0)


left_motor.track_target(240)
right_motor.track_target(240)

SPEED = 1000


while True:
    if left_button.pressed():
        left_motor.track_target(150)
    else:
        left_motor.track_target(240)
    
    if right_button.pressed():
        right_motor.track_target(150)
    else:
        right_motor.track_target(240)

