import pygame
size = width, height = (640, 480)
screen = pygame.display.set_mode(size)
fps = pygame.time.Clock()
pygame.init()
font = pygame.font.SysFont(None, 30)

#Процедура рисования кнопк меню
def  drawButton(x_button, y_button, width_button, height_button, stroka):
    color = pygame.Color(50, 150, 150)
    pygame.draw.rect(screen, color, (x_button+3, y_button+3, width_button, height_button), 0)
    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], hsv[2]+30, hsv[3])
    pygame.draw.rect(screen, color, (x_button, y_button, width_button, height_button), 0)
    color.hsva = (hsv[0], hsv[1], hsv[2], hsv[3])
    pygame.draw.rect(screen, color, (x_button, y_button, width_button, height_button), 3)
    font = pygame.font.SysFont('timesnewroman', 30, bold = True, italic = False)
    text = font.render(stroka, 0, (255, 0, 0))
    dx = width_button//2 - text.get_width()//2
    dy = height_button//2 - text.get_height()//2
    screen.blit(text, (x_button + dx, y_button + dy))

#Функция нажатия кнопки меню    
def clickButton(dy):
    return pos_mouse[0]>x_button and pos_mouse[0]<x_button+width_button and pos_mouse[1]>y_button+dy and pos_mouse[1]<y_button+dy+height_button and buttons_mouse[0]

#Процедура рисования строки текста справки
def drawText(stroka, dy, size_font):
    font = pygame.font.SysFont('timesnewroman', 20, bold = True, italic = False)
    text = font.render(stroka, 0, (255, 0, 0))
    dx = width//2 - text.get_width()//2
    screen.blit(text, (dx, dy))


#блок
class Block():
    def __init__(self, x, y, w, h, visible, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.visible = visible
        self.color = color
        
    def draw(self):
        if self.visible:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h), 0)

#платформа            
class Platform():
    def __init__(self, x, y, w, h, speed):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        
        
    def draw(self):
            pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.w, self.h), 0)
            

#шарик            
class Ball():
    def __init__(self, x, y, r, vx, vy):
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.vy = vy
        
    def draw(self):
        pygame.draw.circle(screen, 'red', (x, y), r, 0)        
               
        
        
        
        
    def draw(self):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.r, 0)

#создание блоков
color_list = ['Red', 'Orange', 'Yellow', 'Green',  'Cyan', 'Blue', 'Violet', 'Pink']
blocks_list = []
num_color = 0
for x in range(50, 600, 70):
    blocks_list.append(Block(x, 20, 60, 30, True, color_list[num_color]))
    num_color += 1

num_color = 0    
for x in range(80, 600-70, 70):
    blocks_list.append(Block(x, 60, 60, 30, True, color_list[num_color]))
    num_color += 1 
    
num_color = 0
for x in range(50, 600, 70):
    blocks_list.append(Block(x, 100, 60, 30, True, color_list[num_color]))
    num_color += 1 
    
num_color = 0
for x in range(80, 600-70, 70):
    blocks_list.append(Block(x, 140, 60, 30, True, color_list[num_color]))
    num_color += 1 
    
num_color = 0
for x in range(50, 600, 70):
    blocks_list.append(Block(x, 180, 60, 30, True, color_list[num_color]))
    num_color += 1 

num_color = 0
for x in range(80, 600-70, 70):
    blocks_list.append(Block(x, 220, 60, 30, True, color_list[num_color]))
    num_color += 1 

 
#сщздание игрока
gamer = Platform(250, 440, 100, 10, 35)

#создание шарика
ball = Ball(300, 430, 10, 0, 0)

#Переменная кнопок
width_button = 200
height_button = 50
x_button = width//2 - width_button//2
y_button = 200
dy_button1 = 0
dy_button2 = 60
dy_button3 = 120

#Переменные старниц меню
PAGE = 'menu'
color_bg = 'Green'


fall = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        keyboard = pygame.key.get_pressed()
        buttons_mouse = pygame.mouse.get_pressed()
        pos_mouse = pygame.mouse.get_pos()                
            
        #Управление платформой
        if keyboard[pygame.K_LEFT]:
            gamer.x -= gamer.speed
        if keyboard[pygame.K_RIGHT]:
            gamer.x += gamer.speed 
        #запуск шарика
        if keyboard[pygame.K_SPACE]:
            ball.vx = 3
            ball.vy = -3
            fall = True
        
            
    screen.fill('White')
    
    #Страницца меню
    if PAGE == 'menu':
        drawButton(x_button, y_button+dy_button1 , width_button, height_button, 'start')
        drawButton(x_button, y_button+dy_button2 , width_button, height_button, 'help')
        drawButton(x_button, y_button+dy_button3, width_button,height_button, 'exit') 
            
        if clickButton(dy_button1):     
            PAGE = 'game'            
        if clickButton(dy_button2):
            PAGE = 'help'            
        if clickButton(dy_button3):   
            PAGE = 'exit'
            
            
    #Страница справки        
    if PAGE == 'help' :
        color_bg = 'Light Blue'
        if keyboard[pygame.K_ESCAPE]:
            PAGE = 'menu'
            color_bg = 'White'
                
        drawText("Правила игры", 50, 30)
        drawText("Управление платформа", 100, 20)
        drawText("Платформа - левая стрелочка и правая. ", 130, 20)
        drawText("Игра ведется пока не сломаете все блоки", 150, 20)
        drawText("Чтобы шарик задвигался то нажмите пробел", 300, 20)
        drawText("Выход в меню - 'ESC'", 450, 20) 
            
    #Выход    
    if PAGE == 'exit' :
        run = False 
        
    #Страница игры       
    if PAGE == 'game' :  
        if keyboard[pygame.K_ESCAPE]:
            PAGE = 'menu'
            color_bg = 'White'
            
    #if PAGE == 'game2' :  
        if keyboard[pygame.K_ESCAPE]:
            PAGE = 'menu'
            color_bg = 'Azure'    

        #Рисование блоков
        for i in range(len(blocks_list)):
            blocks_list[i].draw()
        
        #Рисование игрока
        gamer.draw()
        
        #Рисование шарика
        ball.draw()
        if fall:
            ball.x+=ball.vx
            ball.y+=ball.vy 
        else:
            ball.x = gamer.x+gamer.w/2
        
        #условие проигрыша
        if ball.y+ball.r>height:
            ball.vy=0
            ball.vx=0
        
        #условие отскока от верхней границы    
        if ball.y-ball.r<0:
            ball.vy=-ball.vy     
        
        #условие отскока от боковых границ    
        if ball.x+ball.r>width or ball.x-ball.r<0:
            ball.vx=-ball.vx 
            
        #условие отскока от платформы
        if ball.x+ball.r>gamer.x and ball.x-ball.r<gamer.x+gamer.w and ball.y+ball.r>gamer.y and ball.y-ball.r<gamer.y+gamer.h:
            ball.vy=-ball.vy    
        
        #условие столкновения с блоками
        for i in range(len(blocks_list)):
            if ball.x+ball.r>blocks_list[i].x and ball.x-ball.r<blocks_list[i].x+blocks_list[i].w and ball.y+ball.r>blocks_list[i].y and ball.y-ball.r<blocks_list[i].y+blocks_list[i].h and blocks_list[i].visible==True:
                ball.vy=-ball.vy
                blocks_list[i].visible=False
                
    
    pygame.display.flip()
    fps.tick(60)
pygame.quit()