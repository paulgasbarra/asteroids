import pygame
from constants import ASTEROID_MIN_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT


class Score(pygame.font.Font):
    def __init__(self, x, y):
        self.score = 0

    def draw(self, screen):
        font = pygame.font.Font("fonts/screaming_neon.ttf", 36)
        text = font.render(f"{self.score}", True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT - 40))
        screen.blit(text, text_rect)

    def increase(self, asteroid):
        self.score += asteroid.radius // ASTEROID_MIN_RADIUS
        
