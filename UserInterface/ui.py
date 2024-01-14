import random

import pygame

from pygame_markdown import MarkdownRenderer

pygame.init()
pygame.display.set_caption('ElbowPartner')
icon=pygame.image.load('icon.png')
# resize icon to 50x50 pixels
small_icon = pygame.transform.smoothscale(icon, (60, 60))
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((564, 720))
bg = pygame.image.load("bg2.png")
clock = pygame.time.Clock()
running = True
# Creating and configuring the MarkdownRenderer.
md = MarkdownRenderer()
md.set_markdown(mdfile_path="test.md")
md.set_scroll_step(19.35)
magic_height = 702.36
# md.set_markdown_from_string(md_string)  # Alternatively directly from a string.
shape_surf = pygame.Surface((564 - 90, magic_height), pygame.SRCALPHA)

md.set_area(surface=shape_surf, offset_x=85, offset_y=73, width=564-90, height=magic_height)
md.set_line_gaps(gap_line=0, gap_paragraph=19.35) #! IMPORTANT: make sure gap_line = 0, gap_paragraph = 19.35
arial = pygame.font.SysFont('Arial', 24)

startText = arial.render('Start', True, (0,0,0))
stopText = arial.render('Stop', True, (0,0,0))

pencil = pygame.image.load('pencil.png')
frame_count=0
recording=False

def hovering_start():
    return 100 <= mouse_x <= 100 + 384 and 17 <= mouse_y <= 17 + 50


def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)

    return rotated_image, new_rect
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
    rotated_pencil, new_rect = rot_center(pencil, 20, 15, 60)
    if recording:
        if pygame.time.get_ticks() % 1000 < 500:
            pygame.draw.circle(screen, (255,0,0), (100+384+30, 17+25), 15)
        if frame_count%3==0:
            angle = random.randint(-5, 5)
            rotated_pencil, new_rect = rot_center(rotated_pencil, angle, 15, 60)

    screen.blit(small_icon, (7, 10))
    screen.blit(rotated_pencil, new_rect)
    pygame.display.flip()
    md.set_markdown(mdfile_path="test.md")
    frame_count+=1
    clock.tick(60)

pygame.quit()
