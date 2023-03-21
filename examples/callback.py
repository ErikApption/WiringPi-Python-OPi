import wiringopi
PIN_TO_SENSE = 23

def gpio_callback():
    print "GPIO_CALLBACK!"

wiringopi.wiringPiSetupGpio()
wiringopi.pinMode(PIN_TO_SENSE, wiringopi.GPIO.INPUT)
wiringopi.pullUpDnControl(PIN_TO_SENSE, wiringopi.GPIO.PUD_UP)

wiringopi.wiringPiISR(PIN_TO_SENSE, wiringopi.GPIO.INT_EDGE_BOTH, gpio_callback)

while True:
    wiringopi.delay(2000)
