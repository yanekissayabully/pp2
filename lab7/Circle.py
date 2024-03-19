import pygame

pygame.init()
w = 800
h = 400
sc = pygame.display.set_mode((w, h))
pygame.display.set_caption("Circle")
run = True
x = w//2
y = h//2
r = 25
v = 20
clock = pygame.time.Clock()
while run:
    clock.tick(100)
    sc.fill((255,255,255))
    circle = pygame.draw.circle(sc,(255, 0, 0), (x,y), r)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x > r:
                x-=v
            if event.key == pygame.K_RIGHT and x < w-r:
                x+=v
            if event.key == pygame.K_UP and y > r:
                y-=v
            if event.key == pygame.K_DOWN and y < h-r:
                y+=v