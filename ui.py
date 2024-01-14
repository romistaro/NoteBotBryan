import pygame

from pygame_markdown import MarkdownRenderer

pygame.init()
pygame.display.set_caption('ElbowPartner')
icon=pygame.image.load('icon.png')
# resize icon to 50x50 pixels
small_icon = pygame.transform.scale(icon, (60, 60))
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((564, 720))
bg = pygame.image.load("bg2.png")
clock = pygame.time.Clock()
running = True
# Creating and configuring the MarkdownRenderer.
md = MarkdownRenderer()
md.set_markdown(mdfile_path="test.md")
# md.set_markdown_from_string(md_string)  # Alternatively directly from a string.
shape_surf = pygame.Surface((564 - 90, 720 - 80), pygame.SRCALPHA)

md.set_area(surface=shape_surf, offset_x=85, offset_y=73, width=564-90, height=720-80)
md.set_line_gaps(gap_line=0, gap_paragraph=19.35) #! IMPORTANT: make sure gap_line = 0, gap_paragraph = 19.35
arial = pygame.font.SysFont('Arial', 24)

startText = arial.render('Start', True, (0,0,0))
stopText = arial.render('Stop', True, (0,0,0))

recording=False

def hovering_start():
    return 100 <= mouse_x <= 100 + 384 and 17 <= mouse_y <= 17 + 50


while running:


    pygame_events = pygame.event.get()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()

    for event in pygame_events:
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if hovering_start():
                recording=not recording
                print(recording)

    screen.blit(bg, (0, 0))
    md.display(pygame_events, mouse_x, mouse_y, mouse_pressed)
    screen.blit(shape_surf, pygame.Rect(0, 0, 564, 720))

    shade = 255-100*int(hovering_start())
    pygame.draw.rect(screen, (0,shade,0) if not recording else (shade,0,0), (100, 17, 384, 50), border_radius=25)
    screen.blit(startText if not recording else stopText, (100+172, 17+10))
    if recording:

        if pygame.time.get_ticks() % 1000 < 500:
            pygame.draw.circle(screen, (255,0,0), (100+384+30, 17+25), 15)
    screen.blit(small_icon, (10, 10))
    pygame.display.flip()
    md.set_markdown(mdfile_path="test.md")
    clock.tick(60)

pygame.quit()