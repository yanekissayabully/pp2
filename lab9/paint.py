import pygame
from math import sqrt

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    baseLayer = pygame.Surface((640, 480))
    clock = pygame.time.Clock()
    #позиция ручки
    prevX = 0
    prevY = 0 
    #Starting and ending positions of rectangle while drawing:
    prevX1 = -1
    prevY1 = -1
    currentX1 = -1
    currentY1 = -1

    color = (255,255,255)
    screen.fill((0, 0, 0))
    isMouseDown = False
    while True:      
        pressed = pygame.key.get_pressed()
        # текущая координата
        currentX = prevX
        currentY = prevY       
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #выход из программы
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #правая
                    isMouseDown = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: #левая
                    isMouseDown = False
            if event.type == pygame.MOUSEMOTION: #ручка
                # если мышь переместилась, добавить точку в список для ручки
                currentX =  event.pos[0]
                currentY =  event.pos[1]

            if event.type == pygame.MOUSEBUTTONDOWN: #прямоугольник
                # если мышь переместилась, добавить точку в список для прямоугольника
                if event.button == 1: 
                    isMouseDown = True
                    currentX1 =  event.pos[0]
                    currentY1 =  event.pos[1]    
                    prevX1 =  event.pos[0]
                    prevY1 =  event.pos[1]
            #если isMouseDown фолс, то можем заканчивается наш рисунок
            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))
            # если isMouseDown тру, то можем рисовать фигуры
            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX1 =  event.pos[0]
                    currentY1 =  event.pos[1]
        # цвета
            if event.type == pygame.KEYDOWN:        
                if event.key == pygame.K_r: 
                    color = (255, 0, 0) 
                elif event.key == pygame.K_g: 
                    color = (0, 255, 0) 
                elif event.key == pygame.K_b: 
                    color = (0, 0, 255) 
                elif event.key == pygame.K_w: 
                    color = (255,255,255)  
        if isMouseDown :
            pygame.draw.line(screen, color, (prevX, prevY), (currentX, currentY))

        if pressed[pygame.K_1]: #прямоугольник
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                r = calculateRect(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.rect(screen, color,pygame.Rect(r), 1)

        if pressed[pygame.K_2]: #круг
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1: 
                screen.blit(baseLayer, (0, 0))
                c = centerCirc(prevX1, prevY1, currentX1, currentY1) 
                ra = radiusCirc(prevX1, prevY1, currentX1, currentY1) 
                pygame.draw.circle(screen, color, c, ra, 1)

        if pressed[pygame.K_4]: #квадрат
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                square = calculatesquare(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.rect(screen, color,pygame.Rect(square), 1)

        if pressed[pygame.K_5]: #равносторонний треугольник
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                triangle = equilateraltriangle(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.polygon(screen, color,triangle, 1)
        if pressed[pygame.K_6]: #правильный треугольник
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                rtriangle = calculateRtriangle(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.polygon(screen, color,rtriangle, 1)

        if pressed[pygame.K_7]: #ромб
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                romb = calcRomb(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.polygon(screen, color,romb, 1)

        if pressed[pygame.K_3]:
            if isMouseDown:
                pygame.draw.line(screen, (0,0,0), (prevX, prevY), (currentX, currentY),30)

        prevX = currentX
        prevY = currentY
        
        pygame.display.flip()
        clock.tick(60)
def calculateRect(x1, y1, x2, y2):
#Верхняя левая x координата, Верхняя левая y координата, нижняя правая x координата, нижняя правая y координата
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))
# нахождение центра прямоугольника
def centerCirc(x1, y1, x2, y2): 
    return abs(x1 - x2) / 2 + min(x1, x2), abs(y1 - y2) / 2 + min(y1, y2)
#нахождение радиуса круга 
def radiusCirc(x1, y1, x2, y2): 
    return sqrt((((abs(x1 - x2) / 2) ** 2) + (abs(y1 - y2) / 2) ** 2))
def calculatesquare(x1, y1, x2, y2):
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    return min(x1,x2),min(y1,y2),a,a
def calculateRtriangle(x1, y1, x2, y2): 
    return [(min(x1, x2), min(y1, y2)), (min(x1, x2), abs(y1 - y2) + min(y1, y2)), (abs(x1 - x2) + min(x1, x2), abs(y1 - y2) + min(y1, y2))]
def equilateraltriangle(x1, y1, x2, y2):
    side = min(abs(x2-x1), abs(y2-y1))
    height = round(side * 0.866) 
    x = 1
    y = 1
    if (x2 > x1):
        x = -1
    if (y2 > y1):
        y = -1
    pnt1 = (x2 + round(side/2)*x, y2)
    pnt2 = (x2, y2 + height*y)
    pnt3 = (x2 + side*x, y2 + height*y)
    return (pnt1, pnt2, pnt3)
def calcRomb(x1, y1, x2, y2):
    a, b = abs(x2-x1),abs(y2-y1)
    return (x1,y1+b),(x1+a,y1),(x1,y1-b),(x1-a,y1)
main()