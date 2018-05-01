import pygame
import time

pygame.mixer.init()

def play_sound(path):
    pygame.mixer.Sound(path).play()
