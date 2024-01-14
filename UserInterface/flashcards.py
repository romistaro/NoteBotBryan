import pygame
import sys

pygame.init()

SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Flashcards!")

BG_COLOUR = "#0a092d"
FLASHCARD_COLOUR = "#2e3856"
FLIPPED_COLOUR = "#595e6d"
FONT = pygame.font.SysFont("Arial", 30)


SCREEN.fill(BG_COLOUR)

def fcards(fdata):
    
    fdata = {
        "What is the capital of Canada?": "Ottawa",
        "Who is the GOAT?": "Messi",
        "What is the worst NHL team?": "Tie - Flames and Knights",
        "3 * 3 + 3": "12"
    }

    current_question = ""
    current_answer = ""

    card_turned = False

    index = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    card_turned = not card_turned
                elif pygame.key.get_pressed()[pygame.K_RIGHT] and index < len(fdata) - 1:
                    index += 1
                    card_turned = False
                elif pygame.key.get_pressed()[pygame.K_LEFT] and index > 0:
                    index -= 1
                    card_turned = False
        
        current_question = list(fdata)[index]
        current_answer = list(fdata.values())[index]
        current_question_object = FONT.render(current_question, True, "white")
        current_question_rect = current_question_object.get_rect(center=(400, 400))
        current_answer_object = FONT.render(current_answer, True, "white")
        current_answer_rect = current_answer_object.get_rect(center=(400, 400))
        current_index_object = FONT.render(f"{index+1}/{len(fdata)}", True, "white")
        current_index_rect = current_index_object.get_rect(center=(400, 600))
        
        if not card_turned:
            SCREEN.fill(BG_COLOUR)
            pygame.draw.rect(SCREEN, FLASHCARD_COLOUR, (150, 250, 500, 300))
            SCREEN.blit(current_question_object, current_question_rect)
        else:
            SCREEN.fill(BG_COLOUR)
            pygame.draw.rect(SCREEN, FLIPPED_COLOUR, (150, 250, 500, 300))
            SCREEN.blit(current_answer_object, current_answer_rect)
        
        SCREEN.blit(current_index_object, current_index_rect)
        
        pygame.display.update()