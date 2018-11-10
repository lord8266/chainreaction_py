import pygame
import chainreaction

def event_handle(pos):
    #print(pos,end="")
    loc=pos[0]//100+5*(pos[1]//100)
    chainreaction.a.add_atom(loc)
    chainreaction.a.print_holding()

pygame.init()

w1 = pygame.display.set_mode((500,500))
pygame.display.set_caption("test")

clock = pygame.time.Clock() # returns clock object

running = True

while running:
    for e in pygame.event.get():
        if e.type ==pygame.QUIT:
            running =False
        elif e.type ==pygame.MOUSEBUTTONDOWN:
            event_handle(e.pos)
    chainreaction.a.run()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
