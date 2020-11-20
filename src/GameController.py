import sys
import threading
import time
import json
sys.path.append(".")
import GameBoard
from GameOfLifeConsts import * 

# Just to make linter happy
try:
    from TeamAmyRepo.src.GameOfLifeConsts import *
except:
    None

################################################################################
# Game state controller class for the Game of Life.
# Contains reference to associated GUI and instantiates a GameBoard.
################################################################################
class GameController:
    game_gui = None
    board = None
    game_thread = None
    running = False
    speed = (DEFAULT_SPEED/SPEED_MS_CONVERSION)

    # Function: setSpeed
    # Description:  if there exists a board and it's not currently running,
    #               sets the speed parameter from input
    def setSpeed(self, speed):
        if not self.running and self.board is not None:
            self.speed = speed/SPEED_MS_CONVERSION

    # Function: setGameState
    # Description:  calls the functions to set the speed, resize the board
    #               randomize if applicable, and finally update the window
    def setGameState(self, height, width, speed, random):
        if not self.running and self.board is not None:
            self.setSpeed(speed)
            self.board.resizeBoard(height, width)
            if ( random > 0 ):
                self.board.randomizeBoard(random)
            self.game_gui.updateWindow(height,width,speed,random)

    # Function: toggleGridEntity
    # Description:  takes in an x y position and if the game is not running
    #               and calls a function from the board to toggle
    #               the element at that position, then draws the grid
    def toggleGridEntity(self, x_pos, y_pos):
        if not self.running and self.board is not None:
            self.board.toggleGridEntity(x_pos,y_pos)
            self.game_gui.drawGrid()

    # Function: gameLoop
    # Description:  the main handler function while the grid is running,
    #               loops after completing all tasks once a total time
    #               has elapsed   
    def gameLoop(self):
        while self.running and self.board is not None:
            # gets a start time for reference
            start_time = time.time()
            # Returns "False" if the game should be paused.
            self.running = self.board.processTick()
            self.game_gui.drawGrid()
            # subtracts the elapsed time and waits the remainder
            # of the time determined by the game speed
            time.sleep((start_time + self.speed) - time.time())
    
    # Function: play
    # Description:  changes the game state to running if it is not already
    def play(self):
        if self.running:
            return
        else:
            self.running = True
            self.game_thread = threading.Thread(target=self.gameLoop)
            self.game_thread.start()

    # Function: pause
    # Description:  if currently running, changes the game state to
    #               not running and joins the thread           
    def pause(self):
        if not self.running:
            return
        else:
            self.running = False
            self.game_thread.join()

    # Function: clear
    # Description:  pauses the simulation if needed, then resets the 
    #               board and redraws the grid
    def clear(self):
        self.pause()
        self.board.clearBoard()
        self.game_gui.drawGrid()

    # Function: getCurrentBoard
    # Description:  references the internal board object and returns 
    #               the core attributes: height, width, and the board  
    def getCurrentBoard(self):
        return self.board.getCurrentBoard()    

    # Function: saveToFile
    # Description:  if the simulation is paused opens a window allowing the 
    #               user to save the current board state as a JSON file
    def saveToFile(self, file_path):
        if self.running:
            return False, "Error: Can't save while running!"
        height, width, board = self.board.getCurrentBoard()
        file_data = {"height":height, "width":width, "speed":self.speed, "board":board}
        try:
            with open(file_path, 'w') as f:
                json.dump(file_data, f)
        except Exception as e:
            print(e)
            return False, "Error: Writing file failed, try another location."
        
        return True, None

    # Function: loadFromFile
    # Description:  allows the user to select a previously saved board state 
    #               and import it, replacing the current board state
    def loadFromFile(self, file_path):
        if self.running:
            return False, "Error: Can't load while running!"
        try:
            with open(file_path, 'r') as f:
                file_data = json.load(f)
        except Exception as e:
            print(e)
            return False, "Error: Opening file failed."
        
        data_list = ["height","width","speed","board"]
        if not (all(entry in data_list for entry in file_data.keys()) and all(entry in file_data.keys() for entry in data_list)):
            # Invalid save file, missing one of the key types.
            return False, "Error: fields missing from save file."
        
        try:
            new_height = int(file_data["height"])
            new_width  = int(file_data["width"])
            new_speed  = int(float(file_data["speed"]) * SPEED_MS_CONVERSION) 
        except Exception as e:
            print(e)
            return False, "Error: Converting height/width/speed to int failed"
        # We don't accept saves outside our min or max sizes
        if MIN_SIZE > new_height or new_height > MAX_SIZE:
            return False, "Error: Invalid height."
        if MIN_SIZE > new_width or new_width > MAX_SIZE:
            return False, "Error: Invalid width."
        if MIN_SPEED > new_speed or new_speed > SPEED_MS_CONVERSION:
            return False, "Error: Invalid speed."
        
        new_board = file_data["board"]
        if MIN_SIZE > len(new_board) or len(new_board) > MAX_SIZE or len(new_board) != new_width:
            return False, "Error: Board width does not match stated width."
        for column in new_board:
            if MIN_SIZE > len(column) or len(column) > MAX_SIZE or len(column) != new_height:
                return False, "Error: Board height does not match stated height."
            else:
                for entry in column:
                    if entry not in [0,1]:
                        return False, "Error: Board contains invalid characters (not 0 or 1)."

        self.board.board  = new_board
        self.board.height = new_height
        self.board.width  = new_width
        self.setGameState(new_height, new_width, new_speed, 0)
        return True, None
        

    # Constructor
    def __init__(self, height, width, speed, game_gui):
        self.board = GameBoard.GameBoard(height, width)
        self.setSpeed(speed)
        self.game_gui = game_gui     
    