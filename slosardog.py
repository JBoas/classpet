from sense_hat import SenseHat
import time

sense = SenseHat ()

p = (204, 0, 204)
g = (0, 102, 102)
w = (200, 200, 200)
y = (204, 204, 0)
e = (0, 0, 0)
r = (255, 0, 0)

pet1 = [
	e, e, e, e, e, e, e, e,
	p, e, e, e, e, e, e, e,
	e, p, e, e, p, e, p, e,
	e, p, g, g, p, y, y, e,
	e, g, g, g, y, w, y, g,
	e, g, g, g, g, y, y, e,
	e, g, e, g, e, g, e, e,
	e, e, e, e, e, e, e, e
	]

red = [
	r, r, r, r, r, r, r, r,
	r, r, r, r, r, r, r, r,
	r, r, r, r, r, r, r, r,
	r, r, r, r, r, r, r, r,
	r, r, r, r, r, r, r, r,
	r, r, r, r, r, r, r, r,
	r, r, r, r, r, r, r, r,
	r, r, r, r, r, r, r, r
	]
def walking():
	for i in range(10):
		sense.set_pixels(pet1)
		time.sleep(0.5)
		sense.set_pixels(pet2)
		time.sleep(0.5)

sense.clear()

while True:
	sense.set_pixels(pet1)
	x,y,z = sense.get_accelerometer_raw().values()
	if(x > 2 or y > 2 or z > 2):
		sense.set_pixels(red)
	time.sleep(1)
