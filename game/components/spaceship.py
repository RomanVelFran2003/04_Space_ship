import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, DEFAULT_TYPE
from game.components.bullets.bullet import Bullet

class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500

    def __init__(self):
        # Se inicializa la clase Spaceship como una subclase de Sprite de Pygame para utilizar las características de sprite
        self.image = SPACESHIP
        # Se redimensiona la imagen de la nave espacial a un tamaño específico
        self.image = pygame.transform.scale(self.image, (40, 60))

        # Se obtiene el rectángulo que enmarca la imagen y se establece su posición inicial
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.has_power_up = False
        self.power_time_up = 0
        self.power_up_type = DEFAULT_TYPE

    def move_left(self):
        # Mueve la nave hacia la izquierda si no ha alcanzado el límite izquierdo
        if self.rect.left > -60:
            self.rect.x = self.rect.x - 10
        else:
            # Si alcanza el límite izquierdo, la mueve al extremo derecho de la pantalla y luego hacia la izquierda
            self.rect.x = 1100
            self.rect.x = self.rect.x - 10

    def move_right(self):
        # Mueve la nave hacia la derecha si no ha alcanzado el límite derecho
        if self.rect.right < 1160:
            self.rect.x = self.rect.x + 10
        else:
            # Si alcanza el límite derecho, la mueve al extremo izquierdo de la pantalla y luego hacia la derecha
            self.rect.x = -60
            self.rect.x = self.rect.x + 10

    def move_up(self):
        # Mueve la nave hacia arriba si no ha alcanzado el límite superior
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y = self.rect.y - 10

    def move_down(self):
        # Mueve la nave hacia abajo si no ha alcanzado el límite inferior
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y = self.rect.y + 10

    def shoot(self, game):
            bullet = Bullet(self)
            game.bullet_manager.add_bullet(bullet)

    def update(self, user_input, game):
        # Actualiza la posición de la nave en función de la entrada del usuario
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        elif user_input[pygame.K_SPACE]:
            self.shoot(game)

    def draw(self, screen):
        # Dibuja la imagen de la nave espacial en la pantalla en su posición actual
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def set_image(self, size=(40,60), image=SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)