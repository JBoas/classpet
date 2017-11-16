from sense_hat import SenseHat
import time

sense = SenseHat ()

p = (204, 0, 204)
g = (0, 102, 102)
w = (200, 200, 200)
y = (204, 204, 0)
e = (0, 0, 0)

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

pet2 = [
	e, e, e, e, e, e, e, e,
	p, e, e, e, e, e, e, e,
	e, p, e, e, p, e, p, e,
	e, p, g, g, p, y, y, e,
	e, p, g, g, g, y, y, g,
	e, g, g, g, g, y, y, e,
	e, g, e, g, e, g, e, e,
	e, e, e, e, e, e, e, e,
	]
def walking():
	for i in range(10):
		sense.set_pixels(pet1)
		time.sleep(0.5)
		sense.set_pixels(pet2)
		time.sleep(0.5)

sense.clear()

x, y, z = sense.get_accelerometer_raw().values()

while x<2 and y<2 and z<2:
	x, y, z = sense.get_accelerometer_raw().values()
else:
	sens.set_pixels(pet1 + pet2)
	walking()