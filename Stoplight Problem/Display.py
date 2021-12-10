import pygame, sys
import Intersection
class Model:
    _intersection = None
    def __init__(self):
         self._intersection = Intersection.Intersection(0,[[False, False],[False, False],[False, False],[False, False],[False, False],[False, False],[False, False],[False, False]])

    def step(self, i):
        front = self._intersection._locations[i][-1]
        if front == None:
            return
        if self._intersection.green(front):
            self.vroom(i)

    def vroom(self,i):
        self._intersection._locations[i].pop(0)
        
m = Model()
for e in range(100):
    m._intersection.add_random_car(0.5)
pygame.init()
WIDTH = 1000
HEIGHT = 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 1
pygame.display.set_caption('Stoplight Simulation :)')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

SCREEN.fill(BLACK)
pygame.display.flip()
size = (20, 225)
size1 = (225, 20)

dashed_lines = pygame.Surface((10, 60))
pygame.draw.rect(dashed_lines, WHITE, dashed_lines.get_rect())
SCREEN.blit(dashed_lines, (400, 100))
SCREEN.blit(dashed_lines, (400, 180))
SCREEN.blit(dashed_lines, (400, 260))
SCREEN.blit(dashed_lines, (400, 675))
SCREEN.blit(dashed_lines, (400, 755))
SCREEN.blit(dashed_lines, (400, 835))

dashed_lines1 = pygame.Surface((60,10))
pygame.draw.rect(dashed_lines1, WHITE, dashed_lines1.get_rect())
SCREEN.blit(dashed_lines1, (95, 411))
SCREEN.blit(dashed_lines1, (175, 411))
SCREEN.blit(dashed_lines1, (255, 411))
SCREEN.blit(dashed_lines1, (95, 582))
SCREEN.blit(dashed_lines1, (175, 582))
SCREEN.blit(dashed_lines1, (255, 582))

SCREEN.blit(dashed_lines, (600, 100))
SCREEN.blit(dashed_lines, (600, 180))
SCREEN.blit(dashed_lines, (600, 260))
SCREEN.blit(dashed_lines, (600, 675))
SCREEN.blit(dashed_lines, (600, 755))
SCREEN.blit(dashed_lines, (600, 835))

SCREEN.blit(dashed_lines1, (700, 411))
SCREEN.blit(dashed_lines1, (780, 411))
SCREEN.blit(dashed_lines1, (860, 411))
SCREEN.blit(dashed_lines1, (700, 582))
SCREEN.blit(dashed_lines1, (780, 582))
SCREEN.blit(dashed_lines1, (860, 582))

boundaries = pygame.Surface(size)
pygame.draw.rect(boundaries, YELLOW, boundaries.get_rect())   
SCREEN.blit(boundaries, (300,100))
SCREEN.blit(boundaries, (500,100))
SCREEN.blit(boundaries, (700, 100))
SCREEN.blit(boundaries, (300,675))
SCREEN.blit(boundaries, (500,675))
SCREEN.blit(boundaries, (700, 675))

boundaries1 = pygame.Surface(size1)
pygame.draw.rect(boundaries1, YELLOW, boundaries1.get_rect())
SCREEN.blit(boundaries1, (700,325))
SCREEN.blit(boundaries1, (700,497))
SCREEN.blit(boundaries1, (700,670))
SCREEN.blit(boundaries1, (95,325))
SCREEN.blit(boundaries1, (95,497))
SCREEN.blit(boundaries1, (95,670))
def draw_car(j):
    q = m._intersection._locations[j]
    number_of_cars = len(q)
    vertical = False
    size = (80,40)
    if(j) == 0:
       position = (535,675)
       vertical = True
    elif j==1:
        position = (640,675)
        vertical = True
    elif j==2:
        position = (700, 440)
    elif j==3:
        position = (700, 360)
    elif j==4:
        position = (440,265)
        vertical = True
    elif j==5:
        position = (340,265)
        vertical = True
    elif j==6:
        position = (240,525)
    elif j==7:
        position = (240, 618)
    if vertical: size = (40, 80)

    font_obj = pygame.font.SysFont('arial', 30)
    text_surface_obj = font_obj.render(str(number_of_cars), False, WHITE, BLUE)
    if (number_of_cars == 0):
        pygame.draw.rect(SCREEN, BLACK, (position, size))
    else:
        pygame.draw.rect(SCREEN, BLUE, (position, size))
        SCREEN.blit(text_surface_obj, (position))
    
def s_switch(j):
    vertical = False
    #ORIENTATION AND POSITION ASSIGNMENT
    if j==0:
        position = (545,30)
        vertical = True
        light1_pos = (565, 50)
        light2_pos = (565, 90)
    elif j==1:
        position = (640,30)
        vertical = True
        light1_pos = (660,50)
        light2_pos = (660, 90)
    elif j==2:
        position = (10, 440)
        light1_pos = (30,460)
        light2_pos = (70,460)
    elif j==3:
        position = (10, 360)
        light1_pos = (30, 380)
        light2_pos = (70, 380)
    elif j==4:
        position = (440,900)
        vertical = True
        light2_pos = (460,920)
        light1_pos = (460,960)
    elif j==5:
        position = (340,900)
        vertical = True
        light2_pos = (360, 920)
        light1_pos = (360, 960)
    elif j==6:
        position = (925,525)
        light2_pos = (945, 545)
        light1_pos = (985,545)
    elif j==7:
        position = (925, 618)
        light2_pos = (945, 638)
        light1_pos = (985, 638)
    size = (80,40)
    if(vertical): size = (40,80)
    #LIGHT COLORING
    color1 = RED 
    if(m._intersection._stoplights[j][0]):
        color1 = GREEN
    color2 = RED
    if (m._intersection._stoplights[j][1]):
        color2 = GREEN

    
    
    pygame.draw.rect(SCREEN, WHITE, (position, size))
    pygame.draw.circle(SCREEN, color1, light1_pos,20)
    pygame.draw.circle(SCREEN,color2,light2_pos,20)
    #SCREEN.blit(light_box, position)
    #SCREEN.blit(light1,light1_pos)
    #SCREEN.blit(light2,light2_pos)
    

is_running = True
while is_running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    for j in range(8):
        s_switch(j)
        m.step(j)
        draw_car(j)
        
    pygame.display.update()
    draw_car(0)
    m._intersection.stoplight_update()
    clock.tick(FPS)

pygame.quit()
