#!/usr/bin/env python

import os
import time
import subprocess

def cpuGetTemp():
    temp = subprocess.check_output("cat /sys/class/thermal/thermal_zone0/temp", shell=True)
    currentTime=time.strftime('%x %X %Z')
    return[currentTime, temp]
    
print cpuGetTemp()







"""cmd_linux = "cat /sys/class/thermal/thermal_zone0/temp"
cmd_linux1 = "date"

output = subprocess.check_output(cmd_linux, shell=True)
output1 = subprocess.check_output(cmd_linux1, shell=True)

currentTime=time.strftime('%x %X %Z')

file = open('/home/pi/Documents/EL/ELSpring2018/code/temps.csv', 'a')

num_lines = sum(1 for line in open('/home/pi/Documents/EL/ELSpring2018/code/temps.csv'))

if(num_lines < 1):
    file.write("\"Date_Time\", \"Temp\"\n")
    
file.write(output1[:len(output1)-2] + ",")
file.write(output[:5] + "\n")

file.close()"""