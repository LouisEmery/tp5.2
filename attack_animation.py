from enum import Enum
import arcade
class AttackType(Enum):
   """
   Simple énumération pour représenter les différents types d'attaques.
   """
   NOT_STARTED = 0
   ROCK = 0,
   PAPER = 1,
   SCISSORS = 2
class AttackAnimation(arcade.Sprite):
    ATTACK_SCALE = 0.50
    ANIMATION_SPEED = 0.5


    def on_update(self, delta_time: float = 1 / 60):
       self.time_since_last_swap += delta_time
       if self.time_since_last_swap > self.ANIMATION_SPEED:
           self.time_since_last_swap = 0
       # Update the animation.
           self.current_texture += 1
           if self.current_texture < len(self.textures):
               self.set_texture(self.current_texture)
           else:
               self.current_texture = 0
               self.set_texture(self.current_texture)
    def __init__(self, attack_type, scale):
       super().__init__()
       self.current_texture = 0
       self.amimation_update_time = 1.0 / AttackAnimation.ANIMATION_SPEED
       self.time_since_last_swap = self.ANIMATION_SPEED
       self.attack_type = attack_type
       self.scale = scale
       if self.attack_type == AttackType.ROCK:
           self.textures = [
               arcade.load_texture("assets/rock1.jpg" ),
               arcade.load_texture("assets/rock2.jpg"),
           ]
       elif self.attack_type == AttackType.PAPER:
           self.textures = [
               arcade.load_texture("assets/spaper.png"),
               arcade.load_texture("assets/spaper-attack.png"),
           ]
       else:
           self.textures = [
               arcade.load_texture("assets/scissors.png"),
               arcade.load_texture("assets/scissors-close.png"),
           ]
