import pygame
import sys
from button import Button  # Assuming you already have a Button class for buttons in the menu

def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)  # Customize the font size and style

def end_screen(SCREEN):
    SCREEN.fill("white")  # Fill the screen with a white background

    title_font = get_font(60)
    title_text = title_font.render("Game Over", True, "Black")
    title_rect = title_text.get_rect(center=(640, 100))
    SCREEN.blit(title_text, title_rect)

    # Create a Play Again button
    play_again_button = Button(image=None, pos=(640, 300), text_input="Play Again", font=get_font(50), base_color="Black", hovering_color="Green")
    play_again_button.update(SCREEN)

    # Create an Exit button
    exit_button = Button(image=None, pos=(640, 500), text_input="Exit", font=get_font(50), base_color="Black", hovering_color="Green")
    exit_button.update(SCREEN)

    pygame.display.update()  # Update the screen to show the buttons

    # Event loop for button handling
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.checkForInput(pygame.mouse.get_pos()):
                    return True  # Return True to indicate play again
                if exit_button.checkForInput(pygame.mouse.get_pos()):
                    pygame.quit()  # Exit the game

