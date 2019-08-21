import math
#size of the simulation
frame_end = 20000
#parameters of the path to follow
cir_x = 400
cir_y = 400
#Parameters of the camera
heigth = 5
rot_x = 76 * math.pi / 180 # <90 camera goes down
rot_y = 0 * math.pi / 180
rot_z = 180 * math.pi / 180	
#parameters of the sea
size = 0.1
spatial_size = 10000
depth = 1000
resolution = 15
choppiness = [0.9, 0.2, 0.3]
wave_scale = [7, 3, 10, 11]
wave_scale_min = 0.01
wind_velocity = [30, 50, 70]
wave_alignment = 3
random_seed = [145, 184, 254, 174, 178, 115, 185, 171, 196]
#for the render
RENDER = True
samples_render = 135 #135
FRAME_INTERVAL = 12  
START_FRAME = 0
END_FRAME = 4800
resolution_x = 96
resolution_y = 54
#for file make prosess
version = "test_4_"
