# importing vlc, os, and random modules
## this relies on the system having ffmpeg to play
## music from cli.  Project between https://github.com/calubuddy and myself
##
from gpiozero import MotionSensor
from datetime import datetime 
import os
import time
import random
import path

pir = MotionSensor(4)
musichome="/home/music/"

while True:
    pir.wait_for_motion()
    randomsong = random.choice(os.listdir(musichome))
    fullpath = (musichome + randomsong)
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    print('MOTION DETECTED, NOW PLAYING: ' +fullpath,ts)
    os.system("ffplay -nodisp -autoexit "+fullpath+" >/dev/null 2>&1")
    time.sleep(10)
