# importing vlc, os, and random modules
## this relies on the system having ffmpeg to play
## music from cli
##
from gpiozero import MotionSensor
from datetime import datetime 
import os
import time
import random
import path

pir = MotionSensor(4)
musichome="/home/tiki/music/"

while True:
    pir.wait_for_motion()
    randomsong = random.choice(os.listdir(musichome))
    fullpath = (musichome + randomsong)
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    print('blink!')
    print('MOTION DETECTED, NOW PLAYING: ' +fullpath,ts)
    os.system("ffplay -nodisp -autoexit "+fullpath+" >/dev/null 2>&1")
    print('turn off lights')
    time.sleep(10)
