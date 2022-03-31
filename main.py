from turtle import *
import time
import math

WIDTH, HEIGHT = 500, 500
DRAWING_SPEED = 10 #1 SLOWEST 10 FASTEST

#Change this values
SIDES_NUMBER = 6
SIDES_LENGHT = 100

ANGLE = 360 / SIDES_NUMBER
APOTHEM = SIDES_LENGHT/(2*math.tan((360/(2*SIDES_NUMBER)*(math.pi/180))))

#Initialize turtle module
def init_turtle():
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Geometry')

#Function that draws the polygon with center at the middle of the screen
def draw_regular_polygon(sides_number=SIDES_NUMBER, sides_lenght=SIDES_LENGHT, angle=ANGLE, apothem=APOTHEM, drawing_speed=DRAWING_SPEED):
    pointer = Turtle()
    pointer.penup()
    pointer.hideturtle()
    pointer.backward(sides_lenght//2)
    pointer.right(90)
    pointer.forward(apothem)
    pointer.left(90)
    pointer.pendown()
    pointer.speed(drawing_speed)

    for i in range(sides_number):
        pointer.forward(sides_lenght)
        pointer.left(angle)

#Runs the program
def main():
    init_turtle()
    draw_regular_polygon(SIDES_NUMBER, SIDES_LENGHT)
    time.sleep(5)

if __name__ == '__main__':
    main()