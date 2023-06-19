from game.components.power_ups.power_up import PowerUp
from game.utils.constants import EXPLOSION, EXPLOSION_TYPE,SPACESHIP_EXPLOSION

class Explosion(PowerUp):
    def __init__(self):
        super().__init__(EXPLOSION,EXPLOSION_TYPE)

    def activate(self, game):
        game.player.power_up_type = EXPLOSION_TYPE
        game.player.set_image((40,60), SPACESHIP_EXPLOSION)