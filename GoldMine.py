import pygame, sys
from pygame.locals import *
import random
import time
import PIL
from PIL import Image
import numpy as np

programIcon = pygame.image.load(r'C:\Users\ussfovan\Desktop\temp\python\dollar_coin.ico')
path_tooth = r'C:\Users\ussfovan\Desktop\temp\python\coin.gif'

pygame.display.set_icon(programIcon)

pygame.display.set_caption('Goldmünze Suchen')
running = True

size = 640, 640
screen = pygame.display.set_mode(size)
WHITE = (255, 255, 255)
screen.fill(WHITE)
pygame.display.update()

Window = pygame.display.set_mode((640, 640))
Window.fill((255, 255, 255))

'''cartoon motion'''


class SoldatImg:
    def __init__(self, name):
        self.name = name

    def location(self, x, filepath):
        img = pygame.image.load(filepath)
        img.convert()
        print("Width = " + " " + str(img.get_width()))
        print("Height = " + " " + str(img.get_height()))
        rect = img.get_rect()
        rect.center = x, 400
        RED = (255, 0, 0)
        pygame.draw.rect(screen, RED, rect, 1)
        screen.blit(img, rect)
        pygame.display.update()


SoldatLoc = SoldatImg('SS')
IronCross = SoldatImg('Iron Cross')
for i in range(0, 4):
    j = i * 200
    filepath = r'C:\Users\ussfovan\Desktop\temp\python\minecraft.gif'
    SoldatLoc.location(j, filepath)
    time.sleep(1)
    WHITE = (255, 255, 255)
    pygame.draw.rect(screen, WHITE, (j - 150, 250, 768, 512))

c = 300
filepath = r'C:\Users\ussfovan\Desktop\temp\python\gold-bar-png-gold.png'
IronCross.location(c, filepath)
pygame.display.update()

'''end cartoon motion'''

'''initial rectangles'''
Rectangle1 = Rect(100, 100, 100, 100)
Rectangle2 = Rect(200, 100, 100, 100)
Rectangle3 = Rect(300, 100, 100, 100)
Rectangle4 = Rect(400, 100, 100, 100)
RectangleObjects = (Rectangle1, Rectangle2, Rectangle3, Rectangle4)
for i in range(4):
    pygame.draw.rect(Window, (255, 0, 0), RectangleObjects[i], 10)
    pygame.display.update()
'''finish initial rectangles'''

'''game logic'''
rectangles = [1, 2, 3, 4]
color_diamond = (185, 242, 255)

shpearrange = random.sample(rectangles, 4)
print(shpearrange)


def loc_obj():
    if shpearrange[0] == 1 or shpearrange[0] == 2:
        pygame.draw.polygon(Window, color_diamond, ((110, 150), (150, 120), (190, 150), (150, 180)))

        WHITE = (255, 255, 255)
        pygame.draw.rect(Window, WHITE, (108, 110, 80, 80))
        pygame.display.update()
    elif shpearrange[0] == 3 or shpearrange[0] == 4:
        img = pygame.image.load(path_tooth)
        img.convert()
        rect_tooth = img.get_rect()
        rect_tooth.center = 150, 150
        WHITE = (255, 255, 255)
        pygame.draw.rect(screen, WHITE, rect_tooth, 1)
        screen.blit(img, rect_tooth)
        pygame.display.update()

        pygame.draw.rect(Window, WHITE, (108, 110, 80, 80))
        pygame.display.update()

    if shpearrange[1] == 1 or shpearrange[1] == 2:
        pygame.draw.polygon(Window, color_diamond, ((210, 150), (250, 120), (290, 150), (250, 180)))

        WHITE = (255, 255, 255)
        pygame.draw.rect(Window, WHITE, (208, 110, 80, 80))
        pygame.display.update()
    elif shpearrange[1] == 3 or shpearrange[1] == 4:
        img = pygame.image.load(path_tooth)
        img.convert()
        rect_tooth = img.get_rect()
        rect_tooth.center = 250, 150
        WHITE = (255, 255, 255)
        pygame.draw.rect(screen, WHITE, rect_tooth, 1)
        screen.blit(img, rect_tooth)
        pygame.display.update()

        WHITE = (255, 255, 255)
        pygame.draw.rect(Window, WHITE, (208, 110, 80, 80))
        pygame.display.update()

    if shpearrange[2] == 1 or shpearrange[2] == 2:
        pygame.draw.polygon(Window, color_diamond, ((310, 150), (350, 120), (390, 150), (350, 180)))

        WHITE = (255, 255, 255)
        pygame.draw.rect(Window, WHITE, (308, 110, 80, 80))
        pygame.display.update()
    elif shpearrange[2] == 3 or shpearrange[2] == 4:
        img = pygame.image.load(path_tooth)
        img.convert()
        rect_tooth = img.get_rect()
        rect_tooth.center = 350, 150
        WHITE = (255, 255, 255)
        pygame.draw.rect(screen, WHITE, rect_tooth, 1)
        screen.blit(img, rect_tooth)
        pygame.display.update()

        WHITE = (255, 255, 255)
        pygame.draw.rect(Window, WHITE, (308, 110, 80, 80))
        pygame.display.update()

    if shpearrange[3] == 1 or shpearrange[3] == 2:
        pygame.draw.polygon(Window, color_diamond, ((410, 150), (450, 120), (490, 150), (450, 180)))

        WHITE = (255, 255, 255)
        pygame.draw.rect(Window, WHITE, (408, 110, 80, 80))
        pygame.display.update()
    elif shpearrange[3] == 3 or shpearrange[3] == 4:
        img = pygame.image.load(path_tooth)
        img.convert()
        rect_tooth = img.get_rect()
        rect_tooth.center = 450, 150
        WHITE = (255, 255, 255)
        pygame.draw.rect(screen, WHITE, rect_tooth, 1)
        screen.blit(img, rect_tooth)
        pygame.display.update()

        WHITE = (255, 255, 255)
        pygame.draw.rect(Window, WHITE, (408, 110, 80, 80))
        pygame.display.update()
    return


def show(shpearrange, mouse_position, flag):
    rectanglenumber = findrecNumber(mouse_position)
    print('clicked on rectangle# ', rectanglenumber)
    random_obj = shpearrange
    print(random_obj)
    print('variable i is: ', i)
    pygame.display.update()
    if rectanglenumber == 1 and random_obj[rectanglenumber - 1] == 1:
        pygame.draw.polygon(Window, color_diamond, ((110, 150), (150, 120), (190, 150), (150, 180)))
        pygame.display.update()
        time.sleep(1)
    elif rectanglenumber == 1 and random_obj[rectanglenumber - 1] == 2:
        pygame.draw.polygon(Window, color_diamond, ((110, 150), (150, 120), (190, 150), (150, 180)))
        pygame.display.update()
        time.sleep(1)
    elif rectanglenumber == 2 and random_obj[rectanglenumber - 1] == 1:
        pygame.draw.polygon(Window, color_diamond, ((210, 150), (250, 120), (290, 150), (250, 180)))
        pygame.display.update()
        time.sleep(1)
    elif rectanglenumber == 2 and random_obj[rectanglenumber - 1] == 2:
        pygame.draw.polygon(Window, color_diamond, ((210, 150), (250, 120), (290, 150), (250, 180)))
        pygame.display.update()
        time.sleep(1)
    elif rectanglenumber == 3 and random_obj[rectanglenumber - 1] == 1:
        pygame.draw.polygon(Window, color_diamond, ((310, 150), (350, 120), (390, 150), (350, 180)))
        pygame.display.update()
        time.sleep(1)
    elif rectanglenumber == 3 and random_obj[rectanglenumber - 1] == 2:
        pygame.draw.polygon(Window, color_diamond, ((310, 150), (350, 120), (390, 150), (350, 180)))
        pygame.display.update()
        time.sleep(1)
    elif rectanglenumber == 4 and random_obj[rectanglenumber - 1] == 1:
        pygame.draw.polygon(Window, color_diamond, ((410, 150), (450, 120), (490, 150), (450, 180)))
        pygame.display.update()
        time.sleep(1)
    elif rectanglenumber == 4 and random_obj[rectanglenumber - 1] == 2:
        pygame.draw.polygon(Window, color_diamond, ((410, 150), (450, 120), (490, 150), (450, 180)))
        pygame.display.update()
        time.sleep(1)

    elif rectanglenumber == 1 and random_obj[rectanglenumber - 1] == 3:
        img = pygame.image.load(path_tooth)
        img.convert()
        rect_tooth = img.get_rect()
        rect_tooth.center = 150, 150
        WHITE = (255, 255, 255)
        pygame.draw.rect(screen, WHITE, rect_tooth, 1)
        screen.blit(img, rect_tooth)
        pygame.display.update()
        time.sleep(1)
    elif rectanglenumber == 1 and random_obj[rectanglenumber - 1] == 4:
        img = pygame.image.load(path_tooth)
        img.convert()
        rect_tooth = img.get_rect()
        rect_tooth.center = 150, 150
        WHITE = (255, 255, 255)
        pygame.draw.rect(screen, WHITE, rect_tooth, 1)
        screen.blit(img, rect_tooth)
        pygame.display.update()
        time.sleep(1)
    elif rectanglenumber == 2 and random_obj[rectanglenumber - 1] == 3:
        img = pygame.image.load(path_tooth)
        img.convert()
        rect_tooth = img.get_rect()
        rect_tooth.center = 250, 150
        WHITE = (255, 255, 255)
        pygame.draw.rect(screen, WHITE, rect_tooth, 1)
        screen.blit(img, rect_tooth)
        pygame.display.update()
        time.sleep(1)
    elif rectanglenumber == 2 and random_obj[rectanglenumber - 1] == 4:
        img = pygame.image.load(path_tooth)
        img.convert()
        rect_tooth = img.get_rect()
        rect_tooth.center = 250, 150
        WHITE = (255, 255, 255)
        pygame.draw.rect(screen, WHITE, rect_tooth, 1)
        screen.blit(img, rect_tooth)
        pygame.display.update()
        time.sleep(1)
    elif rectanglenumber == 3 and random_obj[rectanglenumber - 1] == 3:
        img = pygame.image.load(path_tooth)
        img.convert()
        rect_tooth = img.get_rect()
        rect_tooth.center = 350, 150
        WHITE = (255, 255, 255)
        pygame.draw.rect(screen, WHITE, rect_tooth, 1)
        screen.blit(img, rect_tooth)
        pygame.display.update()
        time.sleep(1)
    elif rectanglenumber == 3 and random_obj[rectanglenumber - 1] == 4:
        img = pygame.image.load(path_tooth)
        img.convert()
        rect_tooth = img.get_rect()
        rect_tooth.center = 350, 150
        WHITE = (255, 255, 255)
        pygame.draw.rect(screen, WHITE, rect_tooth, 1)
        screen.blit(img, rect_tooth)
        pygame.display.update()
        time.sleep(1)
    elif rectanglenumber == 4 and random_obj[rectanglenumber - 1] == 3:
        img = pygame.image.load(path_tooth)
        img.convert()
        rect_tooth = img.get_rect()
        rect_tooth.center = 450, 150
        WHITE = (255, 255, 255)
        pygame.draw.rect(screen, WHITE, rect_tooth, 1)
        screen.blit(img, rect_tooth)
        pygame.display.update()
        time.sleep(1)
    elif rectanglenumber == 4 and random_obj[rectanglenumber - 1] == 4:
        img = pygame.image.load(path_tooth)
        img.convert()
        rect_tooth = img.get_rect()
        rect_tooth.center = 450, 150
        WHITE = (255, 255, 255)
        pygame.draw.rect(screen, WHITE, rect_tooth, 1)
        screen.blit(img, rect_tooth)
        pygame.display.update()
        time.sleep(1)

    print('flag at show function is: ', flag)
    return rectanglenumber, random_obj


def findrecNumber(mouse_position):
    for i in range(4):
        if RectangleObjects[i].collidepoint(mouse_position):
            return i + 1


def rightchoice(firstchoice, secondchoice, rectnumchoice, rectnumchoice2, random_obj, flag):
    f = firstchoice
    s = secondchoice
    print('f is:', f)
    print('s is:', s)

    print('at rightchoice flag is:', flag)
    print('The first box you chose is: ', rectnumchoice)
    print('The second box you chose is: ', rectnumchoice2)
    print('The first choice you made is: ', random_obj[rectnumchoice - 1])
    print('The second choice you made is: ', random_obj[rectnumchoice2 - 1])

    if f[0] < 200 and s[0] < 200:
        end()
    elif f[0] < 300 and f[0] >= 200 and s[0] < 300 and s[0] >= 200:
        end()
    elif f[0] < 400 and f[0] >= 300 and s[0] < 400 and s[0] >= 300:
        end()
    elif f[0] > 525 or f[1] > 320 or s[0] > 525 or s[1] > 320:
        end()
    elif random_obj[rectnumchoice - 1] == 1 and random_obj[rectnumchoice2 - 1] == 2:
        # time.sleep(1)
        win()
    elif random_obj[rectnumchoice - 1] == 2 and random_obj[rectnumchoice2 - 1] == 1:
        # time.sleep(1)
        win()
    elif random_obj[rectnumchoice - 1] == 3 and random_obj[rectnumchoice2 - 1] == 4:
        # time.sleep(1)
        win()
    elif random_obj[rectnumchoice - 1] == 4 and random_obj[rectnumchoice2 - 1] == 3:
        # time.sleep(1)
        win()


    else:

        end()

    return


'''start game'''


def main():
    mx = 100
    my = 200
    pygame.mouse.set_pos([mx, my])
    mpos = pygame.mouse.get_pos()
    print('The current mouse positions is: ', mpos)
    pygame.init()

    myfont = pygame.font.SysFont('comicsansms', 22, True)
    textsurface = myfont.render('Find the gold or diamonds !', False, (204, 229, 255))
    Window.blit(textsurface, (20, 550))
    pygame.display.update()

    flag = 0

    while flag == 0 or flag == 1:
        choice_array = np.array([])
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                pygame.display.update()
                if flag == 0:
                    firstchoice = mouse_position
                    show(shpearrange, mouse_position, flag)
                    rectanglenumber, random_obj = show(shpearrange, mouse_position, flag)
                    rectnumchoice = rectanglenumber

                    flag = 1
                else:
                    secondchoice = mouse_position
                    show(shpearrange, mouse_position, flag)
                    rectanglenumber, random_obj = show(shpearrange, mouse_position, flag)
                    rectnumchoice2 = rectanglenumber

                    print('rectangle number is:', show, 'random object is:', show)

                    print('rectangle #1 is: ', rectnumchoice)
                    print('rectangle #2 is: ', rectnumchoice2)
                    print('random _obj is: ', random_obj)

                    rightchoice(firstchoice, secondchoice, rectnumchoice, rectnumchoice2, random_obj, flag)


def end():
    pygame.display.update()
    WHITE = (255, 255, 255)
    pygame.draw.rect(screen, WHITE, (0, 0, 2000, 2000))
    myfont = pygame.font.SysFont('comicsansms', 40, True)
    textsurface = myfont.render('TRY AGAIN', False, (200, 229, 155))
    Window.blit(textsurface, (150, 250))
    pygame.display.update()
    time.sleep(1)
    pygame.quit()
    sys.exit()


def win():
    print(' You win !!')
    pygame.display.update()
    WHITE = (255, 255, 255)
    pygame.draw.rect(screen, WHITE, (0, 0, 2000, 2000))
    myfont = pygame.font.SysFont('comicsansms', 40, True)
    textsurface = myfont.render('YOU WIN !!!! YOU WIN !!!! YOU FOUND THE TREASURE!!!!', False, (200, 229, 155))
    Window.blit(textsurface, (150, 250))
    pygame.display.update()


if __name__ == '__main__':
    main()

'''end game'''

'''from collections import namedtuple
def profile():
    Person = namedtuple('Person', 'name age')
    return Person(name="Danny", age=31)
# Use as namedtuple
p = profile()
print(p, type(p))
# Person(name='Danny', age=31) <class '__main__.Person'>
print(p.name)
# Danny
print(p.age)
#31
# Use as plain tuple
p = profile()
print(p[0])
# Danny
print(p[1])
#31
# Unpack it immediatly
name, age = profile()
print(name)
# Danny
print(age)
#31
def profile():
    name = "Danny"
    age = 30
    return (name, age)
profile_data = profile()
print(profile_data[0])
# Output: Danny
print(profile_data[1])
# Output: 30
'''
@fovanessians
 
