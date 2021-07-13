from machine import Pin, PWM
import machine
import time
import random
from lcd import *

# Led
led = PWM(Pin(25))
led.freq(10)
led.duty_u16(300)

# Encoder
ENC_A = Pin(14, Pin.IN, Pin.PULL_DOWN)
ENC_B = Pin(15, Pin.IN, Pin.PULL_DOWN)
reset = Pin(13, Pin.IN, Pin.PULL_DOWN)

# Fan PWM
PWM_Fan = PWM(Pin(12))
PWM_Fan.freq(25000)

# LCD Object and pin definition
LCD = lcd(RS=17, RW=1, EN=16, D4=18, D5=19, D6=20, D7=21, COL=20, ROW=4)

# LCD Initializing
LCD.init()

# LCD Clear
LCD.clrscr()

# Write down label
LCD.pos_puts(0, 0, "Fan Speed:")
speed = 3930

prev_val = True    
while True:
    # LCD.pos_puts(11, 0, "%d" % adc.read_u16())
    if prev_val == False and ENC_A.value() == True:
        speed += 655 * 5
    elif prev_val == False and ENC_B.value() == True:
        speed -= 655 * 5
    
    if ENC_A.value() == True or ENC_B.value() == True:
        prev_val = True
    else:
        prev_val = False
        
    LCD.pos_puts(5, 1, "%d  " % int((speed / 65535) * 100) )
    LCD.pos_puts(8, 1, "%")
    if speed > 65535:
        speed = 65535
    
    if speed < 0:
        speed = 0
        
    if reset.value() == True:
        speed = 3930
        
    PWM_Fan.duty_u16(speed)
    led.duty_u16(speed)
    