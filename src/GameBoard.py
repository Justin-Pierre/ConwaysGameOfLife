import random
import sys
sys.path.append(".")
from GameOfLifeConsts import * 

# Just to make linter happy
try:
    from TeamAmyRepo.src.GameOfLifeConsts import *
except:
    None

################################################################################
# Game board object class for the Game of Life.
# Holds information about the game board and processes game ticks when called.
################################################################################
class GameBoard():
    board = []          # 2D list holding the grid 
    nextBoard = []      # 2D list to hold the next grid state
    height = 0          # height of the grid
    width = 0           # width of the grid

    # Function: toggleGridEntity
    # Description:  takes in an x and y position and toggles the state of that 
    #               grid element
    def toggleGridEntity(self, x_pos, y_pos):
        if 0 > x_pos or (self.width - 1) < x_pos or 0 > y_pos or (self.width - 1) < y_pos:
            return
        else:
            self.board[x_pos][y_pos] ^= 1
  
    # Function: resizeBoard
    # Description:  takes in a height and width, then reconstructs the board by
    #               removing or adding rows and columns to match the new parameters  
    def resizeBoard(self, height, width):
        # check to ensure resize is within minimum and maximum parameters
        if MIN_SIZE > height or MIN_SIZE > width or height > MAX_SIZE or width > MAX_SIZE:
            return
        
        # no need to resize if the board doesn't exist, just create it
        if not self.board:
            self.width = width
            self.height = height
            self.board     = [[0 for y in range(self.height)] for x in range(self.width)]
            self.nextBoard = [[0 for y in range(self.height)] for x in range(self.width)]
            return

        # first, resize with respect to width

        # if target width is greater than current width
        if ( self.width <= width ):
            # repeat until current width equals target
            while ( self.width < width ):
                # first, add column to the right
                self.board.append([0 for x in range (self.height)])
                self.width += 1

                # if not at target width, next add column to the left
                if ( self.width < width ):
                    self.board.insert(0,[0 for x in range(self.height)])
                    self.width += 1                    
        # otherwise target width is less than current width
        else:
            # set bool to help alternation where possible
            # (this helps maintain the center)
            right = True
            # repeat until current width equals target
            while ( self.width > width ):
                # set counters for the left and right column totals
                leftTotal = 0
                rightTotal = 0
                # get values for those totals
                for x in self.board[0]:
                    leftTotal += x
                for x in self.board[-1]:
                    rightTotal += x
                
                # if the right has less total alive elements, OR if right and left are
                # equal and the alternator is true, delete the right column
                if ( rightTotal < leftTotal or ( rightTotal == leftTotal and right ) ):
                    right = False    # swap alternator
                    del self.board[-1]
                # otherwise delete the left column
                else:
                    right = True    # swap alternator
                    del self.board[0]

                # decrement width
                self.width -= 1 

        # second, resize with respect to height
        
        # if target height is greater than current height
        if ( self.height <= height ):
            # repeat until current height equals target
            while( self.height < height ):
                # first, add row to top 
                for x in self.board:
                    x.append(0)
                self.height += 1

                # if not at target height, next add row to bottom
                if ( self.height < height ):
                    for x in self.board:
                        x.insert(0,0)
                    self.height += 1
        # otherwise target height is less than current height
        else:
            # set bool to help alternation where possible
            # (this helps maintain the center)
            top = True
            # repeat until current height equals target
            while ( self.height > height ):
                # set counters for the bottom and top row totals
                bottomTotal = 0
                topTotal = 0
                for x in self.board:
                    # get values for those totals
                    bottomTotal += x[0]
                    topTotal += x[-1]

                # if the top has less total alive elements, OR if top and bottom are
                # equal and the alternator is true, delete the top row
                if ( topTotal < bottomTotal or ( topTotal == bottomTotal and top ) ):
                    top = False    # swap alternator
                    for x in self.board:
                        del x[-1]
                # otherwise delete the bottom row
                else:
                    top = True     # swap alternator
                    for x in self.board:
                        del x[0]

                # decrement height
                self.height -= 1        

        # clear and resize the next board to match new parameters    
        self.nextBoard = [[0 for y in range(self.height)] for x in range(self.width)]
    
    # Function: clearBoard
    # Description:  sets all grid elements to 0
    def clearBoard(self):
        self.board = [[0 for y in range(self.height)] for x in range(self.width)]

    # Function: processTick
    # Description:  the core logic of the application, processes one individual transition
    #               from one board state to the next, then swaps next and current boards
    def processTick(self):
        # iterate through every square of the grid
        for x in range(self.width):
            for y in range(self.height):
                # Add all adjacent grid values
                total = ( self.board[(x-1) % self.width][(y-1) % self.height] +
                        self.board[x][(y-1) % self.height] +
                        self.board[(x+1) % self.width][(y-1) % self.height] +
                        self.board[(x-1) % self.width][y] +
                        self.board[(x+1) % self.width][y] +
                        self.board[(x-1) % self.width][(y+1) % self.height] +
                        self.board[x][(y+1) % self.height] +
                        self.board[(x+1) % self.width][(y+1) % self.height] )

                # Check total to determine new state       
                if ( self.board[x][y] == 1 ) :
                    # if element is alive (1) ...
                    if ( total < 2 or total > 3 ) :
                        # die (0) if adjacent to less than 2 or more than 3 alive (1) elements
                        self.nextBoard[x][y] = 0
                    else :
                        # remain alive (1) otherwise
                        self.nextBoard[x][y] = 1
                else :
                    # if element is dead (0) ...
                    if ( total == 3 ) :
                        # live (1) if adjacent to exactly 3 alive (1) elements
                        self.nextBoard[x][y] = 1
                    else :
                        # remain dead (0) otherwise
                        self.nextBoard[x][y] = 0

        # if board state has not changed, return false to pause simulation
        if self.board == self.nextBoard:
            return False
        
        # Otherwise, swap the boards and return true
        tempboard = self.board
        self.board = self.nextBoard
        self.nextBoard = tempboard
        return True
    
    # Function: randomizeBoard
    # Description:  takes in an integer percent between 0 and 100;
    #               subtracts the number of currently alive grid 
    #               elements and toggles an additional number of 
    #               dead elements up to the provided percentage of
    #               the grid   
    def randomizeBoard(self, percent):
        # check to ensure randomizeBoard is within minimum and maximum parameters
        if 0 > percent or percent > 100:
            return
        # bypass to simply set all elements to alive (1) if the percent is 100 or more
        if ( percent == 100 ):            
            self.board = [[1 for x in range(self.height)] for y in range(self.width)]
            return
        
        # seed random with time
        random.seed()

        # translate the provided percent into a number of grid squares
        squares = int( self.height * self.width * ( percent / 100.0 ) )
        offSquares = []         # will hold the ordered pairs of all dead grid squares
        numOffSquares = 0       # number of squares in offSquares

        # iterate through the current board
        for x in range(self.width):
            for y in range(self.height):
                # if the element is dead (0) add it to the list and increment the size
                if self.board[x][y] == 0:
                    offSquares.append( (x,y) )
                    numOffSquares += 1
                # if the element is alive (1) decrement the number of squares
                # that need to be randomly populated
                else: 
                    squares -= 1

        # if the total alive (1) squares exceeded the number of squares needing to be randomized
        # no changes are needed
        if ( squares <= 0 ):
            # provide the user with a message and return
            print("Current board population exceeds randomization parameter; No changes made")
            return

        # repeat for the number of squares still needing to be randomized
        # after accounting for the squares already alive
        for _ in range(squares): 
            # get a random number from the range of currently dead squares stored in
            # numOffSquares list of ordered pairs
            newSquare = random.randrange(numOffSquares)
            # decrement the total
            numOffSquares -= 1
            # get a temp list containing the randomly selected ordered pair
            temp = offSquares[newSquare]

            # NOTE: this swap here isn't technically required, 
            # it's just faster to del the last element of a list
            # rather than one in the middle

            # swap the randomly selected ordered pair with the last in the list
            offSquares[newSquare] = offSquares[numOffSquares]
            # delete the last item from the list
            del offSquares[numOffSquares]
            # set the randomly selected grid square to alive
            self.board[temp[0]][temp[1]] = 1

    # Function: getCurrentBoard
    # Description:  returns the current height and width of the board,
    #               as well as the board array
    def getCurrentBoard(self):
        return self.height, self.width, self.board

    # Constructor
    def __init__(self, height, width):
        self.resizeBoard(height, width)