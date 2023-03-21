import wiringopi
INPUT = 0
OUTPUT = 1
LOW = 0
HIGH = 1
BUTTONS = [13,12,10,11]
LEDS = [0,1,2,3,4,5,6,7,8,9]
PUD_UP = 2

wiringopi.wiringPiSetup()

for button in BUTTONS:
	wiringopi.pinMode(button,INPUT)
	wiringopi.pullUpDnControl(button,PUD_UP)

for led in LEDS:
	wiringopi.pinMode(led,OUTPUT)

while 1:
	for index,button in enumerate(BUTTONS):
		button_state = wiringopi.digitalRead(button)
		first_led = LEDS[index*2]
		second_led = LEDS[(index*2)+1]
		#print str(button) + ' ' + str(button_state)
		wiringopi.digitalWrite(first_led,1-button_state)
		wiringopi.digitalWrite(second_led,1-button_state)
	wiringopi.delay(20)
