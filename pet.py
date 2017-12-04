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
K = (0,0,51)    
OR = (226,119,31)    
W = (102,51,0)    
LW = (255,128,0)    
M = (255,228,181)



pet1 = [
        O, O, LW, LW, LW, LW, O, O,
        O, LW, O, LW, Y, LW, Y, O,
        O, O, O, LW, LW, LW, LW, B,
        O, O, O, LW, W, W, O, O,
        O, O, O, LW, LW, LW, LW, O,
        O, LW, LW, W, LW, LW, O, O,
        LW, LW, W, W, LW, W, O, O,
        LW, LW, LW, W, LW, W, O, O,
        ]


	        

entertain = [	
		[
		O, O, LW, LW, LW, LW, O, O,
		O, LW, O, LW, Y, LW, Y, O,
		O, O, O, LW, LW, LW, LW, B,
		LW, O, O, LW, W, W, O, O,
		LW, O, O, LW, LW, LW, LW, O,
		O, LW, LW, W, LW, LW, O, O,
		LW, LW, W, W, LW, W, O, O,
		LW, LW, LW, W, LW, W, O, O,
		], 
		[
		O, O, LW, LW, LW, LW, O, O,
                O, LW, O, LW, Y, LW, Y, O,
                O, O, O, LW, LW, LW, LW, B,
                O, LW, O, LW, W, W, O, O,
                LW, O, O, LW, LW, LW, LW, O,
                O, LW, LW, W, LW, LW, O, O,
                LW, LW, W, W, LW, W, O, O,
                LW, LW, LW, W, LW, W, O, O,
		]
	]

while True:
	sense.set_pixels(pet1)
	x, y, z = sense.get_accelerometer_raw().values()
	if(x>1 or y>1 or z>1):
		for a in range(5):
			sense.set_pixels(entertain[0])
			time.sleep(1)
			sense.set_pixels(entertain[1])
			time.sleep(1)
sense.clear
