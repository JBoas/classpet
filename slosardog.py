from sense_hat import SenseHat
import time

sense = SenseHat ()

p = (204, 0, 204)
g = (102, 255, 102)
w = (255, 255, 255)
y = (255, 255, 0)
e = (32, 32, 32)
r = (255, 0, 0)
o = (255, 128,0)
b = (51, 51, 255)
l = (255, 178, 102)

pet1 = [
	g, g, e, e, e, e, g, g,
	g, e, e, l, l, e, g, g,
	g, e, l, w, l, w, g, g,
	g, e, l, l, l, l, g, g,
	g, b, r, y, y, r, g, g,
	b, o, b, b, b, g, b, g,
	o, l, r, r, r, l, g, g,
	o, o, b, o, g, b, g, g
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
