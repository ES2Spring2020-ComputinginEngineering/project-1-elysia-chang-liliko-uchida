##################
#Project 1 Part 3
#LILIKO UCHIDA & ELYSIA CHANG
#################

#IMPORT STATEMENTS
import microbit as mb
import radio  # Needs to be imported separately


#RADIO SETUP/ PROGRAM START
radio.on()  # Turn on radio
radio.config(channel=15, length=100, queue=7)

print('Program Started')
mb.display.show(mb.Image.HAPPY)


#DATA COLLECTION
while not mb.button_a.is_pressed():  # wait for button A to be pressed to begin logging
    mb.sleep(10)

radio.send('start') # Send the word 'start' to start the receiver
mb.sleep(1000)
mb.display.show(mb.Image.HEART)  # Display Heart while logging


# Read and send accelerometer data repeatedly until button A is pressed again
while not mb.button_a.is_pressed():
    acc_x = mb.accelerometer.get_x()
    acc_y = mb.accelerometer.get_y()
    acc_z = mb.accelerometer.get_z()
    time = mb.running_time()
    incoming_str = str(acc_x) + "," + str(acc_y) +"," + str(acc_z) + "," + str(time)
    radio.send(incoming_str)



    ######################################################

    mb.sleep(10)

    ######################################################

    #TROUBLE SHOOTING
    #P: Channel Interference
    #S: Try changing channel number to team number DONE
    #P: Flat plotter curve
    #S: Increase speed of data collection



mb.display.show(mb.Image.SQUARE)  # Display Square when program ends