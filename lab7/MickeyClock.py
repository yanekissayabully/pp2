import pygame
import datetime
pygame.init()

screen=pygame.display.set_mode((830,700))
clock=pygame.time.Clock()
pygame.display.set_caption("MickeyClock")
mickey=pygame.image.load("main-clock.png")

minutes=pygame.image.load("right-hand.png")
minn=minutes.get_rect()

seconds=pygame.image.load("left-hand.png")
secc=seconds.get_rect()
angle1=0
angle2=0
running=True
while running:
    screen.blit(mickey,(0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
    now=datetime.datetime.now().time()
    minute=now.minute
    second=now.second

    angle1=-minute*6+84
    rot1=pygame.transform.rotate(minutes, angle1)
    rect1=rot1.get_rect()
    rect1.center=minn.center

    angle2=-second*6-282
    rot2=pygame.transform.rotate(seconds, angle2)
    rect2=rot2.get_rect()
    rect2.center=secc.center

    screen.blit(mickey, (0, 0))
    screen.blit(rot1, rect1)
    screen.blit(rot2, rect2)

    pygame.display.flip()
    clock.tick(60)