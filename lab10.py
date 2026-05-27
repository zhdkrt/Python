import pygame
import random
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("lab10")
clock = pygame.time.Clock()

def load_high_score():
    try:
        with open('high_score.txt', 'r') as f:
            return int(f.read())
    except:
        return 0

def save_high_score(score):
    with open('high_score.txt', 'w') as f:
        f.write(str(score))

class Boat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('boat.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 100)

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.rect.centerx = max(60, min(740, mouse_x))
        self.rect.centery = max(60, min(150, mouse_y))

class Hook(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('hook.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 600:
            self.kill()

class Fish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('fish.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 40))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 730)
        self.rect.y = random.randint(250, 500)
        self.speed_x = random.choice([-2, -1, 1, 2])
        self.points = 10

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.right > 800 or self.rect.left < 0:
            self.speed_x *= -1

class Shark(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('shark.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (120, 80))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 680)
        self.rect.y = random.randint(300, 520)
        self.speed_x = random.choice([-3, 3])

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.right > 800 or self.rect.left < 0:
            self.speed_x *= -1

class Treasure(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('treasure.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 40))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 740)
        self.rect.y = 540
        self.points = 50

def draw_grass():
    pygame.draw.rect(screen, (60, 179, 113), (0, 0, 0, 0))

def main():
    boat = Boat()
    fish_group = pygame.sprite.Group()
    shark_group = pygame.sprite.Group()
    treasure_group = pygame.sprite.Group()
    hook_group = pygame.sprite.Group()

    score = 0
    high_score = load_high_score()
    lives = 3

    fish_timer = 0
    shark_timer = 0
    treasure_timer = 0

    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)

    pygame.mixer.music.load('background_music.mp3')
    pygame.mixer.music.play(-1)
    
    running = True
    game_over = False

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    if len(hook_group) == 0:
                        hook = Hook(boat.rect.centerx, boat.rect.bottom)
                        hook_group.add(hook)
                if event.key == pygame.K_r and game_over:
                    return main()

        if not game_over:
            fish_timer += 1
            if fish_timer > 90:
                fish_group.add(Fish())
                fish_timer = 0

            shark_timer += 1
            if shark_timer > 180:
                shark_group.add(Shark())
                shark_timer = 0

            treasure_timer += 1
            if treasure_timer > 300 and len(treasure_group) < 2:
                treasure_group.add(Treasure())
                treasure_timer = 0

            boat.update()
            fish_group.update()
            shark_group.update()
            hook_group.update()

            for hook in hook_group:
                fish_hit = pygame.sprite.spritecollide(hook, fish_group, True)
                for fish in fish_hit:
                    score += fish.points
                    hook.kill()

                treasure_hit = pygame.sprite.spritecollide(hook, treasure_group, True)
                for treasure in treasure_hit:
                    score += treasure.points
                    hook.kill()

                shark_hit = pygame.sprite.spritecollide(hook, shark_group, False)
                if shark_hit:
                    lives -= 1
                    hook.kill()
                    for shark in shark_hit:
                        shark.kill()

            if lives <= 0:
                game_over = True
                if score > high_score:
                    high_score = score
                    save_high_score(high_score)

        screen.fill((135, 206, 235))
        pygame.draw.rect(screen, (34, 139, 34), (0, 0, 800, 190))
        pygame.draw.rect(screen, (0, 105, 148), (0, 190, 800, 410))
        draw_grass()

        for hook in hook_group:
            pygame.draw.line(screen, (0, 0, 0), boat.rect.midbottom, hook.rect.center, 2)

        screen.blit(boat.image, boat.rect)
        fish_group.draw(screen)
        shark_group.draw(screen)
        treasure_group.draw(screen)
        hook_group.draw(screen)

        score_text = font.render(f"Счёт: {score}", True, (255, 255, 255))
        high_score_text = small_font.render(f"Рекорд: {high_score}", True, (255, 255, 255))
        lives_text = font.render(f"Жизни: {lives}", True, (255, 255, 255))

        screen.blit(score_text, (10, 10))
        screen.blit(high_score_text, (10, 50))
        screen.blit(lives_text, (650, 10))

        if game_over:
            game_over_text = font.render("Нажми R для рестарта", True, (255, 255, 255))
            screen.blit(game_over_text, (150, 300))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

main()