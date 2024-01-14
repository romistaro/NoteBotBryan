import pygame

from pygame_markdown import MarkdownRenderer

pygame.init()
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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame_events = pygame.event.get()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print("start")
    screen.blit(bg, (0, 0))
    md.display(pygame_events, mouse_x, mouse_y, mouse_pressed)
    screen.blit(shape_surf, pygame.Rect(0, 0, 564, 720))
    pygame.display.flip()
    md.set_markdown(mdfile_path="test.md")
    clock.tick(60)

pygame.quit()