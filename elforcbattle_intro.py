import pygame

pygame.init()
WINDOW_WIDTH=800
WINDOW_HEIGHT=400
display_surface=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Images!")

GREEN = (0,255,0)
DARKGREEN = (10,50,10)
BLACK = (0,0,0)

sound_intro = pygame.mixer.Sound('sounds/intro_sound.wav')

#Play the sound effects
sound_1.play()
sound_2.play()
sound_3.play()
sound_1.play()

#See all available system fonts
"""fonts = pygame.font.get_fonts()
for font in fonts:
    print(font)"""

#Define fonts
system_font=pygame.font.SysFont('meiryomeiryoboldmeiryouiboldmeiryouibolditalic', 58)  #para definir una fuente que se encuentra en el sistema
custom_font=pygame.font.Font('RademosRegular.ttf', 64)  #para definir una fuente que se encuentra en el sistema

#Define text
system_text=system_font.render("**OrCs Attack**", True, GREEN, DARKGREEN)
system_text_rect=system_text.get_rect()
system_text_rect.center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2)

custom_text=custom_font.render("¡Fight for Freedom!", True, GREEN)
custom_text_rect=custom_text.get_rect()
custom_text_rect.center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2+100)

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    #Blit (copy) the text surfaces to the display surface
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)

    #Update the display
    pygame.display.update()
pygame.quit()
