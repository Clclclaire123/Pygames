import pgzrun
from random import randint

WIDTH=800
HEIGHT=600

balloon = Actor('balloon')
balloon.pos = 400, 300
bird = Actor('bird-up')
bird.pos = randint(800, 1600), randint(10, 200)
house = Actor('house')
house.pos = randint(800, 1600), 460
tree = Actor('tree')
tree.pos = randint(800, 1600), 450

bird_up = True
up = False
game_over = False
score = 0
numofup = 0

scores = []


def update_high_scores():
    global score, scores
    filename = r"/Users/mlim/Documents/Balloon Flight/highscores.txt"
    scores = []
    with open(filename, "r") as file:
        line = file.readline()
        high_scores = line.split()
        for x in high_scores:
            if (score > int(x)):
                scores.append(str(score) + " ")
                score = int(x)
            else:
                scores.append(str(x) + " ")
    with open(filename, "w") as file:
        for x in scores:
            file.write(x)

def display_high_scores():
    screen.draw.text("HIGHSCORES", (350, 150), color = "black")
    y = 175
    rank = 1
    for x in scores:
        screen.draw.text(str(rank) + ". " + str(x), (350, y), color = "black")
        y = y + 25
        rank = rank + 1

def draw():
    screen.blit('background', (0, 0))
    if not game_over:
        balloon.draw()
        bird.draw()
        house.draw()
        tree.draw()
        screen.draw.text('Score: ' + str(score), (700, 5), color = 'black')
    else:
        display_high_scores() 

def on_mouse_down():
    global up
    up = True
    balloon.y = balloon.y - 50

def on_mouse_up():
    global up
    up = False

def flap():
    global bird_up
    if bird_up:
        bird.image = ("bird-down")
        bird_up = False
    else:
        bird.image = ("bird-up")
        bird_up = True

def update():
    global game_over, score, numofup
    if not game_over:
        if not up:
            balloon.y = balloon.y + 1
        if bird.x > 0:
            bird.x = bird.x - 4
            if numofup == 9:
                flap()
                numofup = 0
            else:
                numofup = numofup + 1
        else:
            bird.pos = randint(800, 1600), randint(10, 200)
            score = score + 100
            numofup = 0
        if house.right > 0:
            house.x = house.x - 3
        else:
            house.x = randint(800, 1600)
            score = score + 100
        if tree.right > 0:
            tree.x = tree.x - 2
        else:
            tree.x = randint(800, 1600)
            score = score + 100
        if balloon.top < 0 or balloon.bottom > 560:
            game_over = True
            update_high_scores()
        if balloon.colliderect(bird) or balloon.colliderect(tree) or balloon.colliderect(house):
            game_over = True
            update_high_scores()
            
            


pgzrun.go()
