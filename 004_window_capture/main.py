import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision


#change working directory to the folder that this script is in
os.chdir(os.path.dirname(os.path.abspath(__file__)))

'''
wincap = WindowCapture('Roblox')
# initialize Vision class
vision_horror_vessel = Vision('horror_vessel.png')
'''

wincap = WindowCapture()
vision_LCBG = Vision('LCBG.jpg')


loop_time = time()
while(True):
    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    #cv.imshow("Computer Vision", screenshot)
    #points = vision_horror_vessel.find(screenshot, 0.21, 'rectangles')

    points = vision_LCBG.find(screenshot,0.7,'points')

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # Press 'q' with the output window focused to exit
    # waits 1ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

