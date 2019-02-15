from microbit import *
import radio
radio.config(length=64, queue=1)
radio.on()
while True:
    message=radio.receive()
    if message:
        message = message.split(':')
        if message[0] == "bot":
            forward=int(message[1])
            backward=int(message[2])
            horizontal=message[3]
            horizontal=horizontal.split(',')
            straight=forward-backward
            if straight>=0:
                pin0.write_analog(forward*float(horizontal[0]))
                pin1.write_analog(forward*float(horizontal[1]))
                pin8.write_digital(0)
                pin12.write_digital(0)
            else:
                pin0.write_analog(1023-(backward*float(horizontal[0])))
                pin1.write_analog(1023-(backward*float(horizontal[1])))
                pin8.write_digital(1)
                pin12.write_digital(1)