import pygame
import random

pygame.init()

WIDTH, HEIGHT = 300, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower blox")

clock = pygame.time.Clock()
FPS = 120

WHITE = (255, 255, 255)
Black = (0, 0, 0)

block_image = pygame.image.load("block.png")
block_image =  pygame.transform.scale(block_image, (50, 50))

block_width, block_height = 50, 50
block_x = WIDTH // 2 - block_width // 2
block_y = 50
block_speed = 2
block_direction = 1
block_falling = False

tower = [[WIDTH // 2 - block_width //2, HEIGHT - block_height]]
tower_falling = False
scroll_speed = 0.7

score = 0
font = pygame.font.Font(None, 36)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            block_falling = True

    if block_falling:
        block_y += block_speed


        upper_block = pygame.Rect(tower[-1 ][0], tower[-1][1], block_width, block_height)
        if pygame.Rect(block_x, block_y, block_width, block_height).colliderect(upper_block):
            block_falling = False
            tower.append([block_x, block_y])
            block_y = 50
            score += 1

        else:
            for block in tower[:-1]:
                lower_blocks = pygame.Rect(block[0], block[1], block_width, block_height)
                if pygame.Rect(block_x, block_y, block_width, block_height).colliderect(lower_blocks):
                    tower_falling = True
                    break
            if block_y + block_height > HEIGHT:
                run = False
                print("GAME OVER YOU SUCKER")

    else:
        block_x += block_speed * block_direction
        if block_x + block_width > WIDTH or block_x < 0:
            block_direction *=-1
        if len(tower) > 4:
            for block in tower:
                block[1] += scroll_speed
        if tower_falling:
            for block in tower:
                block[0] += block_speed

    screen.fill(WHITE)
    for block in tower:
        screen.blit(block_image, (block[0], block[1]))
    screen.blit(block_image,(block_x, block_y))

    score_label = font.render(f"Score: {score}", True, Black)
    screen.blit(score_label, (20, 20))

    pygame.display.flip()
    clock.tick(FPS)