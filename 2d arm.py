from encoder import Motor, Count
import time
from machine import PWM, Pin

ANGLE_NORMALIZATION = 500

def degree2servo(angle):
    # assume angle between 0 and 180
    angle = max(0, min(180, angle))
    ms_pulse = angle / 90 + 0.5
    duty = ms_pulse / 20 * 65535
    return int(duty)

Motor1 = Motor(12,13, 25,26)
Motor2 = Motor(14,27, 21,22)

first = PWM(Pin(19),freq=50)
second = PWM(Pin(18),freq=50)
first.duty_u16(degree2servo(90))
second.duty_u16(degree2servo(90))

while True:
    count1 = Motor1.pos() or 0
    count2 = Motor2.pos() or 0
    angle1 = (count1 + 250)  / ANGLE_NORMALIZATION * 180
    angle2 = (count2 + 250) / ANGLE_NORMALIZATION * 180 
    print("angle 1: %d, angle 2: %d" % (angle1, angle2))
    first.duty_u16(degree2servo(angle1))
    second.duty_u16(degree2servo(angle2))
    time.sleep_ms(30)
    
first.deinit()
second.deinit()
