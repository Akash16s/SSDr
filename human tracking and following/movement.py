import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT) # right forward
GPIO.setup(18,GPIO.OUT) # right backward
GPIO.setup(22,GPIO.OUT) # left forward
GPIO.setup(23,GPIO.OUT) # left backward
GPIO.setup(24,GPIO.OUT) # Supply right
GPIO.setup(25,GPIO.OUT) # Supply2 left


# these are the paramenters for ideal human image
yCentre = 70                  # y ideal
yHeight = 220                 # y+h
xCentre = 100                # x ideal
xWidth = 230                 # x+w
area = (xCentre - xWidth) * (yCentre - yHeight)   # computing area of the block
centerX = (xCentre + xWidth) / 2      # finding ideal x center
value=20
value2=-20
def moveForward():
    # all forward movement code with high speed
    print("forward")
    GPIO.output(17,True)
    GPIO.output(18,False)
    GPIO.output(22,True)
    GPIO.output(23,False)
    GPIO.PWM(24,100)
    GPIO.PWM(25,100)


def stopMoving():
    # sudden movement stopped
    GPIO.output(17,False)
    GPIO.output(18,False)
    GPIO.output(22,False)
    GPIO.output(23,False)
    GPIO.PWM(24,0)
    GPIO.PWM(25,0)

def moveRight():
    # rightward movement with less speed and curvy path  means left wheel will have higher rotation
    GPIO.output(17,True)
    GPIO.output(18,False)
    GPIO.output(22,True)
    GPIO.output(23,False)
    GPIO.PWM(24,50)
    GPIO.PWM(25,100)
def moveLeft():
    # leftward movement with less speed and curvy path means right wheel will have higher rotation
    GPIO.output(17,True)
    GPIO.output(18,False)
    GPIO.output(22,True)
    GPIO.output(23,False)
    GPIO.PWM(24,100)
    GPIO.PWM(25,50)
def minimiseError(x, y, xw, yh):         # the function for movement decision....based on PID not total
    centerImgX = (x + xw) / 2
    areaImg = (xw - x) * (yh - y)
    if (areaImg < area and abs(centerX-centerImgX)<=value):
        moveForward()
    elif(areaImg>=area):
        stopMoving()
    if(centerX-centerImgX>value):
        moveLeft()
    elif(centerX-centerImgX<value2):
        moveRight()


