##################
# FILL IN HEADER
#################

import microbit as mb
import radio  # Needs to be imported separately

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=15, length =100)

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)


# Wait for start message before beginning printing
incoming = ''
while not incoming == 'start':
    incoming = radio.receive(acc_str)
print('start')


while True:
    incoming = radio.receive(acc_str) # Read from radio

    if incoming is not None: # message was received
        mb.display.show(mb.Image.HEART, delay=100, clear=True, wait=False)

        #############################################################
        # FILL IN HERE

        incoming = radio.receive(acc_str)
        print(incoming)
        fout = open("incoming.txt", "w")
        fout.write(incoming)
        incoming1 = radio.recieve(time_str)
        print(incoming1)
        fout1 = open("incoming1.txt", "w")
        fout1.write(incoming1)
        fout.write(incoming1)
        # Need to parse it and reformat as a tuple for the MU plotter
        #############################################################

        mb.sleep(100)