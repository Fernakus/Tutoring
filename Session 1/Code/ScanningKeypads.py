'''
Created on Feb. 8, 2020

@author: mferl
'''

# Imports
from machine import Pin
import time

###################### Global Variables ######################
# Outputs
C1 = Pin(13,Pin.OUT)
C2 = Pin(12,Pin.OUT)
C3 = Pin(14,Pin.OUT)

# Inputs
R1 = Pin(2,Pin.IN,Pin.PULL_UP)
R2 = Pin(0,Pin.IN,Pin.PULL_UP)
R3 = Pin(4,Pin.IN,Pin.PULL_UP)
R4 = Pin(5,Pin.IN,Pin.PULL_UP)

# Other Variables   
keys = ['1','4','7','*','2','5','8','0', '3','6','9','#']
#############################################################

# scanKeypad()
def scanKeypad(kIndex, inputRowsList):
    # Check bits in each row
    for rowBit in inputRowsList:
        # Found key pressed
        if rowBit == 0:
            return(keys[kIndex])
        
        # Increment
        kIndex += 1      
        
    # Returns -1 if no key was pressed
    return -1

######################## Main Method ########################
def AppEntryPoint():
    # Continually Scan
    while True:
        # Set Counter
        kIndex = 0

        ########### Scan the LEFT column ###########
        C1(0)
        C2(1)
        C3(1) 
        keyPressed = scanKeypad(kIndex, [R1(), R2(), R3(), R4()])
        
        # Output
        if keyPressed != -1:
            print(keyPressed)
            
        # Increment
        kIndex += 4      
         
        ########### Scan the MIDDLE column ###########
        C1(1)
        C2(0)
        C3(1) 
        keyPressed = scanKeypad(kIndex, [R1(), R2(), R3(), R4()])
        
        # Output
        if keyPressed != -1:
            print(keyPressed)
            
        # Increment
        kIndex += 4  
        
        ########### Scan the RIGHT column ###########
        C1(1)
        C2(1)
        C3(0) 
        keyPressed = scanKeypad(kIndex, [R1(), R2(), R3(), R4()])
        
        # Output
        if keyPressed != -1:
            print(keyPressed)
            
    return 

# Call AppEntryPoint()
AppEntryPoint()