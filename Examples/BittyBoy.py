from microbit import *
import neopixel
import radio
radio.on()
def forward(speed=0.3):
    pin0.write_analog(1023*speed)
    pin1.write_analog(1023*speed)
    pin8.write_digital(0)
    pin12.write_digital(0)
def stop():
    forward(speed=0)
def right(speed=0.5):
    pin0.write_analog(1023*speed)
    pin1.write_analog(1023*(1-speed))
    pin8.write_digital(0)
    pin12.write_digital(1)
def left(speed=0.5):
    pin0.write_analog(1023*(1-speed))
    pin1.write_analog(1023*speed)
    pin8.write_digital(1)
    pin12.write_digital(0)
while True:
    message=radio.receive()
    if message:
        pin14.write_digital(1)
    else:
        pin14.write_digital(0)
    if button_a.is_pressed():
        right()
    elif button_b.is_pressed():
        left()
    else:
        forward()