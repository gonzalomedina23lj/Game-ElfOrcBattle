import pygame, random

pygame.init()

#DISPLAY
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 450
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("ElfOrc BaTTle!")

#COLORES
DARKRED = (179,53,30)
GREEN = (0,255,0)
DARKGREEN = (10,50,10)
AMARILLO = (207,111,51)
WHITE = (255,255,255)
BLACK = (0,0,0)
COLOR_FONDO = (220,220,220)

#CUADROS POR SEGUNDO
FPS = 60
clock = pygame.time.Clock()

VELOCITY = 5 #Sólo para prueba
#VARIABLES CONSTANTES
PLAYER_STARTING_LIVES = 3
PLAYER_VELOCITY = 10
ARROW_STARTING_VELOCITY = 5
FIREBALL_STARTING_VELOCITY = 15
ARROW_ACCELERATION = .5
FIREBALL_ACCELERATION = .5
BUFFER_DISTANCE = 100

score = 0
elf_lives = PLAYER_STARTING_LIVES
orc_lives = PLAYER_STARTING_LIVES
arrow_velocity = ARROW_STARTING_VELOCITY
fireball_velocity =  FIREBALL_STARTING_VELOCITY

#MÚSICA Y SONIDOS
sound_1 = pygame.mixer.Sound('sounds/intro_sound.wav')
sound_2 = pygame.mixer.Sound('sounds/arc_sound_impact.wav')
sound_3 = pygame.mixer.Sound('sounds/explosion_sound_impact.wav')

#FUENTE Y TEXTO
system_font=pygame.font.SysFont('fonts/meiryomeiryoboldmeiryouiboldmeiryouibolditalic', 58) #fuente que se encuentra en el sistema
custom_font=pygame.font.Font('fonts/RademosRegular.ttf', 58)
custom_font_2=pygame.font.Font('fonts/RademosRegular.ttf', 38)

tittle_text=custom_font.render("ElfOrc Battle", True, DARKRED)
tittle_rect=tittle_text.get_rect()
tittle_rect.center=(WINDOW_WIDTH//2, 40)

orc_lives_text = custom_font_2.render("Lives: " + str (orc_lives), True, BLACK, AMARILLO)
orc_lives_rect = orc_lives_text.get_rect()
orc_lives_rect.topright = (WINDOW_WIDTH - 40, 16)

elf_lives_text = custom_font_2.render ("Lives: " + str (elf_lives), True, BLACK, AMARILLO)
elf_lives_rect = elf_lives_text.get_rect()
elf_lives_rect.topleft = (40 , 16)

game_over_text = custom_font.render("GAMEOVER", True, DARKRED, AMARILLO)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//3)

continue_text = custom_font.render("Press any key to play again", True, DARKRED, AMARILLO)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 32)

#PERSONAJES Y ARMAS
elf_image = pygame.image.load("images/elf_image.png")
elf_rect = elf_image.get_rect()
elf_rect.topleft = (0,175)

elf_image_pain = pygame.image.load("images/elf_image_pain.png")
elf_pain_rect = elf_image_pain.get_rect()
elf_pain_rect.topleft = (0,175)

orc_image = pygame.image.load("images/orc_image.png")
orc_rect = orc_image.get_rect()
orc_rect.topright = (WINDOW_WIDTH,175)

orc_fireball_image = pygame.image.load("images/fireball_orc.png")
orc_fireball_rect = orc_fireball_image.get_rect()
orc_fireball_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
orc_fireball_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

elf_arrow_image = pygame.image.load("images/arrow_elf2.png")
elf_arrow_rect = elf_arrow_image.get_rect()
elf_arrow_rect.topleft = (46,180)

#FONDO Y HUD
hud_line = pygame.image.load("images/lineadiv2.png")
hud_rect = hud_line.get_rect()
hud_rect.midtop = (450,60)

crack_image = pygame.image.load("images/crack3.png")
crack_rect = crack_image.get_rect()
crack_rect.center = (450,290)

#fondo = pygame.image.load("images/fondo.png")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Movimiento Elfo
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and elf_rect.left > 0:
        elf_rect.x -= VELOCITY
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and elf_rect.right < (WINDOW_WIDTH//2):
        elf_rect.x += VELOCITY
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and elf_rect.top > 50:
        elf_rect.y -= VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and elf_rect.bottom < WINDOW_HEIGHT:
        elf_rect.y += VELOCITY

    if (keys[pygame.K_SPACE]) and elf_arrow_rect.right < (WINDOW_WIDTH):
        elf_arrow_rect.x += VELOCITY
    
    #Movimiento Bola de Fuego
    if orc_fireball_rect.x < 0:
        orc_fireball_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        orc_fireball_rect.y = random.randint(64, WINDOW_HEIGHT - 64)
    else:
        orc_fireball_rect.x -= fireball_velocity

    if elf_rect.colliderect(orc_fireball_rect):
        sound_3.play()
        display_surface.blit(elf_image_pain, elf_pain_rect)
        orc_fireball_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        orc_fireball_rect.y = random.randint(64, WINDOW_HEIGHT - 64)
        elf_lives -= 1

    #Update HUD
    elf_lives_text = custom_font_2.render("Lives: " + str (elf_lives), True, BLACK, AMARILLO)

    if elf_lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    elf_lives = PLAYER_STARTING_LIVES
                    elf_rect.topleft = (0,175)
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False
    
    display_surface.fill((0,0,0))

    #Personajes y Rectángulos
    pygame.draw.rect(display_surface, (255,0,0), elf_rect,1)
    pygame.draw.rect(display_surface, (255,0,0), orc_rect,1)

    #FONDO
    #display_surface.blit(fondo,(0,-13))
    
    #BLITTING HUD
    display_surface.blit(tittle_text, tittle_rect)
    display_surface.blit(elf_lives_text, elf_lives_rect)
    display_surface.blit(orc_lives_text, orc_lives_rect)
    display_surface.blit(crack_image, crack_rect)
    display_surface.blit(hud_line, hud_rect)
    
    #BLITTING PERSONAJES Y ARMAS
    display_surface.blit(elf_image, elf_rect)
    display_surface.blit(orc_image, orc_rect)
    display_surface.blit(orc_fireball_image, orc_fireball_rect)
    
    #Update display
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
