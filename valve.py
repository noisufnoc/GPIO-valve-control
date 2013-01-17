#!/usr/bin/env python

import RPi.GPIO as GPIO

def setup(*valve_id):
    """ Set up all the valves """
    GPIO.setmode(GPIO.BCM)
    for id in valve_id:
        GPIO.setup(id, GPIO.OUT)
        close(id)
        print "I set up valve id %s" % id

def cleanup():
    """ Clean up the GPIO """
    GPIO.cleanup()
    print "All clean!"

def open(valve_id):
    """ Open the specified valve """
    GPIO.output(valve_id, True)
    print "%s Open!" % valve_id

def close(valve_id):
    """ Close the specified valve """
    GPIO.output(valve_id, False)
    print "%s Closed!" % valve_id