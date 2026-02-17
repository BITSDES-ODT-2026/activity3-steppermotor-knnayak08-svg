from machine import Pin
import time

in1 = Pin(13,Pin.OUT)
in2 = Pin(14,Pin.OUT)
in3 = Pin(15,Pin.OUT)
in4 = Pin(19,Pin.OUT)

while True:
    in1.value(1)
    in2.value(0)
    in3.value(0)
    in4.value(0)
    time.sleep(0.005)
    in1.value(0)
    in2.value(1)
    in3.value(0)
    in4.value(0)
    time.sleep(0.005)
    in1.value(0)
    in2.value(0)
    in3.value(1)
    in4.value(0)
    time.sleep(0.005)
    in1.value(0)
    in2.value(0)
    in3.value(0)
    in4.value(1)
    time.sleep(0.005)

Stepmotor - rotating clockwise and anticlockwise (Anti-clockwise is not working)
from machine import Pin
import time

in1 = Pin(13,Pin.OUT)
in2 = Pin(14,Pin.OUT)
in3 = Pin(15,Pin.OUT)
in4 = Pin(19,Pin.OUT)
steps = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
r_di = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]
while True:
    for k in range(500):
        for i in steps:
            in1.value(i[0])
            in2.value(i[1])
            in3.value(i[2])
            in4.value(i[3])
            time.sleep(0.005)
    
    for x in range(500):
        for s in r_di:
            in1.value(s[0])
            in2.value(s[1])
            in3.value(s[2])
            in4.value(s[3])
            time.sleep(0.005)
