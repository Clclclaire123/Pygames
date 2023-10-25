import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400

dots = []
lines = []

next_dot = 0
timer = 0
time_out = 15
game_over = False

for dot in range(10):
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH-20), randint(20, HEIGHT-20)
    dots.append(actor)

def draw():
    global timer
    global game_over
    screen.clear()
    screen.fill("black")
    number = 1
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1]+12))
        dot.draw()
        number = number+1
    for line in lines:
        screen.draw.line(line[0], line[1], (255, 0, 0))
    if next_dot == 10:
        screen.draw.text("You beat the game in", center=(200,130), color=(255, 255, 0), fontsize=50)
        screen.draw.text(str(round(timer,2)), center=(200, 230), color=(255, 255, 0), fontsize=30)
        game_over=True
    else:
        screen.draw.text(str(round(timer,2)), topleft=(10, 10), color=(255, 0, 0), fontsize=30)
    if timer>= time_out:
        screen.fill("black")
        screen.draw.text("Time's up! You lost the game.", center=(200, 160), color=(255, 255, 255), fontsize=30)
        game_over=True
        

def on_mouse_down(pos):
    global next_dot
    global lines
    if dots[next_dot].collidepoint(pos):
        sounds.click.play()
        if next_dot:
            lines.append((dots[next_dot-1].pos, dots[next_dot].pos))
        next_dot=next_dot+1
    else:
        lines=[]
        next_dot=0

def update():
    global timer
    if next_dot!=10:
        timer=timer+1/60

pgzrun.go()
