import pygame
from pygame_markdown import MarkdownRenderer  # import of the package

# minimal pygame setup
pygame.init()
screenHeight = 900
screenWidth = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pygame")
pygame.display.get_surface().fill((200, 200, 200))  # background coloring

# Creating and configuring the MarkdownRenderer.
md = MarkdownRenderer()
md.set_markdown(mdfile_path="./amongus.md")  # Set the markdown file to be rendered.
# md.set_markdown_from_string(md_string)  # Alternatively directly from a string.
surface = pygame.display.get_surface()  # get existing pygame window/screen
md.set_area(surface=surface, offset_x=50, offset_y=20, width=500, height=500)


while True:
    pygame.draw.rect(screen, (255,255,255), (0, 0, screenWidth, screenHeight))

    # get various input from pygame
    pygame_events = pygame.event.get()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    for event in pygame_events:  # handle QUIT operation
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # renders the markdown text onto the surface and handles mouse input
    md.display(pygame_events, mouse_x, mouse_y, mouse_pressed)

    pygame.display.flip()  # updates pygame window