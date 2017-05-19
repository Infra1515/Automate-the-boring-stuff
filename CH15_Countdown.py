#! python3

# Chapter 15 Project Simple Countdown Program

import time
import subprocess


timeLeft = 60

while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft = timeLeft -1

subprocess.Popen(['start', '/home/infra/Music/wakeup.mp3'], shell=True)
