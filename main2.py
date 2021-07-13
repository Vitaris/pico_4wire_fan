from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(25))

pwm.freq(1000)

while True:
    for duty in range(0, 65025, 100):
        pwm.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025, 0, -2):
        pwm.duty_u16(duty)
        sleep(0.0001)
