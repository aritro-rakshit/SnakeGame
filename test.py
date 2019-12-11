import pygame
x=pygame.init()

#creating window
gameWindow=pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My First Game")


#game Specifics
exit_game=False
game_over=False 


#creating a game loop
while not exit_game:
    for event in pygame.event.get():
            print(event)
            if event.type==pygame.quit:
                exit_game=True
                
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    print("You have entered right key")
pygame.quit()
quit()