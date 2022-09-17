import sys
from game import *

pygame.init()

# Screen
WIDTH, HEIGHT = 750, 500
pygame.display.set_icon(pygame.image.load('assets/ball.png'))
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Initialize classes
game = PongGame(screen, WIDTH, HEIGHT)

# Main Loop
while 1:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            
    key_input = pygame.key.get_pressed()   
    if   key_input[pygame.K_LEFT] :    game.controls(direction="left")
    elif key_input[pygame.K_RIGHT]:    game.controls(direction="right")
    
    game.draw_screen()
    game.ball_motion()
    game.breakbrick()
    game.isgameover()
    pygame.display.update()