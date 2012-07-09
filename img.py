#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from SimpleCV import *
import math

def show(img):
	show=img.show()
	raw_input("Press enter to quit.")

img=Image("black.png")


def addlines(img, offset=100):
	a=map(lambda x: int(math.sin(x*1.0/60)*x/1600.0*4+4+1), range(offset,offset+1600))
	displacement=map(lambda x: int(math.sin(x*1.0/200)*40+40+x/50.0), range(offset,offset+1600))
	print displacement

	for x,v in enumerate(a):
		img[x,displacement[x]+offset]=Color.RED
		for cell in xrange(v):
			for pixel in xrange(6):
				img[x,pixel+cell*10+offset+displacement[x]]=Color.WHITE

def addbloom(img):
	imgb=img.copy()
	imgb=imgb.smooth('gaussian', (25,25), 0)
	imgb=imgb.dilate(1)
	
	
	blank=ColorCurve([[0,0], [100, 0], [180, 0], [255, 0]])
	full=ColorCurve([[0,0], [100, 100], [180, 180], [255, 255]])
	c = ColorCurve([[0,0], [100, 30], [180, 60], [255, 100]])
	
	
	imgb = imgb.applyRGBCurve(blank,c,c)
	
	img=img.smooth('gaussian', (3,3), 0)
	img+=imgb
	img+=imgb
	
	imgb=img.copy()
	imgb=imgb.dilate(5)
	imgb=imgb.smooth('gaussian', (455,455), 0)
	
	#c = ColorCurve([[0,0], [100, 70], [180, 100], [255, 128]])
	#img = img.applyRGBCurve(c,c,c)
	
	imgb = imgb.applyRGBCurve(blank,blank,full)
	
	
	img+=imgb
	return img

addlines(img,100)
addlines(img,700)
img=addbloom(img)
show(img)
img.save("output.png")

if __name__=="__main__":
	pass