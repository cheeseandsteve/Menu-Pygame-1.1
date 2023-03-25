import pygame
import button

pygame.init()

# game window
screenwidth = 800
screenheight = 600

screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("Main menu")

icon_img = pygame.image.load("icon.png").convert_alpha()
pygame.display.set_icon(icon_img)

# bg_img = pygame.image.load("background.png").convert_alpha()
# bg_img = pygame.transform.scale(bg_img, (screenwidth, screenheight))

# game variables
menu_state = "start"

# define fonts / colours
font = pygame.font.Font("Minecraft.ttf", 45)
text_col = (255, 255, 255)


def drawtext(text, font, textcol, x, y):
    img = font.render(text, True, textcol)
    screen.blit(img, (x, y))


# load images
resume_img = pygame.image.load("resume.png").convert_alpha()
options_img = pygame.image.load("options.png").convert_alpha()
quit_img = pygame.image.load("quit.png").convert_alpha()
video_img = pygame.image.load("video.png").convert_alpha()
audio_img = pygame.image.load("audio.png").convert_alpha()
bindings_img = pygame.image.load("bindings.png").convert_alpha()
back_img = pygame.image.load("back.png").convert_alpha()
start_img = pygame.image.load("start.png").convert_alpha()
pause_img = pygame.image.load("pause.png").convert_alpha()
restart_img = pygame.image.load("restart.png").convert_alpha()


# create button instances
resume_button = button.Button(295, 175, resume_img, 1.5)
options_button = button.Button(283, 300, options_img, 1.5)
quit_button = button.Button(646, 536, quit_img, 1.5)
video_button = button.Button(75, 175, video_img, 1.5)
audio_button = button.Button(75, 275, audio_img, 1.5)
bindings_button = button.Button(75, 375, bindings_img, 1.5)
back_button = button.Button(75, 475, back_img, 1.5)
back_options_button = button.Button(328, 475, back_img, 1.5)
start_button = button.Button(307, 380, start_img, 1.5)
pause_button = button.Button(15, 15, pause_img, 1.2)
restart_button = button.Button(277, 420, restart_img, 1.5)

# game loop
run = True
while run:
    screen.fill((51, 31, 91))
    # screen.blit(bg_img, (0, 0))

    # check menu state
    if menu_state == "main":
        if resume_button.draw(screen):
            menu_state = "game"
        if options_button.draw(screen):
            menu_state = "options"
        if restart_button.draw(screen):
            menu_state = "start"
        if quit_button.draw(screen):
            run = False

    if menu_state == "options":
        drawtext("Options", font, text_col, 320, 75)
        if video_button.draw(screen):
            menu_state = "video"
        if audio_button.draw(screen):
            menu_state = "audio"
        if bindings_button.draw(screen):
            menu_state = "bindings"
        if back_button.draw(screen):
            menu_state = "main"

    if menu_state == "video":
        drawtext("Video settings", font, text_col, 300, 75)
        if back_options_button.draw(screen):
            menu_state = "options"

    if menu_state == "audio":
        drawtext("Audio settings", font, text_col, 300, 75)
        if back_options_button.draw(screen):
            menu_state = "options"

    if menu_state == "bindings":
        drawtext("Key Bindings", font, text_col, 280, 75)
        if back_options_button.draw(screen):
            menu_state = "options"

    if menu_state == "start":
        if start_button.draw(screen):
            menu_state = "game"
        if options_button.draw(screen):
            menu_state = "options"

    if menu_state == "game":
        if pause_button.draw(screen):
            menu_state = "main"
        drawtext("Press ESCAPE to pause", font, text_col, 150, 250)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu_state = "main"
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
