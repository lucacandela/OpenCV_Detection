import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import findClickPositions


#change working directory to the folder that this script is in
os.chdir(os.path.dirname(os.path.abspath(__file__)))


wincap = WindowCapture('Roblox')


loop_time = time()
while(True):
    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    #cv.imshow("Computer Vision", screenshot)
    findClickPositions('horror_vessel.png', screenshot, 0.21, 'rectangles')

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # Press 'q' with the output window focused to exit
    # waits 1ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

