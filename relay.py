import RPi.GPIO as GPIO
import time

relay1 = 19
relay2 = 13
stat = True

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)

print('Setup has done.')

while(stat):

	ans = input('Please enter stat: ')

	if(ans == 'false' or ans == 'f1'):
		GPIO.output(relay1, True)
		time.sleep(0.1)

	if(ans == 'true' or ans == 't1'):
		GPIO.output(relay1, False)
		time.sleep(0.1)

	if(ans == 'false' or ans == 'f2' or ans == '0'):
		GPIO.output(relay2, True)
		time.sleep(0.1)

	if(ans == 'true' or ans == 't2' or ans == '1'):
		GPIO.output(relay2, False)
		time.sleep(0.1)

	if(ans == 'w'):
		GPIO.output(relay1, True)
		GPIO.output(relay2, True)
		time.sleep(0.1)

	if(ans == 'q'):
		GPIO.output(relay1, False)
		GPIO.output(relay2, False)
		time.sleep(0.1)

	if(ans == 'close' or ans == 'c'):
		stat = False
		break
