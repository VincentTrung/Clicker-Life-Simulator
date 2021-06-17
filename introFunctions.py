from settings import *
from helper import *
import time

#start menu before game loop
def startMenu():
    global cursorY
    intro = True
    while intro:
        if startButton.collidepoint(pygame.mouse.get_pos()):
            cursorY= startY
        if quitButton.collidepoint(pygame.mouse.get_pos()):
            cursorY = quitY
    
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:#collect clicked coords
                mouse_pos = event.pos
                if startButton.collidepoint(mouse_pos):
                    return True
                if quitButton.collidepoint(mouse_pos):
                    return False
        #DRAW
        screen.fill(SKYBLUE)
        drawBird()
        drawBunny()
        grass = pygame.Rect(0,HEIGHT-100,WIDTH,100)
        pygame.draw.rect(screen,GRASS, grass)

        #title
        pygame.draw.ellipse(screen, RED, (40,10,400,100))
        screen.blit(Title, (55,50))

        screen.blit(cursor,(startX- 50, cursorY + button1Y//2))
        #start button
        createButton('Start', GREEN, startX, startY,button1X,button1Y)
        #quit button
        createButton('Quit', RED, quitX, quitY ,button1X,button1Y)
        
        clock.tick(24)
        pygame.display.flip()

#bunny animation
def drawBunny():
    global bunnyX, bunnyY, WIDTH, frame
    if frame > 3:
      frame -= 3
    bunny = pygame.image.load("Images/bunny sprite/bunny-" +str(frame)+".png")
    screen.blit(bunny,(bunnyX,bunnyY))
    if bunnyX <= 0:
        bunnyX = WIDTH
    else:
        bunnyX -= 7

#bird animation
def drawBird():
    global birdX, birdY, WIDTH, frame
    if frame < 7:
        frame += 1
    else:
        frame -= 7
    bird = pygame.image.load("Images/bird sprite/frame-" +str(frame)+".png")
    screen.blit(bird,(birdX,birdY))
    if birdX >= WIDTH:
        birdX = 0
    else:
        birdX += 3