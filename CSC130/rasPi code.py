#Import RPi.GPIO
import RPi.GPIO as GPIO
from time import sleep


#specify the naming convention
GPIO.setmode(GPIO.BCM)      #set pin mode

GPIO.setup(17, GPIO.OUT)    #set output pin as pin 17#Morse Code Functions


def s():                    #S in morse code
    i = 0
    for i in range(0,2):
        GPIO.output(17, 1)
        sleep(0.5)
        GPIO.output(17, 0)
        sleep(0.5)
        i = i + 1

def o():                    #O in morse code
    i = 0
    for i in range(0,2):
        GPIO.output(17, 1)
        sleep(1)
        GPIO.output(17, 0)
        sleep(1)
        i = i + 1

# # # # # # # # # # # # # # # # # # MAIN # # # # # # # # # # # # # # # # # # # # # #
while (True):
    s = s()
    o = o()
    s = s()
    sleep(2)