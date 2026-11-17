import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pygame.draw.rect(screen, (0,125,255), pygame.Rect(30,30,60,60))
        Green = (0,225,0)
        pygame.draw.circle(screen, Green, (300, 300), 50)
        pygame.draw.circle(screen, Green, (100, 200), 50, 3)

    pygame.display.flip()

