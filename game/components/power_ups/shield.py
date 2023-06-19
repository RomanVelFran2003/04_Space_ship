from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SHIELD, SHIELD_TYPE,SPACESHIP_SHIELD

class Shield(PowerUp):
    def __init__(self):
        super().__init__(SHIELD,SHIELD_TYPE)

    def activate(self, game):
        game.player.power_up_type = SHIELD_TYPE
        game.player.set_image((65,75), SPACESHIP_SHIELD)