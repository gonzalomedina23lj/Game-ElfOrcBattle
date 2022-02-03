from unittest.mock import seal
import pygame 
import random
import math
import sys
pygame.init()

#DISPLAY
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 450
TILESIZE = 32
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("ElfOrc BaTTle!")

#CUADROS POR SEGUNDO
FPS = 60
clock = pygame.time.Clock()

#CLASES JUEGO
class Game():
    
    def __init__(self, player_elf, enemy_orc, orc_attack_group, elf_attack_group):
        
        #Valores del juego
        self.player_elf = player_elf
        self.enemy_orc = enemy_orc
        self.elf_attack_group = elf_attack_group
        self.orc_attack_group = orc_attack_group

        #Sonidos y música
        self.intro_sound = pygame.mixer.Sound('sounds/intro_sound.wav')
        self.arc_impact = pygame.mixer.Sound('sounds/arrow_impact.wav')
        self.fireball_impact = pygame.mixer.Sound('sounds/fireball_impact.wav')

        #Fuentes
        self.system_font = pygame.font.SysFont('fonts/meiryomeiryoboldmeiryouiboldmeiryouibolditalic', 58) #fuente que se encuentra en el sistema
        self.custom_font = pygame.font.Font('fonts/RademosRegular.ttf', 58)
        self.custom_font_2 = pygame.font.Font('fonts/RademosRegular.ttf', 52)
        self.custom_font_3 = pygame.font.Font('fonts/RademosRegular.ttf', 38)

    def update(self):
        self.check_end_round()
        self.check_collisions()
        self.reset_game()
    
    def draw(self):
        
        #Colores
        DARKRED = (179, 53, 30)
        DARKGREEN = (10, 50, 10)
        AMARILLO = (207, 111, 51)
        BLACK = (0, 0, 0)
        
        #Texto, fondo y HUD
        tittle_text = self.custom_font.render("ElfOrc Battle", True, DARKRED)
        tittle_rect = tittle_text.get_rect()
        tittle_rect.center = (WINDOW_WIDTH//2, 40)
        
        orc_lives_text = self.custom_font_3.render("Lives: " + str (self.enemy_orc.lives), True, BLACK, AMARILLO)
        orc_lives_rect = orc_lives_text.get_rect()
        orc_lives_rect.topright = (WINDOW_WIDTH - 40, 16)

        elf_lives_text = self.custom_font_3.render ("Lives: " + str (self.player_elf.lives), True, BLACK, AMARILLO)
        elf_lives_rect = elf_lives_text.get_rect()
        elf_lives_rect.topleft = (40 , 16)

        hud_line = pygame.image.load("images/lineadiv2.png")
        hud_rect = hud_line.get_rect()
        hud_rect.midtop = (450,60)

        crack_image = pygame.image.load("images/crack3.png")
        crack_rect = crack_image.get_rect()
        crack_rect.center = (450,290)

        #Blit HUD
        display_surface.blit(tittle_text, tittle_rect)
        display_surface.blit(orc_lives_text, orc_lives_rect)
        display_surface.blit(elf_lives_text, elf_lives_rect)
        display_surface.blit(hud_line, hud_rect)
        display_surface.blit(crack_image, crack_rect)
         
    def check_collisions(self):
        
        if pygame.sprite.spritecollide(self.player_elf, self.orc_attack_group, True):
            self.fireball_impact.play()
            self.player_elf.lives -= 1
        
        if pygame.sprite.spritecollide(self.enemy_orc, self.elf_attack_group, True):
            self.arc_impact.play()
            self.enemy_orc.lives -= 1   
            
    def check_end_round(self):
        #Orco pierde una vida
        pass

    def new(self):
        pass
    
    def intro_screen(self):
        pass

    def pause_game(self):
        global running

        DARKRED = (179, 53, 30)
        BLACK = (0, 0, 0)

        pause_text = self.custom_font.render("PAUSED", True, DARKRED)
        pause_rect = pause_text.get_rect()
        pause_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

        display_surface.fill(BLACK)
        display_surface.blit(pause_text, pause_rect)
        pygame.display.update()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    def reset_game(self):
        
        DARKRED = (179, 53, 30)
        BLACK = (0, 0, 0)
        
        global running
        game_over = False
        
        if player_elf.lives == 0:
            game_over = True
            while game_over is True:
                orc_win_text = self.custom_font_2.render("Orc's Win...", True, DARKRED, BLACK)
                orc_win_rect = orc_win_text.get_rect()
                orc_win_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 12)

                history_orc_text = self.custom_font_2.render("The elf resistance has fallen...", True, DARKRED, BLACK)
                history_orc_rect = history_orc_text.get_rect()
                history_orc_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//4)
                
                continue_text = self.custom_font_2.render("Press 'Enter' to play again", True, DARKRED, BLACK)
                continue_rect = continue_text.get_rect()
                continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 80)
            
                display_surface.fill(BLACK)
                display_surface.blit(orc_win_text, orc_win_rect)
                display_surface.blit(history_orc_text, history_orc_rect)
                display_surface.blit(continue_text, continue_rect)
                pygame.display.update()
                
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            game_over = False
                            running = True
                            player_elf.lives = 3
                            enemy_orc.lives = 3
                            enemy_orc.reset_position()
                            player_elf.reset_position()
                            orc_attack_group.empty()
                            elf_attack_group.empty()
                            pygame.display.update()                        
    
                    if event.type == pygame.QUIT:
                            game_over = False
                            running = False
            
        if enemy_orc.lives == 0:
            game_over = True
            while game_over is True:
                elf_win_text = self.custom_font_2.render("Elf's Win...", True, DARKRED, BLACK)
                elf_win_rect = elf_win_text.get_rect()
                elf_win_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 12)

                history_elf_text = self.custom_font_2.render("The orc tyranny has fallen...", True, DARKRED, BLACK)
                history_elf_rect = history_elf_text.get_rect()
                history_elf_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//4)

                continue_text = self.custom_font_2.render("Press 'Enter' to play again", True, DARKRED, BLACK)
                continue_rect = continue_text.get_rect()
                continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 80)

                display_surface.fill(BLACK)
                display_surface.blit(elf_win_text, elf_win_rect)
                display_surface.blit(history_elf_text, history_elf_rect)
                display_surface.blit(continue_text, continue_rect)
                pygame.display.update()
                
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            game_over = False
                            running = True
                            player_elf.lives = 3
                            enemy_orc.lives = 3
                            enemy_orc.reset_position()
                            player_elf.reset_position()
                            orc_attack_group.empty()
                            elf_attack_group.empty()
                            pygame.display.update()
                            
                    if event.type == pygame.QUIT:
                            game_over = False
                            running = False
                                
#CLASES PERSONAJES
class PlayerElf(pygame.sprite.Sprite):
    def __init__(self, attack_group):
        super().__init__()
        self.image = pygame.image.load("images/elf_image.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,175)

        self.lives = 3
        self.velocity = 4

        self.attack_group = attack_group

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_d] and self.rect.right < (WINDOW_WIDTH//2):
            self.rect.x += self.velocity
        if keys[pygame.K_w] and self.rect.top > 80:
            self.rect.y -= self.velocity
        if keys[pygame.K_s] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += self.velocity
    
    def firearrow(self):
        if len(self.attack_group) < 3:
            PlayerElfArrow(self.rect.centerx, self.rect.centery, self.attack_group)

    def reset_position(self):
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,175)

class PlayerElfArrow(pygame.sprite.Sprite):
    def __init__(self, x, y, attack_group):
        super().__init__()
        self.image = pygame.image.load("images/arrow_elf2.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (62, 48))

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        
        self.velocity = 6
        attack_group.add(self)

    def update(self):
        self.rect.x += self.velocity

        if self.rect.right > WINDOW_WIDTH:
            self.kill()

class EnemyOrc(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity, attack_group):
        super().__init__()
        self.image = pygame.image.load("images/orc_image.png")
        self.rect = self.image.get_rect()
        self.rect.topright = (x, y)

        self.starting_x = x
        self.starting_y = y

        self.lives = 3 
        self.velocity = velocity
        
        self.attack_group = attack_group

    def update(self):
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > (WINDOW_WIDTH//2):
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] and self.rect.top > 80:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += self.velocity

    def fireball(self):
                if len(self.attack_group) < 3:
                    EnemyOrcFireball(self.rect.centerx, self.rect.centery, self.attack_group)

    def reset_position(self):
        self.rect.topright = (self.starting_x, self.starting_y)

class EnemyOrcFireball(pygame.sprite.Sprite):
    def __init__(self, x, y, attack_group):
        super().__init__()
        self.image = pygame.image.load("images/fireball_orc.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        
        self.velocity = 6
        attack_group.add(self)

    def update(self):
        self.rect.x -= self.velocity

        if self.rect.left < 0:
            self.kill()

#ATAQUES grupos
elf_attack_group = pygame.sprite.Group()
orc_attack_group = pygame.sprite.Group()

#ELFO grupo y objeto
player_elf_group = pygame.sprite.Group()
player_elf = PlayerElf(elf_attack_group)
player_elf_group.add(player_elf)

#ORCO grupo y objeto
enemy_orc_group = pygame.sprite.Group()
enemy_orc = EnemyOrc(WINDOW_WIDTH, 175, 4, orc_attack_group)
enemy_orc_group.add(enemy_orc)

#OBJETO DEL JUEGO
my_game = Game(player_elf, enemy_orc, orc_attack_group, elf_attack_group)

#GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Ataque Elfo
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_elf.firearrow()
        #Ataque Orco
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP0:
                enemy_orc.fireball()
        #Pausa
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                my_game.pause_game()

    display_surface.fill((0,0,0))

    player_elf_group.update()
    player_elf_group.draw(display_surface)
    elf_attack_group.update()
    elf_attack_group.draw(display_surface)
    
    enemy_orc_group.update()
    enemy_orc_group.draw(display_surface)
    orc_attack_group.update()
    orc_attack_group.draw(display_surface)

    my_game.update()
    my_game.draw()



    #UPDATE
    pygame.display.update()
    clock.tick(FPS)

#END THE GAME
pygame.quit()