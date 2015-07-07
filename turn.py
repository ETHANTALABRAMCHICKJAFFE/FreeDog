import os
from time import sleep
import RPi.GPIO as GPIO

left_motor = 23
right_motor = 24
left_command_audio = "randomfile"
right_command_audio = "randomfile2"
def setup():
    GPIO.setmode(GPIO.BCM)  # setup pin number references
    GPIO.setup(left_motor, GPIO.OUT)
    GPIO.setup(right_motor, GPIO.OUT)

def play_audio(filename):
    os.system('mpg123 -q ' + filename + '&') # you must install mpg123 in order for this to work

def turn_motor_on(pin_number):
    GPIO.output(pin_number, GPIO.HIGH)

def turn_motor_off(pin_number):
    GPIO.output(pin_number, GPIO.LOW)

def turn(direction="left"):
    if direction is "left":
        play_audio(left_command_audio)
        sleep(1.5)
        turn_motor_on(left_motor)
        sleep(1)
        turn_motor_off(left_motor)
    else:
        play_audio(right_command_audio)
        sleep(1.5)
        turn_motor_on(right_motor)
        sleep(1)
        turn_motor_off(left_motor)
