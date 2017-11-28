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
K = (1,1,1)    
OR = (226,119,31)    
    
    
pet1 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, R, R, R, R, R, R, O,
        O, R, R, R, R, R, R, O,
        O, K, K, O, K, K, O, O,
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

RED = [
	K, R, R, R, R, R, R, K,
	R, K, R, R, R, R, K, R,
	R, R, K, R, R, K, R, R,
	R, R, R, K, K, R, R, R,
	R, R, R, K, K, R, R, R,
	R, R, K, R, R, K, R, R,
	R, K, R, R, R, R, K, R,
	K, R, R, R, R, R, R, K,
        ]



while True:
	sense.set_pixels(pet1)
	x, y, z = sense.get_accelerometer_raw().values()
	if(x>1 or y>1 or z>1):
		sense.set_pixels(RED)
	time.sleep(1)
sense.clear
