# Test of the softTone module in wiringopi
# Plays a scale out on pin 3 - connect pizeo disc to pin 3 & 0v
import wiringopi

PIN = 3

SCALE = [262, 294, 330, 349, 392, 440, 494, 525]

wiringopi.wiringPiSetup()
wiringopi.softToneCreate(PIN)

while True:
    for idx in range(8):
        print(idx)
        wiringopi.softToneWrite(PIN, SCALE[idx])
        wiringopi.delay(500)
