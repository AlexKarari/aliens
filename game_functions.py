import sys

import pygame

def check_events():
    """Respond to ley presses and mouse events."""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()