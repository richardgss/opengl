# Nome: Richard Garcia de Souza
# RA: 32216450

import pygame
import sys

pygame.init()

WIDTH = 1200
HEIGHT = 800


RED = (255, 0, 0)
GREEN = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Rectangles
rect1 = pygame.Rect(0,(HEIGHT-50), (WIDTH), 50)
rect2 = pygame.Rect((WIDTH*0.4),((HEIGHT-50)-200), 100, 200)
# define a surface (RECTANGLE)
image_braco = pygame.Surface((100 , 100))

rectMove = pygame.Rect((WIDTH*0.4),((HEIGHT-50)-200), 100, 200)
rect1_speed = pygame.Vector2(0, 0)
rect2_speed = pygame.Vector2(0, 0)

# define a surface (RECTANGLE)
image_braco = pygame.Surface((300, 80))
# for making transparent background while rotating an image
image_braco.set_colorkey(RED)
# fill the rectangle / surface with green color
image_braco.fill(GREEN)
# define rect for placing the rectangle at the desired position
rectBraco = image_braco.get_rect()
rectBraco.center = (WIDTH // 2 +73 , HEIGHT // 2 -78)


# define a surface (RECTANGLE)
image_mao = pygame.Surface((25, 150))
# for making transparent background while rotating an image
image_mao.set_colorkey(RED)
# fill the rectangle / surface with green color
image_mao.fill(GREEN)
# define rect for placing the rectangle at the desired position
rectmao = image_mao.get_rect()
rectmao.center = (WIDTH // 2 +120, HEIGHT // 2 -80)


# define a surface (RECTANGLE)
image_dedo_1 = pygame.Surface((70, 20))
# for making transparent background while rotating an image
image_dedo_1.set_colorkey(RED)
# fill the rectangle / surface with green color
image_dedo_1.fill(GREEN)
# define rect for placing the rectangle at the desired position
rectdado_1 = image_dedo_1.get_rect()
rectdado_1.center = (WIDTH // 2 +235, HEIGHT // 2 -130)

# define a surface (RECTANGLE)
image_dedo_2 = pygame.Surface((70, 26))
# for making transparent background while rotating an image
image_dedo_2.set_colorkey(RED)
# fill the rectangle / surface with green color
image_dedo_2.fill(GREEN)
# define rect for placing the rectangle at the desired position
rectdado_2 = image_dedo_2.get_rect()
rectdado_2.center = (WIDTH // 2 +180, HEIGHT // 2 -160)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()

        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_LEFT:
            #    rect1_speed.x = -5
            # elif event.key == pygame.K_RIGHT:
            #    rect1_speed.x = 5
            # elif event.key == pygame.K_UP:
            #    rect1_speed.y = -5
            # elif event.key == pygame.K_DOWN:
            #    rect1_speed.y = 5

            if event.key == pygame.K_a:
               rect2_speed.x = -5
            elif event.key == pygame.K_d:
               rect2_speed.x = 5
            elif event.key == pygame.K_w:
               rect2_speed.y = -5
            elif event.key == pygame.K_s:
               rect2_speed.y = 5

        if event.type == pygame.KEYUP:
            # if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #    rect1_speed.x = 0
            # elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #    rect1_speed.y = 0

            if event.key == pygame.K_a or event.key == pygame.K_d:
               rect2_speed.x = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
               rect2_speed.y = 0
    # Move rectangles
   #  rect1.move_ip(rect1_speed)
    rect2.move_ip(rect2_speed)

    # Check for collision
    if rect1.colliderect(rect2):
        rect_color = RED
    else:
        rect_color = GREEN

    # Draw rectangles
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, rect_color, rect1)
    pygame.draw.rect(screen, rect_color, rect2)
    # drawing the rotated rectangle to the screen
    screen.blit(pygame.transform.rotate(image_braco,45) , rectBraco)
    screen.blit(pygame.transform.rotate(image_mao,45) , rectmao)
    screen.blit(pygame.transform.rotate(image_dedo_1,60) , rectdado_1)
    screen.blit(pygame.transform.rotate(image_dedo_1,25) , rectdado_2)
    # flipping the display after drawing everything
    pygame.display.flip()
    clock.tick(60)