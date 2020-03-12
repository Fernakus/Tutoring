# Imports 
from machine import Pin, Timer
import time

################ Global Variables ################
# GPIOs
A1 = Pin(2,Pin.OUT)
A2 = Pin(0,Pin.OUT)
B1 = Pin(4,Pin.OUT)
B2 = Pin(5, Pin.OUT)

# Lists
codes = [[1,0,1,0],
         [1,0,0,1],
         [0,1,0,1],
         [0,1,1,0]] 

motor = [A1, A2, B1, B2]

# main()
def main():
    # Loop Indefinitely
    while True:
        try:
            # Collect Input
            choice = int(raw_input('Enter [1 or 2]: '))
            
            # Part 1
            if choice == 1:           
                # Collect Speed
                speed = float(raw_input('Enter an integer speed [20 RPM - 60 RPM]: '))
                
                # Invalid Speed
                if speed < 20 or speed > 60:
                    raise ValueError
                
                # Make move with speed
                else:
                    index = 0
                    
                    while True:
                        # Increment index
                        index += 1
                        index = keepInRange(index)
                        
                        # Call moveWithSpeed()
                        moveWithSpeed(calcRPM(speed))
                        
            # Part 2
            elif choice == 2:
                
                # Collect Direction
                direction = raw_input('Enter N for north, W for west, E for east or S for south: ')
                
                # Make move with direction
                if direction == 'N' or direction == 'E' or direction == 'S' or direction == 'W':
                    moveWithDirection(direction)
                
                # Invalid
                else:
                    print('Invalid direction selection starting over...')
                    print('')
                    continue
                    
        except ValueError:
            print('Invalid selection starting over...')
            print('')  
            
        except NameError:
            print('Invalid selection starting over...')
            print('')
            
    return 

# calcRPM()
def calcRPM(speed):
    return 1 / ((speed / 60) * 200)

# moveWithSpeed()
def moveWithSpeed(speed):
    # Move The Motor
    moveMotor('f', 200, speed)

    return

# moveWithDirection()
def moveWithDirection(direction):
    # Speed Variable
    speed = 0.005

    # North
    if direction == 'N':
        moveMotor('forwards', 200, speed)

    # South
    elif direction == 'S':
        moveMotor('backwards', 100, speed)

    # East
    elif direction == 'E':
        moveMotor('forwards', 50, speed)

    # West
    elif direction == 'W':
        moveMotor('backwards', 50, speed)

    return

# moveMotor()
def moveMotor(direction, numOfSteps, speed):
    # Variables
    index = 0

    # Repeat Number of Steps
    for i in range(0, numOfSteps):
        # FORWARDS
        if direction == 'forwards':
            # Range Handling
            index += 1
            newIndex = keepInRange(index)
            index = newIndex
            
            # Make 1 move  
            z = 0
            for var in motor:                  
                var(codes[index][z])                
                z += 1

            # Time Delay
            time.sleep(speed) 

        # BACKWARDS
        elif direction == 'backwards':
            # Range Handling
            index -= 1
            if index < 0:
                index = 3
            
            # Make 1 move  
            z = 0
            for var in motor:                  
                var(codes[index][z])                
                z += 1

            # Time Delay
            time.sleep(speed) 
    return 

# keepInRange()
def keepInRange(index):
    # Keep in range of code list
    if index > 3:
        return 0

    return index

# Call Main()
main()