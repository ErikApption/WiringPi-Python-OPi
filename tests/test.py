import wiringopi
io = wiringopi.GPIO(wiringopi.GPIO.WPI_MODE_PINS)
print io.digitalRead(1)
print io.analogRead(1)
