import pygame

pygame.init()

black = (0,0,0)
white = (255,255,255)


width,height = 600, 500
screen = pygame.display.set_mode((width , height))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(white)
pygame.display.update()


radius = 40

running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:

            #ROW1
            if pygame.mouse.get_pos()[0] < width/3 and pygame.mouse.get_pos()[1] < height/3:
                pygame.draw.circle(screen, black, ( int((width/3)/2), int((height/3)/2) ) , radius, 1) 
                pygame.draw.line(screen ,black , (0,0), (width/3, height/3),1) 
                pygame.draw.line(screen ,black , (width/3, 0), (0, height/3),1)
                print(1)
            if pygame.mouse.get_pos()[0] > width/3 and pygame.mouse.get_pos()[0] < (width/3)*2 and pygame.mouse.get_pos()[1] < height/3:
                pygame.draw.circle(screen, black, ( int(width/2), int((height/3)/2) ) , radius, 1) 
                pygame.draw.line(screen ,black , (width/3,0), ((width/3)*2, height/3),1) 
                pygame.draw.line(screen ,black , ((width/3)*2, 0), (width/3, height/3),1)
                print(2)
            if pygame.mouse.get_pos()[0] > (width/3)*2 and pygame.mouse.get_pos()[1] < height/3: 
                pygame.draw.circle(screen, black, ( int(((width/3)*2)+((width/3)/2)), int((height/3)/2) ) , radius, 1)
                pygame.draw.line(screen ,black , ((width/3)*2,0), (width, height/3),1) 
                pygame.draw.line(screen ,black , (width, 0), ((width/3)*2, height/3),1) 
                print(3)
            
            #ROW2
            if pygame.mouse.get_pos()[0] < width/3 and pygame.mouse.get_pos()[1] > height/3 and pygame.mouse.get_pos()[1] < (height/3)*2: 
                pygame.draw.circle(screen, black, ( int((width/3)/2), int(height/2) ) , radius, 1)  
                pygame.draw.line(screen ,black , (0,height/3), (width/3, (height/3)*2),1) 
                pygame.draw.line(screen ,black , (width/3, height/3), (0, (height/3)*2),1) 
                print(4)
            if pygame.mouse.get_pos()[0] > width/3 and pygame.mouse.get_pos()[0] < (width/3)*2 and pygame.mouse.get_pos()[1] > height/3 and pygame.mouse.get_pos()[1] < (height/3)*2:
                pygame.draw.circle(screen, black, ( int(width/2), int(height/2) ) , radius, 1) 
                pygame.draw.line(screen ,black , (width/3,height/3), ((width/3)*2, (height/3)*2),1) 
                pygame.draw.line(screen ,black , ((width/3)*2, height/3), (width/3,(height/3)*2),1)
                print(5)
            if pygame.mouse.get_pos()[0] > (width/3)*2 and pygame.mouse.get_pos()[1] > height/3 and pygame.mouse.get_pos()[1] < (height/3)*2:
                pygame.draw.circle(screen, black, ( int(((width/3)*2)+((width/3)/2)), int(height/2) ) , radius, 1)
                pygame.draw.line(screen ,black , ((width/3)*2,height/3), (width, (height/3)*2),1) 
                pygame.draw.line(screen ,black , (width, height/3), ((width/3)*2,(height/3)*2),1) 
                print(6)
            
            #ROW3
            if pygame.mouse.get_pos()[0] < width/3 and pygame.mouse.get_pos()[1] > (height/3)*2:
                pygame.draw.circle(screen, black, ( int((width/3)/2), int(((height/3)*2)+((height/3)/2))) , radius, 1)
                pygame.draw.line(screen ,black , (0, (height/3)*2), (width/3, height),1) 
                pygame.draw.line(screen ,black , (width/3, (height/3)*2), (0, height),1)
                print(7)
            if pygame.mouse.get_pos()[0] > width/3 and pygame.mouse.get_pos()[0] < (width/3)*2 and pygame.mouse.get_pos()[1] > (height/3)*2:
                pygame.draw.circle(screen, black, ( int(width/2), int(((height/3)*2)+((height/3)/2)))  , radius, 1)
                pygame.draw.line(screen ,black , (width/3,(height/3)*2), ((width/3)*2, height),1) 
                pygame.draw.line(screen ,black , ((width/3)*2, (height/3)*2), (width/3, height),1)
                print(8)
            if pygame.mouse.get_pos()[0] > (width/3)*2 and pygame.mouse.get_pos()[1] > (height/3)*2:
                pygame.draw.circle(screen, black, ( int(((width/3)*2)+((width/3)/2)),int(((height/3)*2)+((height/3)/2)))  , radius, 1)
                pygame.draw.line(screen ,black , ((width/3)*2,(height/3)*2), (width, height),1) 
                pygame.draw.line(screen ,black , (width, (height/3)*2), ((width/3)*2, height),1) 
                print(9)
    
    
    #Vertical Lines
    pygame.draw.line(screen ,black , (width/3, 0), (width/3, height),1)
    pygame.draw.line(screen ,black , ((width/3)*2, 0), ((width/3)*2, height),1)
    #horizontal Lines
    pygame.draw.line(screen ,black , (0, height/3), (width, height/3),1)
    pygame.draw.line(screen ,black , (0, (height/3)*2), (width, (height/3)*2),1)
    pygame.display.update()


