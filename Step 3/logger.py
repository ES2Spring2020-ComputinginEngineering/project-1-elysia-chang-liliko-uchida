##################
#Project 1 Part 3
#LILIKO UCHIDA & ELYSIA CHANG
#################

import microbit as mb
import radio  # Needs to be imported separately

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=15, length=100)

print('Program Started')
mb.display.show(mb.Image.HAPPY)

while not mb.button_a.is_pressed():  # wait for button A to be pressed to begin logging
    mb.sleep(10)

radio.send('start') # Send the word 'start' to start the receiver
mb.sleep(1000)
mb.display.show(mb.Image.HEART)  # Display Heart while logging


# Read and send accelerometer data repeatedly until button A is pressed again
while not mb.button_a.is_pressed():
    ######################################################
    acc_x = mb.accelerometer.get_x()
    acc_y = mb.accelerometer.get_y()
    acc_z = mb.accelerometer.get_z()
    acc_list = [acc_x, acc_y, acc_z]
    acc_str = str(acc_x) + "," + str(acc_y) +"," + str(acc_z)
    radio.send(acc_str)
    time = microbit.running_time()
    str(time)
    time_str = str(time)
    radio.send(time_str)


    ######################################################

    mb.sleep(100)



mb.display.show(mb.Image.SQUARE)  # Display Square when program ends