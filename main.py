import pygame
from sys import exit

#Start everything and settings
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True

#Display
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surface = test_font.render('Score:', False, (64, 64, 64))
score_rect = score_surface.get_rect(center = (400, 50))


#EnemyNPCs
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (0, 300))

#Player
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (100 , 300))
player_gravity = 0

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #If player presses "X" button, game will close
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:  #if player presses "ESC" button, game will close
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:  #Jumping with Clicks
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: 
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:    #Jumping with SPACE mechanic
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                game_active = True
                snail_rect.left = 800


    if game_active:
        #blits for background
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        pygame.draw.rect(screen, '#c0e8ec', score_rect)
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        screen.blit(score_surface, score_rect)

        #blits for snail
        screen.blit(snail_surface, snail_rect)
        snail_rect.left -= 4
        if snail_rect.left < -80: snail_rect.left = 800  #respawn the snail after leaving the map
        
        #blits for player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300 : player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        #collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('yellow')
        



    
    
    pygame.display.update()
    clock.tick(60)