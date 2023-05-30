"""
Modèle de départ pour la programmation Arcade.
Il suffit de modifier les méthodes nécessaires à votre jeu.
"""
import random
import game_state
import arcade
#import arcade.gui
from enum import Enum
from attack_animation import AttackType, AttackAnimation
from game_state import GameState
NPC_score = 0
player_score = 0
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Roche, papier, ciseaux"
DEFAULT_LINE_HEIGHT = 45  # The default line height for text.

class MyGame(arcade.Window):
   """
   La classe principale de l'application

   NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
   Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
   """

   PLAYER_IMAGE_X = (SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 4)
   PLAYER_IMAGE_Y = SCREEN_HEIGHT / 2.5
   COMPUTER_IMAGE_X = (SCREEN_WIDTH / 2) * 1.5
   COMPUTER_IMAGE_Y = SCREEN_HEIGHT / 2.5
   ATTACK_FRAME_WIDTH = 154 / 2
   ATTACK_FRAME_HEIGHT = 154 / 2

   def __init__(self, width, height, title):
       super().__init__(width, height, title)

       arcade.set_background_color(arcade.color.BLACK_OLIVE)

       self.player = None
       self.computer = None
       self.players = None
       self.rock = None
       self.paper = None
       self.scisors = None
       self.player_score = 0
       self.computer_score = 0
       self.player_attack_type = {}
       self.computer_attack_type = None
       self.player_attack_chosen = False
       self.player_won_round = None
       self.draw_round = None
       self.game_state = game_state.GameState.NOT_STARTED

   def setup(self):
       """
       Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
       fois si vous recommencer une nouvelle partie.
       """
       # C'est ici que vous allez créer vos listes de sprites et vos sprites.
       # Prenez note que vous devriez attribuer une valeur à tous les attributs créés dans __init__

       self.player = arcade.Sprite('Assets/faceBeard.png', 0.5)
       self.NPC = arcade.Sprite('Assets/compy.png', 2)
       self.rock = arcade.Sprite('Assets/rock1.jpg', 0.75)
       self.paper = arcade.Sprite('Assets/spaper.png', 0.75)
       self.scisors = arcade.Sprite('Assets/scissors.png', 0.75)


       self.players = arcade.SpriteList()
       self.players.append(self.player)
       self.players.append(self.NPC)
       self.players.append(self.rock)
       self.players.append(self.paper)
       self.players.append(self.scisors)



   def validate_victory(self):
       """
       Utilisé pour déterminer qui obtient la victoire (ou s'il y a égalité)
       Rappel: après avoir validé la victoire, il faut changer l'état de jeu
       """


   def draw_possible_attack(self):
       """
       Méthode utilisée pour dessiner toutes les possibilités d'attaque du joueur
       (si aucune attaque n'a été sélectionnée, il faut dessiner les trois possibilités)
       (si une attaque a été sélectionnée, il faut dessiner cette attaque)
       """
       pass

   def draw_computer_attack(self):
       """
       Méthode utilisée pour dessiner les possibilités d'attaque de l'ordinateur
       """
       pass


   def draw_scores(self):
       """
       Montrer les scores du joueur et de l'ordinateur
       """
       pass

   def draw_instructions(self):
       """
       Dépendemment de l'état de jeu, afficher les instructions d'utilisation au joueur (appuyer sur espace, ou sur une image)
       """
       pass

   def on_draw(self):
       """
       C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
       de votre jeu à l'écran.
       """

       # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière
       # plan selon la couleur spécifié avec la méthode "set_background_color".
       arcade.start_render()

       # Display title
       arcade.draw_text(SCREEN_TITLE,0,SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 2,arcade.color.BLACK_BEAN,60,width=SCREEN_WIDTH,align="center")
       arcade.draw_text('Score: ' and NPC_score, 300, 50)
       arcade.draw_text('Score: ' and NPC_score, 700, 50)
       arcade.draw_text("ROCHE, PAPIER, CISEAU", 250, 570, arcade.color.WHITE, 20)

       self.player.center_x = 300
       self.player.center_y = 300
       self.player.draw()
       self.NPC.center_x = 700
       self.NPC.center_y = 300
       self.NPC.draw()
       self.rock.center_x = 150
       self.rock.center_y = 150
       self.rock.draw()
       self.paper.center_x = 300
       self.paper.center_y = 150
       self.paper.draw()
       self.scisors.center_x = 450
       self.scisors.center_y = 150
       self.scisors.draw()
       #afficher l'attaque de l'ordinateur selon l'état de jeu
       #afficher le résultat de la partie si l'ordinateur a joué (ROUND_DONE)
       pass

   def on_update(self, delta_time):
       """
       Toute la logique pour déplacer les objets de votre jeu et de
       simuler sa logique vont ici. Normalement, c'est ici que
       vous allez invoquer la méthode "update()" sur vos listes de sprites.
       Paramètre:
           - delta_time : le nombre de milliseconde depuis le dernier update.
       """
       #vérifier si le jeu est actif (ROUND_ACTIVE) et continuer l'animation des attaques
       #si le joueur a choisi une attaque, générer une attaque de l'ordinateur et valider la victoire
       #changer l'état de jeu si nécessaire (GAME_OVER)
       if game_state.GameState.ROUND_ACTIVE:
           if self.player_attack_chosen == True:
               pc_attack = randint(0, 2)
               if pc_attack == 0:
                   self.computer_attack_type = AttackType.ROCK
               elif pc_attack == 1:
                   self.computer_attack_type = AttackType.PAPER
               else:
                   self.computer_attack_type = AttackType.SCISSORS


   def on_key_press(self, key, key_modifiers):
       """
       Cette méthode est invoquée à chaque fois que l'usager tape une touche
       sur le clavier.
       Paramètres:
           - key: la touche enfoncée
           - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?

       Pour connaître la liste des touches possibles:
       http://arcade.academy/arcade.key.html

       if (self.game_state == game.state.GameState.NOT_STARTED)
           self.game_state = game_state.GameState.ROUND_ACTIVE
           """
       if key == arcade.key.SPACE:
            if self.game_state == GameState.NOT_STARTED:
                self.game_state = GameState.ROUND_ACTIVE
            elif self.game_state == GameState.ROUND_DONE:
                self.game_state = GameState.ROUND_ACTIVE
                self.player_win = self. player_lose = self.player_draw = False
                self.player_attack_chosen = False
                self.player_attack_type = AttackType.NOT_STARTED
            elif self.game_state == GameState.GAME_OVER:
                self.game_state = GameState.ROUND_ACTIVE
                player_score = 0
                NPC_score = 0
                self.player_win = self.player_lose = self.player_draw = False
                self.player_attack_chosen = False
                self.player_attack_type = AttackType.NOT_STARTED

   def reset_round(self):
       """
       Réinitialiser les variables qui ont été modifiées
       """
       #self.computer_attack_type = -1
       #self.player_attack_chosen = False
       #self.player_attack_type = {AttackType.ROCK: False, AttackType.PAPER: False, AttackType.SCISSORS: False}
       #self.player_won_round = False
       #self.draw_round = False

       pass

   def on_mouse_press(self, x, y, button, key_modifiers):
       """
       Méthode invoquée lorsque l'usager clique un bouton de la souris.
       Paramètres:
           - x, y: coordonnées où le bouton a été cliqué
           - button: le bouton de la souris appuyé
           - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
       """

       if self.game_state == GameState.ROUND_ACTIVE:
           if self.scissors.collides_with_point(x,y):
               self.player_attack = AttackType.SCISSORS
               self.player_attack_chosen = True
           if self.rock.collides_with_point(x, y):
               self.player_attack = AttackType.ROCK
               self.player_attack_chosen = True
           if self.rock.collides_with_point(x, y):
               self.player_attack = AttackType.ROCK
               self.player_attack_chosen = True

       pass


def main():
   """ Main method """
   game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
   game.setup()
   arcade.run()


if __name__ == "__main__":
   main()