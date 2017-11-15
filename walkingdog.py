from sense_hat import SenseHat
import time

sense = SenseHat()
G = (0, 255, 0)
Y = (255, 255, 0)
B = (0, 0, 255)
R = (255, 0, 0)
W = (255,255,255)
O = (0,0,0)
P = (255,105, 180)
    
    
    
    
pet1 = [
	O, O, O, O, O, O, O, O,
	P, O, O, O, O, O, O, O,
	O, P, O, O, P, O, P, O,
	O, P, G, G, P, Y, Y, O,
	O, G, G, G, Y, W, Y, G,
	O, G, G, G, G, Y, Y, O,
	O, G, O, G, O, G, O, O,
	O, O, O, O, O, O, O, O,
	]
pet2 = [
	O, O, O, O, O, O, O, O,
	P, O, O, O, O, O, O, O,
	O, P, O, O, P, O, P, O,
	O, P, G, G, P, Y, Y, O,
	O, G, G, G, Y, W, Y, G,
	O, G, G, G, G, Y, Y, O,
	O, O, G, O, G, O, O, O,
	O, O, O, O, O, O, O, O,
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
	walking()
