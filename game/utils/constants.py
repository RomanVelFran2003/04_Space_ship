import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
EXPLOSION = pygame.image.load(os.path.join(IMG_DIR, 'Other/explosion.png'))
BONUS = pygame.image.load(os.path.join(IMG_DIR, 'Other/bonus.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
BG_MENU = pygame.image.load(os.path.join(IMG_DIR, 'Other/background_menu.jpg'))
BG_GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/background_game_over.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
EXPLOSION_TYPE = 'explosion'
BONUS_TYPE = 'bonus'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
SPACESHIP_EXPLOSION = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_explosion.png"))
SPACESHIP_BONUS = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_bonus.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))

#SFX Sounds

SFXSHOOT = os.path.join(IMG_DIR, "Sounds/sfxShootPlayer.wav")
SFXSHOOTENEMY = os.path.join(IMG_DIR, "Sounds/sfxShootEnemy.wav")
SFXEXPLOSIONENEMY = os.path.join(IMG_DIR, "Sounds/sfxExplosionEnemy.wav")
SFXDEATHPLAYER = os.path.join(IMG_DIR, "Sounds/sfxDeathPlayer.wav")
SFXPOWERUPEXPLOSION = os.path.join(IMG_DIR, "Sounds/sfxPowerupExplosion.wav")
SFXMOREPOINTS = os.path.join(IMG_DIR, "Sounds/sfxMorePoints.wav")

MUSICBG = os.path.join(IMG_DIR, "Sounds/musicBg.wav")


FONT_STYLE = 'freesansbold.ttf'
