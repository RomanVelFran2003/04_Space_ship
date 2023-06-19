import pygame
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH, BG_MENU,BG_GAME_OVER

class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2

    def __init__(self, screen):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        screen.fill((255,255,255))
        self.font = pygame.font.Font(FONT_STYLE, 30)

    def  handle_events_on_menu(self, game):
        user_input = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            if user_input[pygame.K_TAB]:
                game.run()

    def update(self,game):

        pygame.display.update()
        self.handle_events_on_menu(game)
    
    def draw(self, screen, message, x = HALF_SCREEN_WIDTH, y = HALF_SCREEN_HEIGHT, color = (0,0,0)):
        
        text = self.font.render(message, True, color)
        text_rect = text.get_rect()
        text_rect.center = (x, y)        
        screen.blit(text, text_rect)

    
    def draw_background_menu(self, screen):
        # Dibuja el fondo de pantalla
        image = pygame.transform.scale(BG_MENU, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))

    def draw_background_gameover(self, screen):
        # Dibuja el fondo de pantalla
        image = pygame.transform.scale(BG_GAME_OVER, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))