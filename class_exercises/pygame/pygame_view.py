from class_exercises.pygame.game_controller import Game


class TextInterface:
    """ Create a text-based interface for the turn-based game."""
    def __init__(self):
        self.game = Game()
        self.game.set_up()
        self.player = self.game.characters[0]
        self.game_area = []
        self.running = True

    def _create_area(self):
        width, height = self.game.dimensions
        self.game_area = []

        for y in range(height):
            row = []
            for x in range(width):
                contents = self.game.get_cell_contents((x, y))

                if contents:
                    row.append(contents[0].name[0])
                else:
                    row.append(".")
            self.game_area.append(row)

    def _draw_area(self):
        grid_str = self.game.show_game_grid()
        grid_lines = grid_str.split("\n")
        width = len(grid_lines[0])

        print("┌" + "─" * width + "┐")

        for line in grid_lines:
            print("│" + line + "│")

        print("└" + "─" * width + "┘")

    def _handle_input(self):
        move = input("Move (W/A/S/D or Q): ").lower()

        if move == "q":
            self.running = False
            return

        directions = {
            "w": "up",
            "s": "down",
            "a": "left",
            "d": "right"
        }

        if move in directions:
            result = self.game.move_character(self.player, directions[move])

            if result:
                print(result)
        else:
            print("Invalid input")


    def main_loop(self):
        """Keep drawing the area and asking for player moves while self.running is True."""
        print("Welcome to Rowan's Game")
        while self.running:
            self._draw_area()
            self._handle_input()


if __name__ == "__main__":
    tui = TextInterface()
    tui.main_loop()