WIDTH = 1280
HEIGHT = 720

mainbox = Rect(0, 0, 820, 240)
timerbox = Rect(0, 0, 240, 240)
answerbox1 = Rect(0, 0, 495, 165)
answerbox2 = Rect(0, 0, 495, 165)
answerbox3 = Rect(0, 0, 495, 165)
answerbox4 = Rect(0, 0, 495, 165)

mainbox.move_ip(50, 40)
timerbox.move_ip(990, 40)
answerbox1.move_ip(50, 358)
answerbox2.move_ip(735, 358)
answerbox3.move_ip(50, 538)
answerbox4.move_ip(735, 538)

answerboxes = [answerbox1, answerbox2, answerbox3, answerbox4]

score = 0
timeleft = 20

q1 = ["What is the name of Claire's older sister?", "Christina", "Catherine", "Callie", "Chloe", 4]
q2 = ["Where was Claire born?", "Seoul, Korea", "Daegu, Korea", "Champaign, Illinois", "Boston, Massachusetts", 3]
q3 = ["What instument does Claire play?", "Flute", "Viola", "Saxophone", "Piano", 1]
q4 = ["What is Claire's favorite girl group?", "Le Sserafim", "Red Velvet", "Twice", "Aespa", 2]
q5 = ["What is Claire's favorite color?", "Sage Green", "Denim Blue", "Lemon Yellow", "Maroon Red", 1]

questions = [q1, q2, q3, q4, q5]
question = questions.pop(0)


def draw():
    screen.fill((145, 156, 112))
    screen.draw.filled_rect(mainbox, (219, 227, 195))
    screen.draw.filled_rect(timerbox, (219, 227, 195))

    for box in answerboxes:
        screen.draw.filled_rect(box, (242, 242, 242))

    screen.draw.textbox(str(timeleft), timerbox, color=(76, 79, 66))
    screen.draw.textbox(question[0], mainbox, color=(76, 79, 66))

    index = 1

    for box in answerboxes:
        screen.draw.textbox(question[index], box, color=(76, 79, 66))
        index = index + 1


def game_over():
    global question, timeleft
    message = "Game over. You got %s questions correct." % str(score)
    question =  [message, '-', '-', '-', '-', 5]
    timeleft = 0


def correct_answer():
    global question, score, timeleft

    score = score + 1
    if questions:
        question = questions.pop(0)
        timeleft = 20
    else:
        print("End of questions")
        game_over()


def on_mouse_down(pos):
    index = 1
    for box in answerboxes:
        if box.collidepoint(pos):
            print("Clicked answer")
            if index==question[5]:
                correct_answer()
            else:
                game_over()
        index = index + 1


def update_time_left():
    global timeleft

    if timeleft:
        timeleft = timeleft - 1
    else:
        game_over()


clock.schedule_interval(update_time_left, 1.0)








