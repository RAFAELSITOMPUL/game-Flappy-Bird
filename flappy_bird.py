import pygame 
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Warna
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Kecepatan frame
clock = pygame.time.Clock()
fps = 30

# Ukuran dan posisi burung
bird_x = 50
bird_y = 300
bird_width = 40
bird_height = 40
bird_velocity = 0
gravity = 1

# Posisi pipa
pipe_width = 60
pipe_gap = 200
pipe_velocity = -5
pipe_x = screen_width
pipe_height = random.randint(100, 400)

# Skor
score = 0

# Loop game
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        # Kontrol burung
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = -10
    
    # Update posisi burung
    bird_velocity += gravity
    bird_y += bird_velocity

    # Update posisi pipa
    pipe_x += pipe_velocity

    if pipe_x < -pipe_width:
        pipe_x = screen_width
        pipe_height = random.randint(100, 400)
        score += 1

    # Deteksi tabrakan
    if (bird_y < 0 or bird_y > screen_height - bird_height or
        (pipe_x < bird_x + bird_width < pipe_x + pipe_width and
         (bird_y < pipe_height or bird_y > pipe_height + pipe_gap))):
        run = False
    
    # Gambar di layar
    screen.fill(blue)
    pygame.draw.rect(screen, white, (bird_x, bird_y, bird_width, bird_height))
    pygame.draw.rect(screen, green, (pipe_x, 0, pipe_width, pipe_height))
    pygame.draw.rect(screen, green, (pipe_x, pipe_height + pipe_gap, pipe_width, screen_height - pipe_height - pipe_gap))

    # Gambar skor
    font = pygame.font.SysFont(None, 55)
    text = font.render(f"Score: {score}", True, white)
    screen.blit(text, [10, 10])

    pygame.display.update()
    clock.tick(fps)

# Akhiri game
pygame.quit()
