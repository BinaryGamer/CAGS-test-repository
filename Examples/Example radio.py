from microbit import *
import radio
radio.config(length=64, queue=1)
radio.on()
def t(f, b, l, r):
    s="bot:{}:{}:{},{}".format(f, b, l, r)
    radio.send(s)
z=0
x=0
ALPHA=0.9
while True:
    z=accelerometer.get_z()
    x=accelerometer.get_x()
    forward=0
    back=0
    left=1
    right=1
    if z>0:
        if z > 1023:
            z=1023
        back=z        
    elif z<0:
        z=abs(z)
        if z > 1023:
            z=1023
        forward=z
    if x>0:
        if x > 1023:
            x=1023
        right=x/1023
        right=1-right
    elif x<0:
        x=abs(x)
        if x > 1023:
            x=1023
        left=x/1023
        left=1-left
    print((forward, back, left, right))
    sleep(50)
    t(forward, back, left, right)