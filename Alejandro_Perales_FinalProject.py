import pygame
import sys
import time
from random import randint

# CONTROLS
# Move with up, down, right and left arrows keys
# "p" key pause the game and active it again


# Draw the snake (first the head and later the body)
def drawSnake(snake):
    for i in range(len(snake)):
        if i == 0:
            pygame.draw.rect(
                screen,
                black,
                (snake[i][1]*sideRec, snake[i][0]*sideRec, sideRec, sideRec)
            )
        pygame.draw.rect(
            screen,
            black,
            (snake[i][1]*sideRec, snake[i][0]*sideRec, sideRec, sideRec),
            widthRec
        )


# Move the snake forward
def ahead(snake, newPos):
    for i in reversed(range(1, len(snake))):
        snake[i] = snake[i-1]
    snake[0] = newPos
    # If the snake cross the border, he appears on the opposite side
    if snake[0][1]*sideRec >= widthScr:
        snake[0][1] = 0
    elif snake[0][1] < 0:
        snake[0][1] = widthScr/sideRec
    elif snake[0][0]*sideRec >= heightScr:
        snake[0][0] = 0
    elif snake[0][0] < 0:
        snake[0][0] = heightScr/sideRec
    return snake


# Initial screen
def startScreen():
    myFont = pygame.font.Font(None, 90)
    text = myFont.render("PRESS SPACE TO START", True, white)
    text_rect = text.get_rect()
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_height() / 2 - text_rect.height / 2
    screen.blit(text, [text_x, text_y])
    pause = True
    pygame.display.flip()
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        pause = False


# Show the score on the screen
def showScore(score):
    myFont = pygame.font.Font(None, 30)
    text = myFont.render("Score: "+str(score), True, white)
    text_rect = text.get_rect()
    text_x = screen.get_width() / 20 - text_rect.width / 2
    text_y = screen.get_height() / 30 - text_rect.height / 2
    screen.blit(text, [text_x, text_y])


# Pause the game
def pause():
    myFont = pygame.font.Font(None, 130)
    text = myFont.render("PAUSE", True, white)
    text_rect = text.get_rect()
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_height() / 2 - text_rect.height / 2
    screen.blit(text, [text_x, text_y])
    pause = True
    pygame.display.flip()
    pygame.time.wait(500)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                        pause = False


# Show the final score
def showFinalScore(score):
    myFont = pygame.font.Font(None, 80)
    text = myFont.render("Score: "+str(score), True, white)
    text_rect = text.get_rect()
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_height() / 2 - text_rect.height / 2
    screen.blit(text, [text_x, text_y])


# Show Game Over
def showGameOver():
    myFont = pygame.font.Font(None, 120)
    text = myFont.render("GAME OVER", True, white)
    text_rect = text.get_rect()
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_height() / 4 - text_rect.height / 2
    screen.blit(text, [text_x, text_y])


pygame.init()

# Screen
widthScr = 900
heightScr = 600
screen = pygame.display.set_mode((widthScr, heightScr))
# Row and column of each rectangle of the initial snake
snake = [[6, 9], [6, 8], [6, 7], [6, 6]]
# Direction of the snake - Keys
right, left, up, down = True, False, False, False
# Food coordinates
posX = 10
posY = 10
# Characteristics of the rectangle
sideRec = 30
widthRec = 2
# Colours
background = (40, 150, 20)
black = (0, 0, 0)
red = (200, 0, 0)
white = (255, 255, 255)
# Others
score = 0

startScreen()

while True:

    screen.fill(background)

    drawSnake(snake)

    pygame.draw.rect(
        screen,
        red,
        (posX*sideRec, posY*sideRec, sideRec, sideRec))

    showScore(score)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and down is False:
                right, left, up, down = False, False, True, False
            elif event.key == pygame.K_DOWN and up is False:
                right, left, up, down = False, False, False, True
            elif event.key == pygame.K_LEFT and right is False:
                right, left, up, down = False, True, False, False
            elif event.key == pygame.K_RIGHT and left is False:
                right, left, up, down = True, False, False, False
            elif event.key == pygame.K_p:
                    pause()

    # When the snake take the food, we add a rectangle to him
    if snake[0][0] == posY and snake[0][1] == posX:
        snake.append([0, 0])
        posX = randint(0, (widthScr/sideRec)-1)
        posY = randint(0, (heightScr/sideRec)-1)
        score = score + 1

    # Check if the snake bites himself
    for i in range(1, len(snake)):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            showGameOver()
            showFinalScore(score)
            pygame.display.flip()
            pygame.time.wait(5000)
            pygame.quit()
            sys.exit()

    # Decide the direction of the snake and move the snake
    if right is True:
        snake = ahead(snake, [snake[0][0], snake[0][1]+1])
    elif left is True:
        snake = ahead(snake, [snake[0][0], snake[0][1]-1])
    elif up is True:
        snake = ahead(snake, [snake[0][0]-1, snake[0][1]])
    elif down is True:
        snake = ahead(snake, [snake[0][0]+1, snake[0][1]])

    time.sleep(0.1)

    pygame.display.flip()
