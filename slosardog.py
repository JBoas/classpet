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

def animate(sense,slides,timeToSleep):
	for slide in slides:
		sense.set_pixels(slide)
		time.sleep(timeToSleep)

entertain =[
        [
	g, g, e, e, e, e, g, g,
	g, e, e, l, l, e, g, g,
	g, e, l, w, l, w, g, g,
	g, e, l, l, l, l, g, g,
	g, b, r, y, y, r, g, g,
	b, o, b, b, b, g, b, g,
	o, l, r, r, r, l, g, g,
	o, o, b, o, g, b, g, g
	],[
	g, g, g, e, e, e, e, g,
	g, g, e, e, l, l, e, g,
	g, g, e, l, w, l, w, g,
	g, g, e, l, l, l, l, g,
	g, g, b, r, y, y, r, g,
	g, b, o, b, b, b, g, b,
	g, o, l, r, r, r, l, g,
	g, o, o, b, o, g, b, g
        ],[
	g, g, g, g, e, e, e, e,
	g, g, g, e, e, l, l, e,
	g, g, g, e, l, w, l, w,
	g, g, g, e, l, l, l, l,
	g, g, g, b, r, y, y, r,
	g, g, b, o, b, b, b, g,
	g, g, o, l, r, r, r, l,
	g, g, o, o, b, o, g, b
	],[
	g, g, g, g, g, e, e, e,
        g, g, g, g, e, g, l, l,
        g, g, g, g, e, l, w, l,
        g, g, g, g, e, l, l, l,
        g, g, g, g, b, r, y, y,
        g, g, g, b, o, b, b, b,
        g, g, g, o, l, r, r, r,
        g, g, g, o, o, b, o, g
	],[
	g, g, g, g, g, g, e, e,
        g, g, g, g, g, e, g, l,
        g, g, g, g, g, e, l, w,
        g, g, g, g, g, e, l, l,
        g, g, g, g, g, b, r, y,
        g, g, g, g, b, o, b, b,
        g, g, g, g, o, l, l, r,
        g, g, g, g, o, o, b, o
	],[
	g, g, g, g, g, g, e, e,
        g, g, g, g, g, e, g, l,
        g, g, g, g, g, e, l, w,
        g, g, g, g, g, e, l, l,
        g, g, g, g, g, b, r, y,
        g, g, g, g, b, o, b, b,
        g, g, g, g, o, l, l, r,
        g, g, g, g, o, o, b, o
	],[
	g, g, g, g, g, g, g, e,
        g, g, g, g, g, g, e, g,
        g, g, g, g, g, g, e, l,
        g, g, g, g, g, g, e, l,
        g, g, g, g, g, g, b, r,
        g, g, g, g, g, b, o, b,
        g, g, g, g, g, o, l, l,
        g, g, g, g, g, o, o, b
	],[
	g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, e,
        g, g, g, g, g, g, g, e,
        g, g, g, g, g, g, g, e,
        g, g, g, g, g, g, g, b,
        g, g, g, g, g, g, b, o,
        g, g, g, g, g, g, o, l,
        g, g, g, g, g, g, o, o
	],[
	g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, b,
        g, g, g, g, g, g, g, o,
        g, g, g, g, g, g, g, o
	],[
	g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g
	],[
	g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, e, e, e, e, g, g
	],[
	g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, e, e, e, e, g, g,
        g, e, e, l, l, e, g, g
	],[
	g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, e, e, e, e, g, g,
        g, e, e, l, l, e, g, g,
        g, e, l, w, l, w, g, g
	],[
	g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, e, e, e, e, g, g,
        g, e, e, l, l, e, g, g,
        g, e, l, w, l, w, g, g,
        g, e, l, l, l, l, g, g
	],[
	g, g, g, g, g, g, g, g,
	g, g, g, g, g, g, g, g,
	g, g, g, g, g, g, g, g,
	g, g, e, e, e, e, g, g,
        g, e, e, l, l, e, g, g,
        g, e, l, w, l, w, g, g,
        g, e, l, l, l, l, g, g,
        g, b, r, y, y, r, g, g,
        ],[
	g, g, g, g, g, g, g, g,
	g, g, g, g, g, g, g, g, 
	g, g, e, e, e, e, g, g,
        g, e, e, l, l, e, g, g,
        g, e, l, w, l, w, g, g,
        g, e, l, l, l, l, g, g,
        g, b, r, y, y, r, g, g,
	b, o, b, b, b, g, b, g
        ],[
	g, g, g, g, g, g, g, g,
	g, g, e, e, e, e, g, g,
        g, e, e, l, l, e, g, g,
        g, e, l, w, l, w, g, g,
        g, e, l, l, l, l, g, g,
        g, b, r, y, y, r, g, g,
        b, o, b, b, b, g, b, g,
        o, l, r, r, r, l, g, g,
        ],[
	g, g, e, e, e, e, g, g,
        g, e, e, l, l, e, g, g,
        g, e, l, w, l, w, g, g,
        g, e, l, l, l, l, g, g,
        g, b, r, y, y, r, g, g,
        b, o, b, b, b, g, b, g,
        o, l, r, r, r, l, g, g,
        o, o, b, o, g, b, g, g
	],[
	g, g, e, e, e, e, g, g,
        g, g, e, l, l, e, e, g,
        g, g, w, l, w, l, e, g,
        g, g, l, l, l, l, e, g,
        g, g, r, y, y, r, b, g,
        g, g, g, b, b, b, o, b,
        g, g, l, r, r, r, l, g,
        g, g, b, g, o, b, o, g
	],[
	g, g, g, e, e, e, e, g,
	g, g, g, e, l, l, e, e,
	g, g, g, w, l, w, l, e,
	g, g, g, l, l, l, l, e,
	g, g, g, r, y, y, r, b,
	g, g, g, g, b, b, b, o,
	g, g, g, l, r, r, r, l,
	g, g, g, b, g, o, b, o
	],[
	g, g, g, e, e, e, e, g,
        g, g, g, e, l, l, e, e,
        g, g, g, w, l, w, l, e,
        g, g, g, l, l, l, l, e,
        g, g, g, r, y, y, r, b,
        g, g, g, g, b, b, b, o,
        g, g, g, l, r, r, r, l,
        g, g, g, b, g, o, b, o





]

def walking():
	for i in range(10):
		sense.set_pixels(pet1)
		time.sleep(0.5)
		sense.set_pixels(pet2)
		time.sleep(0.5)

sense.clear()

while True:
	sense.set_pixels(entertain[0])
	x,y,z = sense.get_accelerometer_raw().values()
	if(x > 2 or y > 2 or z > 2):
		animate(sense,entertain,0.5)
	time.sleep(1)
