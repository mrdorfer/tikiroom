## Moved from VLC to ffmpeg to lower the overhead so it can run on a raspberry pi zero
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
    os.system("ffplay -nodisp -autoexit "+fullpath+" >/dev/null 2>&1")
    time.sleep(10)
