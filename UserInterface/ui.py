import random
import os
import threading
from pathlib import Path
import pygame
import markdown
from pygame_markdown import MarkdownRenderer
from transcription.rec import record_and_transcribe, start_mic, stop_mic

dir_path = Path(os.path.dirname(os.path.realpath(__file__)))

pygame.init()
pygame.display.set_caption("Bryan")
icon = pygame.image.load(dir_path / "icon.png")
# resize icon to 50x50 pixels
small_icon = pygame.transform.smoothscale(icon, (60, 60))
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((564, 720))
bg = pygame.image.load(dir_path / "bg2.png")
clock = pygame.time.Clock()
running = True
# Creating and configuring the MarkdownRenderer.
md = MarkdownRenderer()
md.set_markdown(mdfile_path="../transcription/output.md")

md.set_scroll_step(19.35)
magic_height = 702.36
# md.set_markdown_from_string(md_string)  # Alternatively directly from a string.
shape_surf = pygame.Surface((564 - 90, magic_height), pygame.SRCALPHA)

md.set_area(
    surface=shape_surf, offset_x=85, offset_y=73, width=564 - 90, height=magic_height
)
md.set_line_gaps(
    gap_line=0, gap_paragraph=19.35
)  #! IMPORTANT: make sure gap_line = 0, gap_paragraph = 19.35
font40 = pygame.font.SysFont("Ariel", 40)
but_text_colour = (223, 229, 232)

startText = font40.render("Start recording", True, but_text_colour)
stopText = font40.render("Pause recording", True, but_text_colour)

pencil = pygame.image.load(dir_path / "pencil.png")
frame_count = 0
recording = False


def hovering_start():
    return 100 <= mouse_x <= 100 + 384 and 17 <= mouse_y <= 17 + 50


def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)

    return rotated_image, new_rect

pencil_x = 15

open("../transcription/transcript.txt", "w").write("")
open("../transcription/output.md", "w").write("")


to_expand=[]
def click_recording():
    global recording
    recording = not recording
    to_expand.append(pygame.Rect(267, 17, 50, 50))
    if recording:
        start_mic()
    else:
        stop_mic()


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
                click_recording()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                click_recording()

    screen.blit(bg, (0, 0))
    md.display(pygame_events, mouse_x, mouse_y, mouse_pressed)
    screen.blit(shape_surf, pygame.Rect(0, 0, 564, 720))
    button_colour = (17, 40, 60)
    if hovering_start():
        button_colour = tuple(max(0,x-10) for x in button_colour)

    pygame.draw.rect(screen, button_colour, (100, 17, 384, 50), border_radius=25)
    screen.blit(startText if not recording else stopText, (100 + 112, 20 + 10))

    if not recording:
        # draw a play triangle to the left of the starttext
        pygame.draw.polygon(
            screen,
            but_text_colour,
            ((100 + 50, 17 + 10), (100 + 50, 17 + 40), (100 + 80, 17 + 25)),
        )
    else:
        # draw a pause sign to the left of the starttext
        pygame.draw.rect(screen, but_text_colour, (100 + 50, 17 + 10, 10, 30))
        pygame.draw.rect(screen, but_text_colour, (100 + 65, 17 + 10, 10, 30))
    rotated_pencil, new_rect = rot_center(pencil, 20, pencil_x, 60)
    if recording:
        if pygame.time.get_ticks() % 1000 < 500:
            pygame.draw.circle(screen, (242, 77, 61), (100 + 384 + 40, 17 + 25), 15)
        if frame_count % 5 == 0:
            angle = random.randint(-30, 30)
            rotated_pencil, new_rect = rot_center(rotated_pencil, angle, pencil_x, 60)
            pencil_x += 1
            if pencil_x > 40:
                pencil_x = 15

    for rect in to_expand:
        expand_surf = pygame.Surface(rect.size, pygame.SRCALPHA)
        pygame.draw.rect(expand_surf, (0,0,0,100), expand_surf.get_rect(), border_radius=25)
        screen.blit(expand_surf, rect)
        rect.width+=44
        rect.x-=22
        if rect.width > 384:
            to_expand.remove(rect)
    screen.blit(small_icon, (7, 10))
    screen.blit(rotated_pencil, new_rect)
    pygame.display.flip()
    temp_md = md
    md.set_markdown(mdfile_path="../transcription/output.md")
    frame_count += 1
    clock.tick(60)

pygame.quit()
