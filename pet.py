
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


def animate(sense,slides,timetosleep):
	for slide in slides:
		sense.set_pixels(slide)
		time.sleep(timetosleep)

pet1 = [
        O, O, LW, LW, LW, LW, O, O,
        O, LW, O, LW, Y, LW, Y, O,
        O, O, O, LW, LW, LW, LW, W,
        O, O, O, LW, W, W, O, O,
        O, O, O, LW, LW, LW, LW, O,
        O, LW, LW, W, LW, LW, O, O,
        LW, LW, W, W, LW, W, O, O,
        LW, LW, LW, W, LW, W, O, O
        ]

eating = [
		[
		LW, LW, LW, W, W, LW, O, O,
		LW, LW, W, LW, LW, LW, LW, O,
		LW, W, LW, W, Y, LW, O, O,
		LW, O, LW, W, LW, O, O, O,
		LW, O, O, LW, LW, O, O, O,
		W, O, O, LW, W, O, O, O,
		LW, W, B, W, W, B, O, O,
		LW, LW, B, B, B, B, O, O,
		],
		[
		LW, LW, LW, W, W, LW, O, O,
		LW, LW, W, LW, LW, LW, LW, O,
		LW, W, LW, W, Y, LW, O, O,
		LW, O, LW, W, LW, O, O, O,
		LW, O, W, P, LW, O, O, O,
		W, O, LW, P, W, O, O, O,
		LW, W, B, P, W, B, O, O,
		LW, LW, B, B, B, B, O, O,
		],
		[
		LW, LW, LW, W, W, LW, O, O,
		LW, LW, W, LW, LW, LW, LW, O,
		LW, W, LW, W, Y, LW, O, O,
		LW, O, LW, W, LW, O, O, O,
		LW, O, W, W, LW, O, O, O,
		W, O, O, LW, W, O, O, O,
		LW, W, B, O, O, B, O, O,
		LW, LW, B, B, B, B, O, O,
		]
	]

entertain = [	
		[
		O, O, LW, LW, LW, LW, O, O,
		O, LW, O, LW, Y, LW, Y, O,
		O, O, O, LW, LW, LW, LW, W,
		LW, O, O, LW, W, W, O, O,
		LW, O, O, LW, LW, LW, LW, O,
		O, LW, LW, W, LW, LW, O, O,
		LW, LW, W, W, LW, W, O, O,
		LW, LW, LW, W, LW, W, O, O,
		], 
		[             
		O, O, LW, LW, LW, LW, O, O,
                O, LW, O, LW, Y, LW, Y, O,
                O, O, O, LW, LW, LW, LW, W,
                O, LW, O, LW, W, W, P, P,
                LW, O, O, LW, LW, LW, LW, P,
                O, LW, LW, W, LW, LW, O, O,
                LW, LW, W, W, LW, W, O, O,
                LW, LW, LW, W, LW, W, O, O,
		],
		O, O, LW, LW, LW, LW, O, O,
		O, LW, O, LW, Y, LW, Y, O,
		O, O, O, LW, LW, LW, LW, W,
		LW, O, O, LW, W, W, O, O,
		LW, O, O, LW, LW, LW, LW, O,
		O, LW, LW, W, LW, LW, O, O,
		LW, LW, W, W, LW, W, O, O,
		LW, LW, LW, W, LW, W, O, O,
		]
	]


while True:
	sense.set_pixels(pet1)
	x, y, z = sense.get_accelerometer_raw().values()
	if(x>1.5 or y>1.5 or z>1.5):
		for a in range(5):
			animate(sense,entertain,1)
sense.clear
