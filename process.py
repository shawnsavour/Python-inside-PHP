#!/usr/bin/env python
import sys
import cv2
from os.path import isfile, join
import os
def removefile(removepaths):
    for removepath in removepaths:
        files=[f for f in os.listdir(removepath) if isfile(join(removepath,f))]
        for i in range (len(files)):
            filename=removepath+files[i]
            os.remove(filename)

def process():
    files=[f for f in os.listdir(pathIn) if isfile(join(pathIn,f))]
    print('upload/' + files[0])
    image = cv2.imread('uploads/123g.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('outputs/output.jpg', gray)
    removefile('uploads/')
    print('removedone')

pathIn = 'uploads/'
process()
print('removeevr')
# print(sys.argv[1])