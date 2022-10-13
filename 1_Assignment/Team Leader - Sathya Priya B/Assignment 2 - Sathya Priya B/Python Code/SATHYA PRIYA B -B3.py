import RPi.GPIO as GPIO
import time

GIPO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
                 
GPIO.setup(40,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)

while True:

#Blinking LED
        
       GPIO.output(40,True)
       time.sleep(0.5)
        GPIO.output(40,False)
       time.sleep(0.5)

#Traffic Light
       
       GPIO.output(38,True)      # Red LED
       time.sleep(2)
       GPIO.output(38,False)
       time.sleep(1)
       GPIO.output(36,True)     # Yellow LED
       time.sleep(1)
       GPIO.output(36,False)
       time.sleep(1)
       GPIO.output(32,True)    # Green LED
       time.sleep(2)
       GPIO.output(32,False)
       time.sleep(1)
       
