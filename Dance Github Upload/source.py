from random import randint
import pgzrun

WIDTH = 800
HEIGHT = 600
CenterX = 400
CenterY = 300

move_list = []
display_list = []
score = 0
current_move = 0
count = 4
dance_length = 4

say_dance = False
show_countdown = True
moves_complete = False
game_over = False

dancer = Actor("dancer-start")
dancer.pos = (CenterX + 5, CenterY - 40)
upkey = Actor("up")
upkey.pos = (CenterX, CenterY + 110)
rightkey = Actor("right")
rightkey.pos = (CenterX + 60, CenterY + 170)
downkey = Actor("down")
downkey.pos = (CenterX, CenterY + 230)
leftkey = Actor("left")
leftkey.pos = (CenterX - 60, CenterY + 170)
    
def draw():
    global game_over, score, say_dance, count, show_countdown
    if not game_over:
        screen.clear()
        screen.blit("stage", (0, 0))
        dancer.draw()
        upkey.draw()
        downkey.draw()
        leftkey.draw()
        rightkey.draw()
        screen.draw.text("score: " + str(score), topleft = (10, 10), color = "black")
        if say_dance:
            screen.draw.text("DANCE!", color = "black", topleft = (CenterX - 65, 150), fontsize = 60)
        if show_countdown:
            screen.draw.text(str(count), color = "black", topleft = (CenterX - 8, 150), fontsize = 60)
    else:
        screen.clear()
        screen.blit("stage", (0, 0))
        screen.draw.text("Game over.", color = "black", topleft = (CenterX - 130, 220), fontsize = 60)
    return

def generate_moves():
    global move_list, dance_length, count, show_countdown, say_dance
    count = 4
    move_list = []
    say_dance = False
    for x in range(0, dance_length):
        lala = randint(0, 3)
        move_list.append(lala)
        display_list.append(lala)
    show_countdown = True
    countdown()
    return

def reset_dancer():
    global game_over
    if not game_over:
        dancer.image = ("dancer-start")
        upkey.image = ("up")
        downkey.image = ("down")
        rightkey.image = ("right")
        leftkey.image = ("left")
    return

def display_moves():
    global move_list, dance_length, count, show_countdown, say_dance, current_move, display_list
    if display_list:
        this_move = display_list[0]
        display_list = display_list[1:]
        if this_move == 0:
            change_dancer(0)
            clock.schedule(display_moves, 1)
        elif this_move == 1:
            change_dancer(1)
            clock.schedule(display_moves, 1)
        elif this_move == 2:
            change_dancer(2)
            clock.schedule(display_moves, 1)
        elif this_move == 3:
            change_dancer(3)
            clock.schedule(display_moves, 1)
    else:
        say_dance = True
        show_countdown = False
    return

def change_dancer(move):
    global game_over
    if not game_over:
        if move == 0:
            upkey.image = ("up-lit")
            dancer.image = ("dancer-up")
            clock.schedule(reset_dancer, 0.5)
        elif move == 1:
            rightkey.image = ("right-lit")
            dancer.image = ("dancer-right")
            clock.schedule(reset_dancer, 0.5)
        elif move == 2:
            downkey.image = ("down-lit")
            dancer.image = ("dancer-down")
            clock.schedule(reset_dancer, 0.5)
        elif move == 3:
            leftkey.image = ("left-lit")
            dancer.image = ("dancer-left")
            clock.schedule(reset_dancer, 0.5)
    return

def on_key_up(key):
    global score, game_over
    if key == keys.UP:
        change_dancer(0)
        if move_list[current_move] == 0:
            score = score + 1
            next_move()
        else:
            game_over = True
    elif key == keys.RIGHT:
        change_dancer(1)
        if move_list[current_move] == 1:
            score = score + 1
            next_move()
        else:
            game_over = True
    elif key == keys.DOWN:
        change_dancer(2)
        if move_list[current_move] == 2:
            score = score + 1
            next_move()
        else:
            game_over = True
    elif key == keys.LEFT:
        change_dancer(3)
        if move_list[current_move] == 3:
            score = score + 1
            next_move()
        else:
            game_over = True

def next_move():
    global dance_length, current_move, moves_complete
    if current_move < dance_length - 1:
        current_move = current_move + 1
    else:
        moves_complete = True
    return

def countdown():
    global count, game_over, show_countdown
    if count > 1:
        count = count - 1
        clock.schedule(countdown, 1)
    else:
        show_countdown = False
        display_moves()
    return

generate_moves()
music.play("vanishing-horizon")

def update():
    global current_move, game_over, moves_complete, dance_length
    if not game_over:
        if moves_complete:
            generate_moves()
            moves_complete = False
            current_move = 0
    else:
        music.stop()
        


pgzrun.go()



