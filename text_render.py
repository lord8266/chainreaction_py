import pygame


font = pygame.font.SysFont("comicsansms",72)

def create_text(name,color):
    text =font.render(name,True,color)
    return text
