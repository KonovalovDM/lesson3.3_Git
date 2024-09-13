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

# Скорость движения мишени можно изменить
target_speed_x = random.choice([-1, 1]) * 0.25
target_speed_y = random.choice([-1, 1]) * 0.25

# Цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Звуковые эффекты
hit_sound = pygame.mixer.Sound("sounds/hit.wav")
miss_sound = pygame.mixer.Sound("sounds/miss.wav")

# Счетчик попаданий и промахов
hits = 0
misses = 0

# Шрифт для отображения текста
font = pygame.font.Font(None, 36)

# Основной цикл игры до 50 промахов или принудительного выхода

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                # Попадание
                hits += 1
                hit_sound.play()
                # Новые координаты мишени
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                # изменение цвета при клике
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            else:
                # Промах
                misses += 1
                miss_sound.play()
                # изменение цвета при промахе
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            if misses >= 50:
                running = False

     # Обновление позиции мишени
    target_x += target_speed_x
    target_y += target_speed_y

    # Отражение мишени от стен
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x *= -1
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y *= -1

    # Обновление экрана
    screen.fill(color)
    screen.blit(target_img, (target_x, target_y))

    # Отображение счётчиков
    hits_text = font.render(f'Попадания: {hits}', True, (255, 255, 255))
    misses_text = font.render(f'Промахи: {misses}', True, (255, 255, 255))
    screen.blit(hits_text, (10, 10))
    screen.blit(misses_text, (10, 50))

    pygame.display.update()


pygame.quit()