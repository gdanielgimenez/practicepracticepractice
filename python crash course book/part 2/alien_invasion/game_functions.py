import sys
import pygame


def check_events():
    """response to key presses and mouse events """
    # watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """update images to the screen and flip to the new screen"""
    # Re draw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # make the most recently drawn screen visible
    pygame.display.flip()
