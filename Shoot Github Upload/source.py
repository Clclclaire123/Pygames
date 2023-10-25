import pgzrun
from random import randint

apple=Actor("apple")
points=0

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x=randint(10, 800)
    apple.y=randint(10, 600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        global points
        points=points+1
        place_apple()
    else:
        print("You missed! Your score is",points)
        quit()

place_apple()

pgzrun.go()
