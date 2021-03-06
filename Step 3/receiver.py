##################
# FILL IN HEADER
#################

import microbit as mb
import radio  # Needs to be imported separately

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=15, length =100, queue=7)

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)


# Wait for start message before beginning printing
incoming = ''
while not incoming == 'start':
    incoming = radio.receive()
print('start')


while True:
    incoming = radio.receive() # Read from radio

    if incoming is not None: # message was received
        mb.display.show(mb.Image.HEART, delay=100, clear=True, wait=False)
        s = incoming.split(",")
        n = (int(s[0]), int(s[1]), int(s[2]), int(s[3]))
        print(n)



        #############################################################
        # FILL IN HERE

        # Need to parse it and reformat as a tuple for the MU plotter
        #############################################################

        mb.sleep(5)