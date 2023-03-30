# -*- coding: utf-8 -*-
"""
@author: William Klubinski
"""

import pyautogui
import time
import random

while True:
    
    screenWidth, screenHeight = pyautogui.size()
    x = random.randint(0, screenWidth)
    y = random.randint(0, screenHeight)
    
    duration = random.uniform(1.0, 1.5)
    
    pyautogui.moveTo(x, y, duration=duration, tween=pyautogui.easeInOutQuad)
    
    time.sleep(5)