from microbit import *
import radio
radio.config(length=64, queue=1)
radio.on()
while True:
    message=radio.receive()
    if message:
        #Splits message into list of individual messages
        message = message.split(':')
        #Check if message is intended for the Bit:Bot
        if message[0] == "bot":
            #assigning the individual messages variables
            forward=int(message[1])
            backward=int(message[2])
            horizontal=message[3]
            horn=message[4]
            horizontal=horizontal.split(',')
            straight=forward-backward
            if horn=='True':
                #activates horn
                pin14.write_digital(1)
            else:
                #Deactivates horn
                pin14.write_digital(0)
            if straight>=0:
                #Going Forward
                pin0.write_analog(forward*float(horizontal[0]))
                pin1.write_analog(forward*float(horizontal[1]))
                pin8.write_digital(0)
                pin12.write_digital(0)
            else:
                #Going Straight
                pin0.write_analog(1023-(backward*float(horizontal[0])))
                pin1.write_analog(1023-(backward*float(horizontal[1])))
                pin8.write_digital(1)
                pin12.write_digital(1)