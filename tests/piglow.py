import wiringopi
io = wiringopi.GPIO(wiringopi.GPIO.WPI_MODE_PINS)
io.piGlowSetup()
io.piGlowLeg(1,100)
