
# doesnt do anything as of now just sets up the boxes and connecting surrounding

from board import board
import pygame
import conf
data=conf.data
# look at conf.py

# no of rows ,cols and the multiplier says the size of each box
# each box is a square


pygame.init()
w1 = pygame.display.set_mode((data["cols"]*data["multiplier"],data["rows"]*data["multiplier"]))
icon=pygame.image.load(data["icon_loc"])
pygame.display.set_icon(icon)
pygame.display.set_caption(data["title"])

data["w1"]=w1
clock = pygame.time.Clock()

game = board(data)

print("start\n")

game.main_running =True

def event_handle(pos):
    id = pos[0]//data["multiplier"] +data["cols"]*(pos[1]//data["multiplier"])
    game.user_event(id)


while game.main_running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            game.main_running=False
        elif e.type==pygame.MOUSEBUTTONDOWN:
            event_handle(e.pos)
    w1.fill((0,0,0))
    game.run()

    pygame.display.flip()
    clock.tick(60)

print(game.current.name,"won")
pygame.quit()
