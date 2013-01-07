#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
valve_a = 18
valve_b = 23
GPIO.setup(valve_a, GPIO.OUT)
GPIO.setup(valve_b, GPIO.OUT)

GPIO.output(valve_a, True)
GPIO.output(valve_b, False)
time.sleep(19)
GPIO.output(valve_a, False)
GPIO.output(valve_b, True)
