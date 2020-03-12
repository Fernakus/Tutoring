#Program: Project 2: Part 1-Stepper Motor Procedure 1
#Programmer: Kaleb Lidstone
#Date submitted: February 11th,2020
#Description of program: This program prompts a user to enter in a f for turning the motor forward one step
#and b for turning the motor reverse one step
from machine import Pin, Timer
import time
MyGPIO=[2,0,4,5]
A1 = Pin(2,Pin.OUT)#create my outputs
A2 = Pin(0,Pin.OUT)#create my outputs
B1 = Pin(4,Pin.OUT)#create my outputs
B2 = Pin(5,Pin.OUT)#create my outputs
         
codes = [[1,0,1,0],[1,0,0,1],[0,1,0,1],[0,1,1,0]]
#when the f key is pressed the motor will move up one step and when b is pressed the motor will move one step back      
def SendOutputs(codes,Motor):
   x=0
   while True:
        enter = input('enter to move forward or back')
        if enter == 'f':
            x+=1
            if x>3:                             #ensures that when f is pressed more than 4 times, it doesnt exceed the 4 steps for a full cycle in the list codes
                x=0
            print(codes[x])
            z=0
            for var in Motor:                   #takes the required outputs from the MyGPIO list
                var(codes[x][z])                #takes the bits from the list codes 
                z+=1
      
        elif enter == 'b':
            x-=1
            if x<0:                             #ensures that when b is pressed more than 4 times, it doesnt exceed the 4 steps for a full cycle in the list codes
               x=3
            print(codes[x])
            z = 0
            for var in Motor:                   #takes the required outputs from the MyGPIO list
                var(codes[x][z])                #takes the bits from the list codes
                z+=1
        elif enter != 'f' and enter != 'b':     #ensures that the user enters the correct key and is prompted to do so if correct key is not entered
                print('invald selection try again')
        else:
            continue
def main():
    Motor = [] 
    for num in MyGPIO:                          #displays the pins
        TheOutput = Pin(num , Pin.OUT)
        Motor.append(TheOutput)
    SendOutputs(codes,Motor)                    #calls the function SendOutputs with the arguments codes and Motor being passed
main()
