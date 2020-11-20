import PySimpleGUI as sg
import sys
import os
import time
import queue
import copy
sys.path.append(".")
import GameBoard
import GameController
from GameOfLifeConsts import *

# Just to make linter happy
try:
    from TeamAmyRepo.src.GameOfLifeConsts import *
except:
    None

################################################################################
# Main class for the Game Of Life.
# Contains GUI and instantiates a GameController.
################################################################################
class GameOfLifeGUI():
    window = None
    controller = None
    game_area = None
    pending_draw = False
    element_size_scaled = ELEMENT_SIZE_PX

    help_text = [sg.Text(
    """Use the buttons below to interact with the game.
    Clicking on grid elements will toggle their state.
    Click \"Update\" after typing in desired height / width / speed / random% to update game board."""),]

    # build the game menu and all buttons
    def buildMenu(self, 
                height, 
                width, 
                speed, 
                rand):
        gui_menu = [sg.Button("Play",key="PLAY"),
                sg.Button("Pause",key="PAUSE"),
                sg.Button("Save",key="SAVE"),
                sg.Button("Load",key="LOAD"),
                sg.Button("Clear",key="CLEAR"),
                sg.Text("Height:"),sg.Input(default_text=height,size=(3,1),key="HEIGHT"),
                sg.Text("Width:"),sg.Input(default_text=width,size=(3,1),key="WIDTH"),                    
                sg.Text("ms/tick:"),sg.Input(default_text=speed,size=(4,1),key="SPEED"),
                sg.Text("Random %:"),sg.Input(default_text=rand,size=(3,1),key="RANDOM"),
                sg.Button("Update",key="UPDATE"),
                ]
        return gui_menu


    # Function: drawGrid
    # Description:  sets the bool "pending_draw" to true, which will trigger a 
    #               redraw of the grid next loop
    def drawGrid(self):
        self.pending_draw = True

    # Function: drawGridIfPending
    # Description:  if the grid has been flagged as needing to be redrawn,
    #               this function erases the current displayed grid and 
    #               redraws it from the current board array 
    def drawGridIfPending(self):
        if self.pending_draw:
            self.game_area.erase()
            height, width, board = self.controller.getCurrentBoard()
            for x in range(width):
                for y in range(height):
                    # dead cells (0) are set to white
                    if board[x][y] == 0:
                        color = "white"
                    # alive cells (1) are set to black
                    else:
                        color = "black"
                    self.game_area.draw_rectangle(  (x * self.element_size_scaled, y * self.element_size_scaled),
                                                    ((x+1) * self.element_size_scaled, (y+1) * self.element_size_scaled),
                                                    color, line_color=None, line_width=None)
            # reset the flag for redrawing the grid
            self.pending_draw = False

    # Function: boardClickHandler
    # Description:  this handler function takes the position of the mouse on click
    #               and if it is within the grid, calculates the coordinate within
    #               the game board and triggers that element to be toggled
    def boardClickHandler(self, mouse_pos):
        if mouse_pos == (None, None):
            # Error case, return
            return
        click_x = mouse_pos[0] // self.element_size_scaled
        click_y = mouse_pos[1] // self.element_size_scaled
        self.controller.toggleGridEntity(click_x, click_y)

    # Function: updateWindow
    # Description:  the main function hanlding the updating of the application window
    def updateWindow(self, height, width, speed, rand):
        if self.window is not None:
            self.window.close()
        # handle the scaling of the grid squares
        self.element_size_scaled = ELEMENT_SIZE_PX - int(5 * (max(height,width) / 40))
        # define the game area holding the grid
        self.game_area = sg.Graph((width*self.element_size_scaled+1, height*self.element_size_scaled+1), (0, -1), (width*self.element_size_scaled+1, height*self.element_size_scaled),
                                   key="GAMEBOARD",
                                   change_submits=True,
                                   drag_submits=False,
                                   background_color="grey")
        layout = [  copy.deepcopy(self.help_text),
                    self.buildMenu(height,width,speed,rand),
                    [self.game_area]]
        self.window = sg.Window("Conway's Game of Life - Team Amy", layout, icon=None)
        self.window.finalize()
        self.drawGrid()


    # Function: clear
    # Description:  the main controller of the application while running, handles
    #               all events that may occur
    def gameLoop(self):
        while True:
            self.drawGridIfPending()
            event, values = self.window.read(10)
            if event == sg.WIN_CLOSED:
                break
            elif event == "PLAY":
                self.controller.play()
            elif event == "PAUSE":
                self.controller.pause()
            elif event == "SAVE":
                file_name = sg.PopupGetText("Enter desired save name")
                if not file_name:
                    sg.PopupError("Error: invalid save name")
                    continue
                save_folder = sg.PopupGetFolder("Select desired save location")
                if not save_folder:
                    sg.PopupError("Error: invalid save location")
                    continue
                save_success, error_message = self.controller.saveToFile(save_folder + "/" +  file_name + ".gameOfLife")
                if not save_success:
                    sg.PopupError(error_message)
            elif event == "LOAD":
                load_file = sg.PopupGetFile("Select a file to load")
                valid_save, error_message = self.controller.loadFromFile(load_file)
                if not valid_save:
                    sg.PopupError(error_message)
            elif event == "CLEAR":
                self.controller.clear()
            elif event == "UPDATE":
                # We need to validate all the inputs:
                try:
                    height = int(values["HEIGHT"].strip())
                    width = int(values["WIDTH"].strip())
                    speed = int(values["SPEED"].strip())
                    random = int(values["RANDOM"].strip().strip('%'))
                except Exception as e:
                    print(e)
                
                # Bound our values to their ranges
                height = max(MIN_SIZE, min(height, MAX_SIZE))
                width = max(MIN_SIZE, min(width, MAX_SIZE))
                speed = max(MIN_SPEED, min(speed, MAX_SPEED))
                random = max(0, min(random, 100))

                self.controller.setGameState(height, width, speed, random)
            elif event == "GAMEBOARD":
                mouse_pos = values["GAMEBOARD"]
                self.boardClickHandler(mouse_pos)

    # constructor
    def __init__(self):
        sg.theme("DefaultNoMoreNagging")
        self.controller = GameController.GameController(DEFAULT_HEIGHT,
                                                        DEFAULT_WIDTH,
                                                        DEFAULT_SPEED,
                                                        self)
        self.updateWindow(DEFAULT_HEIGHT,DEFAULT_WIDTH,DEFAULT_SPEED,DEFAULT_RAND)
        self.gameLoop()
    
    def __del__(self):
        self.window.close()


if __name__ == "__main__":
    game = GameOfLifeGUI()
