import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Warna
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Pengaturan bola
ball_radius = 20
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 5
ball_speed_y = 5

# Pengaturan waktu
clock = pygame.time.Clock()

# Loop utama game
while True:
    # Cek event (keluar dari game)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Ambil input keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_x -= ball_speed_x
    if keys[pygame.K_RIGHT]:
        ball_x += ball_speed_x
    if keys[pygame.K_UP]:
        ball_y -= ball_speed_y
    if keys[pygame.K_DOWN]:
        ball_y += ball_speed_y

    # Batasi gerakan bola agar tidak keluar layar
    if ball_x - ball_radius < 0:
        ball_x = ball_radius
    if ball_x + ball_radius > screen_width:
        ball_x = screen_width - ball_radius
    if ball_y - ball_radius < 0:
        ball_y = ball_radius
    if ball_y + ball_radius > screen_height:
        ball_y = screen_height - ball_radius

    # Bersihkan layar
    screen.fill(WHITE)

    # Gambar bola
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Update layar
    pygame.display.flip()

    # Atur kecepatan frame
    clock.tick(60)
