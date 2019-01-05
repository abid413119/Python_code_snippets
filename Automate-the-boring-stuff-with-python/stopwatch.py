#! python3
# stopwatch.py - A simple stopwatch program.

import time

input('Press ENTER to bigin or CTRL-C to quit.')

print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' %(lapNum, totalTime, lapTime), end="")
        lapNum += 1
        lastTime = time.time() 
except KeyboardInterrupt:
    print('\nDone.')