
# doesnt do anything as of now just sets up the boxes and connecting surrounding

import pygame
pygame.init()
pygame.font.init()
from board import board
import conf
data=conf.data
# look at conf.py

# no of rows ,cols and the multiplier says the size of each box
# each box is a square





clock = pygame.time.Clock()

game = board(data)

print("start\n")

game.main_running =True

def event_handle(pos):
    print(pos)
    game.user_event(pos)


while game.main_running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            game.main_running=False
        elif e.type==pygame.MOUSEBUTTONDOWN:
            event_handle(e.pos)

    game.run()

    pygame.display.flip()
    clock.tick(data["fps"])
    if game.reset:
        game.reset_all()


pygame.quit()
