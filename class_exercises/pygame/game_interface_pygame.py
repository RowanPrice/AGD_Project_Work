import pygame
from class_exercises.pygame.game_controller import Game

from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_UP,
    K_DOWN,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SQUARE_SIZE = 50

BACKGROUND_COLORS = {'wall': 'gray30',
                     'start': 'gold',
                     'exit': 'dodgerblue',
                     'floor': 'white'
                     }
PLAYER_COLOR = 'green'

class GameGUI:
    key_moves = {K_UP: 'n',
                 K_DOWN: 's',
                 K_RIGHT: 'e',
                 K_LEFT: 'w',
                 }

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Pygame MVC')

        # Set clock so that FPS can be limited
        self.clock = pygame.time.Clock()

        self.game = Game()
        self.game.set_up()
        self.player = self.game.characters[0]
        self.move_direction: str | None = None

        self.screen = pygame.display.set_mode([self.game.dimensions[1] * SQUARE_SIZE,
                                               self.game.dimensions[0] * SQUARE_SIZE])
        self.running = True

    @staticmethod
    def _convert_position(pos, center: bool = False) -> tuple[int, int]:
        """ Convert a grid position in the game to an (x, y) coordinate
                if centre is false the position returned is top-left and if center is true
                the position returned is the centre """
        pos_y, pos_x = pos[1]*SQUARE_SIZE, pos[0]*SQUARE_SIZE
        if not center:
            return pos_x, pos_y
        return pos_x + 0.5*SQUARE_SIZE, pos_y + 0.5*SQUARE_SIZE

    def main_loop(self):
        while self.running:
            self._handle_input()
            self._process_game_logic()
            self._draw()
            self.clock.tick(60) # cap to 60 FPS
        pygame.quit()

    def _handle_input(self):
        """ Checks key presses and adjusts GameGUI attributes depending on the presses """

        for event in pygame.event.get():
            # Quit conditions
            if (event.type == QUIT or
                    event.type == KEYDOWN and event.key == K_ESCAPE):
                self.running = False

            # Checks for movement keys amd sets self.move_direction according to the key pressed.
            # Otherwise, set self.move_direction to None
            ...

    def _process_game_logic(self):
        """ Implements character moves and checks if player has reached the exit """
        ...

    def _draw(self):
        """draw background first then characters"""
        self._draw_background()
        self._draw_characters()
        pygame.display.flip()

    def _draw_background(self):
        """Loop through all the game backgrounds and draw a rectangle of the appropriate colour"""
        self.screen.fill(BACKGROUND_COLORS['floor'])
        for bg in self.game.backgrounds:
            if bg.pos == (0,7):
                colour = 'gold'
            else:
                colour = BACKGROUND_COLORS[bg.name]
            grid_x, grid_y = self._convert_position(bg.pos)
            pygame.draw.rect(self.screen,colour,(grid_x,grid_y,SQUARE_SIZE,SQUARE_SIZE))

    def _draw_characters(self):
        """Loop through the characters and draw a circle for each character"""
        for char in self.game.characters:
            grid_x, grid_y = self._convert_position(char.pos,True)
            color = PLAYER_COLOR
            pygame.draw.circle(self.screen,color,(grid_x,grid_y),25)

if __name__ == "__main__":
    game = GameGUI()
    game.main_loop()