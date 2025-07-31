import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Cricket Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FIELD_GREEN = (0, 128, 0)
PITCH_BROWN = (139, 69, 19)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([20, 70])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

# Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # create a surface for the ball, making the background transparent
        self.image = pygame.Surface([14, 14])
        self.image.set_colorkey((0,0,0))
        pygame.draw.circle(self.image, RED, (7, 7), 7)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vx = 0
        self.vy = 5 # Start moving down

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        # Bounce off sides
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.vx *= -1

        # Reset ball if it goes off screen (top or bottom)
        if self.rect.top > SCREEN_HEIGHT or self.rect.bottom < 0:
            self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.25)
            self.vx = 0
            self.vy = 5 # Move down again

# Main game loop
def game_loop():
    running = True

    # Sprites
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    ball_group = pygame.sprite.Group()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.75)
    all_sprites.add(player)
    player_group.add(player)

    ball = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.25)
    all_sprites.add(ball)
    ball_group.add(ball)

    # Score
    score = 0
    font = pygame.font.Font(None, 36)

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        all_sprites.update()

        # Collision detection
        collided_balls = pygame.sprite.spritecollide(player, ball_group, False)
        if collided_balls:
            ball = collided_balls[0]
            ball.vy *= -1

            # Add horizontal velocity based on where it hit the bat
            bat_center = player.rect.centerx
            ball_center = ball.rect.centerx
            hit_pos = ball_center - bat_center
            ball.vx = hit_pos * 0.1

            score += 1


        # Drawing
        # Draw the field
        screen.fill(FIELD_GREEN)

        # Draw the pitch
        pitch_width = 60
        pitch_height = 300
        pitch_x = (SCREEN_WIDTH - pitch_width) / 2
        pitch_y = (SCREEN_HEIGHT - pitch_height) / 2
        pygame.draw.rect(screen, PITCH_BROWN, (pitch_x, pitch_y, pitch_width, pitch_height))

        # Draw all sprites
        all_sprites.draw(screen)

        # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()
