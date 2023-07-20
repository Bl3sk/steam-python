import time
import msvcrt
from grid import Grid

GRID_WIDTH = 5    #45
GRID_HEIGHT = 8   #40



def game_loop():
    game_grid = Grid(5, 8, 0, 0)
    x, y = game_grid.get_player_pos()
    game_grid.set_cell(x, y, 'U')
    nevim = 0

    while nevim < 100:

        oldX, oldY = game_grid.get_player_pos() # first get the old position

        # get user input
        if msvcrt.kbhit():
            char = ord(msvcrt.getch()) # this is blocking without the msvcrt.kbhit()
    
            if char == 27: # the ESC key code, exit game
                break
            elif char == 97: # a key, move left
                x -= 1
            elif char == 100: # d key, move right
                x += 1
            else:
                continue

        if not game_grid.check_Hbounds(x):
            x, y = oldX, oldY
        else:
            game_grid.set_cell(oldX, oldY, '.')

        game_grid.set_player_pos(x, y) # then set the new position
        game_grid.set_cell(x, y, 'U')
    
        # update the eggs
        game_grid.update()

        # draw the game board
        game_grid.draw()

        time.sleep(0.1) # 1/10 or 0.1
        nevim += 1


if __name__ == "__main__":
    game_loop()