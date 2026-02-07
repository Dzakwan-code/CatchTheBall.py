import pygame
import random

pygame.init()

# Tahapan
win_width = 600
win_height = 500
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Catch The Ball")

clock = pygame.time.Clock()
FPS = 60

#  Warna Objek
BG_TOP = (100, 180, 255)
BG_BOTTOM = (50, 150, 50)
PLAYER_COLOR = (0, 0, 0)
GOOD_BALL_COLOR = (0, 200, 0)
BAD_BALL_COLOR = (200, 0, 0)

# Level - Levelnya
level_scores = {
    1: 35,
    2: 67,
    3: 100
}

def set_level(lv):
    global level, max_score, score, lives, finish, win
    level = lv
    max_score = level_scores[lv]
    score = 0
    lives = 3
    finish = False
    win = False

# mulainya di level 1
set_level(1)

# Benda2 nya
player = pygame.Rect(250, 420, 100, 20)
good_ball = pygame.Rect(random.randint(0, 560), -40, 40, 40)
bad_ball = pygame.Rect(random.randint(0, 560), -200, 40, 40)

player_speed = 6
good_ball_speed = 5
bad_ball_speed = 9

#  Tulisan
font = pygame.font.Font(None, 26)
big_font = pygame.font.Font(None, 60)

lose_text = big_font.render("GAME OVER", True, (200, 0, 0))
win_text = big_font.render("YOU WIN!", True, (0, 150, 0))

lose_rect = lose_text.get_rect(center=(win_width//2, win_height//2))
win_rect = win_text.get_rect(center=(win_width//2, win_height//2))

# CREDIT :)
credit_text1 = font.render("BY dzakwan", True, (0, 0, 0))
credit_text2 = font.render("THANKS TO kak nadia dan teman semuanya", True, (0, 0, 0))

credit_rect1 = credit_text1.get_rect(bottomright=(win_width-10, win_height-30))
credit_rect2 = credit_text2.get_rect(bottomright=(win_width-10, win_height-10))

#  Function
def draw_background():
    window.fill(BG_TOP)
    pygame.draw.rect(window, BG_BOTTOM, (0, 350, win_width, 150))

#  pengulangan
game = True
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

        # menu level
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_1:
                set_level(1)
            if e.key == pygame.K_2:
                set_level(2)
            if e.key == pygame.K_3:
                set_level(3)

    if not finish:
        draw_background()

        # kontrol player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x > 0:
            player.x -= player_speed
        if keys[pygame.K_d] and player.x < win_width - player.width:
            player.x += player_speed

        # Gerakan bola
        good_ball.y += good_ball_speed
        bad_ball.y += bad_ball_speed

        # GOOD BALL
        if player.colliderect(good_ball):
            score += 1
            good_ball.y = -40
            good_ball.x = random.randint(0, 560)

        if good_ball.y > win_height:
            lives -= 1
            good_ball.y = -40
            good_ball.x = random.randint(0, 560)

        # BAD BALL
        if player.colliderect(bad_ball):
            lives -= 1
            bad_ball.y = -200
            bad_ball.x = random.randint(0, 560)

        if bad_ball.y > win_height:
            bad_ball.y = -200
            bad_ball.x = random.randint(0, 560)

        # cek jika kalah
        if lives <= 0:
            finish = True

        # cek jika menang
        if score >= max_score:
            finish = True
            win = True

        # gambar objek :)
        pygame.draw.rect(window, PLAYER_COLOR, player)
        pygame.draw.ellipse(window, GOOD_BALL_COLOR, good_ball)
        pygame.draw.ellipse(window, BAD_BALL_COLOR, bad_ball)

        # UI
        score_text = font.render(f"Score: {score}/{max_score}", True, (0, 0, 0))
        lives_text = font.render(f"Lives: {lives}", True, (0, 0, 0))
        level_text = font.render(f"Level: {level}", True, (0, 0, 0))
        menu_text = font.render("Press 1/2/3 to change level", True, (0, 0, 0))

        window.blit(score_text, (20, 20))
        window.blit(lives_text, (20, 50))
        window.blit(level_text, (20, 80))
        window.blit(menu_text, (240, 20))

        # credit :)
        window.blit(credit_text1, credit_rect1)
        window.blit(credit_text2, credit_rect2)

    else:
        draw_background()
        if win:
            window.blit(win_text, win_rect)
        else:
            window.blit(lose_text, lose_rect)

        # credit tetap tampil
        window.blit(credit_text1, credit_rect1)
        window.blit(credit_text2, credit_rect2)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

# THANKS TO ALL
