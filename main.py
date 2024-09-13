import pygame
import random

pygame.init()

# Настройки экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")

# Иконка и изображение мишени
icon = pygame.image.load("img/Tir.jpeg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

# Начальные координаты мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Скорость движения мишени
target_speed_x = random.choice([-1, 1]) * 5
target_speed_y = random.choice([-1, 1]) * 5

# Цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Звуковые эффекты
hit_sound = pygame.mixer.Sound("sounds/hit.wav")
miss_sound = pygame.mixed.Sound("sounds/hit.wav")


running = True
while running:
    pass

pygame.quit()