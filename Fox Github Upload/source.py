import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 600

score=0
game_over=False

fox=Actor("fox")
fox.pos=100, 100
coin=Actor('coin')
coin2=Actor('coin')
coin3=Actor('coin')
coin4=Actor('coin')
coin5=Actor('coin')
coin.pos=randint(20, (WIDTH-20)),randint(20, (HEIGHT-20))
coin2.pos=randint(20, (WIDTH-20)),randint(20, (HEIGHT-20))
coin3.pos=randint(20, (WIDTH-20)),randint(20, (HEIGHT-20))
coin4.pos=randint(20, (WIDTH-20)),randint(20, (HEIGHT-20))
coin5.pos=randint(20, (WIDTH-20)),randint(20, (HEIGHT-20))

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    coin2.draw()
    coin3.draw()
    coin4.draw()
    coin5.draw()    
    
    global score
    screen.draw.text("Score: "+str(score),color="black",topleft=(10,10))

    if game_over:
        screen.fill("blue")
        screen.draw.text("Final score: "+str(score),color="black",topleft=(10, 10),fontsize=60)

def place_coin():
    coin.x=randint(20, (WIDTH-20))
    coin.y=randint(20, (HEIGHT-20))

def place_coin2():
    coin2.x=randint(20, (WIDTH-20))
    coin2.y=randint(20, (HEIGHT-20))

def place_coin3():
    coin3.x=randint(20, (WIDTH-20))
    coin3.y=randint(20, (HEIGHT-20))

def place_coin4():
    coin4.x=randint(20, (WIDTH-20))
    coin4.y=randint(20, (HEIGHT-20))

def place_coin5():
    coin5.x=randint(20, (WIDTH-20))
    coin5.y=randint(20, (HEIGHT-20))

    
def time_up():
    global game_over
    game_over=True

def update():
    global score
    if keyboard.left:
        fox.x=fox.x-8
    elif keyboard.right:
        fox.x=fox.x+8
    elif keyboard.up:
        fox.y=fox.y-8
    elif keyboard.down:
        fox.y=fox.y+8

    coin_collected=fox.colliderect(coin)
    if coin_collected:
        score=score+10
        place_coin()
    coin_collected2=fox.colliderect(coin2)
    if coin_collected2:
        score=score+10
        place_coin2()
    coin_collected3=fox.colliderect(coin3)
    if coin_collected3:
        score=score+10
        place_coin3()
    coin_collected4=fox.colliderect(coin4)
    if coin_collected4:
        score=score+10
        place_coin4()
    coin_collected5=fox.colliderect(coin5)
    if coin_collected5:
        score=score+10
        place_coin5()


place_coin()

pgzrun.go()
