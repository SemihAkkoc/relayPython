from gpiozero import LED
from time import sleep

pin = 19
pin2 = 13
relay = LED(pin)
relay2 = LED(pin2)
sleep(0.1)

while(True):
    inp = input("Enter stat: ")
    if (inp == '0'):
    	relay.on()
    if (inp == '1'):
    	relay.off(
    if (inp == '2'):
        relay.on()
    if (inp == '3'):
        relay.off()
    if (inp == 'c'):
    	break
