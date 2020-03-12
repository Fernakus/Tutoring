# test_keypad.py
# Author: by Mark Allemang
# Descr: this code simply tests the wiring of the keypad

from machine import Pin
import time

# create my outputs
C1 = Pin(13,Pin.OUT)
C2 = Pin(12,Pin.OUT)
C3 = Pin(14,Pin.OUT)

# create my inputs
R1 = Pin(2,Pin.IN,Pin.PULL_UP)
R2 = Pin(0,Pin.IN,Pin.PULL_UP)
R3 = Pin(4,Pin.IN,Pin.PULL_UP)
R4 = Pin(5,Pin.IN,Pin.PULL_UP)

# scan the left column
C1(0)
C2(1)
C3(1)

# check the 4 rows continually
while True:
  if not R1():
    print('got a zero on R1')
  if not R2():
    print('got a zero on R2')
  if not R3():
    print('got a zero on R3')
  if not R4():
    print('got a zero on R4')
