
# doesnt do anything as of now just sets up the boxes and connecting surrounding

from board import board
import pygame

data = {"rows":2,"cols":5,"multiplier":80}

pygame.init()
w1 = pygame.display.set_mode((data["cols"]*data["multiplier"],data["rows"]*data["multiplier"]))
clock = pygame.time.Clock()

game = board(data)

print("start\n")

running =True

def event_handle(pos):
    print()
    id = pos[0]//data["multiplier"] +data["cols"]*(pos[1]//data["multiplier"])
    print(id)
    game.add_atom(id)
    game.print_holding()

while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            running=False
        elif e.type==pygame.MOUSEBUTTONDOWN:
            event_handle(e.pos)
    game.run()

pygame.quit()
