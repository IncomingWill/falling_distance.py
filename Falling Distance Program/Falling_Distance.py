# Title: Falling Distance Program
# Program created by William Schaeffer
# CPS 313
# P. 296, Exercise 13, Falling Distance Program
# 01.25.22

# This program will use functions to take variable input to calculate falling distance per second

distance = 0.0              #distance to fall
fallingTime = 1             #time in seconds

#Main Program

def main():
    print(f'Falling Distance:')

    for fallingTime in range(1, 11):
        distance = falling_distance(fallingTime)
        print(f'In {fallingTime}s an object falls {distance:,.1f}m')
        fallingTime += 1

#Function Definition

def falling_distance(t):
    d = 0.0                 #variable to return for distance
    g = 9.8                 #g is for gravity, calculated at 9.8, which is the rate at which objects accelerate per square second

    d = .5*g*(t**2)         #Equation for calculating distance fallen given time

    return d

main()