import cv2 as cv
import numpy as np
import statistics as st

# import tkinter

im = r"HR.tif"
#you can specify your locaion

image = cv.imread(im)
print("Image Dimensions =", image.shape)

bl, gr, rd = cv.split(image)

blue = bl.reshape(1, -1)
red = rd.reshape(1, -1)

print("Pixels = ",red.size)

size = blue.size
# print(blue)
# print(blue.shape)

tempnir = tempr = np.zeros(red.size)

# print(tempr)
for i in range(bl.size):
    calr = ((1.0 * red[0, i]) - (1.012 * blue[0, i]))
    tempr[i] = calr
    # print(cal)

# print(tempr)

RED = st.mean(tempr)
print("RED =", RED)

for i in range(bl.size):
    calnir = ((6.403 * blue[0, i]) - (1.012 * red[0, i]))
    tempnir[i] = calnir
    print(calnir)

NIR = st.mean(tempnir)
print("NIR =", NIR)

def NDVI_Calc(b,r):
	tempndvi = np.zeros(r.size)
	for i in range(b.size):
		den = ((1.00 * b[0,i]) + (0.044 * r[0,i]))
		if (den == 0):
			calndvi = 0
		if (den != 0):
			calndvi = (((1.236 * b[0,i] - 0.188 * r[0,i])) / den)
			#tempndvi[i] = calndvi
	#NDVI = st.mean(tempndvi)
	#print("NDVI =", NDVI)
	#return NDVI

NDVI_Calc(blue,red)
