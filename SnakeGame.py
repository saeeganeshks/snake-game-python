import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
blue2 = (0, 0, 139, 255)

bound = 50 
dis_width = 500
dis_height = 500
 
dis = pygame.display.set_mode((dis_width+bound,dis_height+bound))
pygame.display.set_caption('Snake Game')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("Helvetica", 25)
score_font = pygame.font.SysFont("Times", 35)
 
 
def Score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
def Snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [bound, dis_height/2])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    dotx1 = round(random.randrange(bound, dis_width - snake_block) / 10.0) * 10.0
    doty1 = round(random.randrange(bound, dis_height - snake_block) / 10.0) * 10.0

    dotx2 = round(random.randrange(bound, dis_width - snake_block) / 10.0) * 10.0
    doty2 = round(random.randrange(bound, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue2)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < bound or y1 >= dis_height or y1 < bound:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue2)
        pygame.draw.rect(dis,blue,(bound,bound,dis_width-bound,dis_height-bound))
        pygame.draw.rect(dis, green, [dotx1, doty1, snake_block, snake_block])
        pygame.draw.rect(dis, green, [dotx2, doty2, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        Snake(snake_block, snake_List)
        Score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == dotx1 and y1 == doty1:
            dotx1 = round(random.randrange(bound, dis_width - snake_block) / 10.0) * 10.0
            doty1 = round(random.randrange(bound, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        elif x1 == dotx2 and y1 == doty2:
            dotx2 = round(random.randrange(bound, dis_width - snake_block) / 10.0) * 10.0
            doty2 = round(random.randrange(bound, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()