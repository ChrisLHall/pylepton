import RPi.GPIO as GPIO
import time

SPEED = 60

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
left = GPIO.PWM(21,100)
right = GPIO.PWM(26,100)
left.start(0)
right.start(0)
GPIO.output(20, 0)
GPIO.output(19, 0)

def TurnLeft():
  print "Turning left"
  left.ChangeDutyCycle(SPEED)
  right.ChangeDutyCycle(SPEED)
  GPIO.output(20, 1)
  GPIO.output(19, 1)

def TurnRight():
  print "Turning right"
  left.ChangeDutyCycle(SPEED)
  right.ChangeDutyCycle(SPEED)
  GPIO.output(20, 0)
  GPIO.output(19, 0)

def MoveForward():
  print "Moving forward"
  left.ChangeDutyCycle(SPEED)
  right.ChangeDutyCycle(SPEED)
  GPIO.output(20, 1)
  GPIO.output(19, 0)

def MoveBackward():
  print "Why are you trying to move backward? >:("

def Stop():
  left.ChangeDutyCycle(0)
  right.ChangeDutyCycle(0)
  GPIO.output(20, 1)
  GPIO.output(19, 1)
  pass

def Cleanup():
  pass

if __name__ == "__main__":
  #Do this stuff if running movement.py directly from the command line
  pass
