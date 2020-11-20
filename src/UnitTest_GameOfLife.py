import PySimpleGUI as sg
import copy
import sys
import pytest
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
# GameBoard Unit Tests
################################################################################
def test_toggleGridEntity():
    game_board = GameBoard.GameBoard(MIN_SIZE, MIN_SIZE)
    board = game_board.board
    starting_board = copy.deepcopy(board)

    game_board.toggleGridEntity(-1,-1)
    assert starting_board == board

    game_board.toggleGridEntity(MIN_SIZE,MIN_SIZE)
    assert starting_board == board

    game_board.toggleGridEntity(sys.maxsize,sys.maxsize)
    assert starting_board == board

    game_board.toggleGridEntity(-sys.maxsize,-sys.maxsize)
    assert starting_board == board

    zero_zero = board[0][0]
    game_board.toggleGridEntity(0,0)
    assert starting_board != board
    assert zero_zero ^ board[0][0]

def test_resizeBoard():
    game_board = GameBoard.GameBoard(MIN_SIZE, MIN_SIZE)
    game_board.randomizeBoard(50)
    starting_board     = copy.deepcopy(game_board.board)
    starting_nextBoard = copy.deepcopy(game_board.nextBoard)

    game_board.resizeBoard(MAX_SIZE+1,MAX_SIZE+1)
    assert starting_board == game_board.board
    assert starting_nextBoard == game_board.nextBoard

    game_board.resizeBoard(MIN_SIZE-1,MIN_SIZE-1)
    assert starting_board == game_board.board
    assert starting_nextBoard == game_board.nextBoard

    game_board.resizeBoard(MIN_SIZE,MIN_SIZE)
    assert starting_board == game_board.board
    assert starting_nextBoard == game_board.nextBoard

    game_board.resizeBoard(35, 60)
    assert starting_board != game_board.board
    assert starting_nextBoard != game_board.nextBoard
    assert 60 == len(game_board.board)
    assert 60 == len(game_board.nextBoard)
    for list in game_board.board:
        assert 35 == len(list)
    for list in game_board.nextBoard:
        assert 35 == len(list)

    game_board.resizeBoard(MAX_SIZE,MAX_SIZE)
    assert starting_board != game_board.board
    assert starting_nextBoard != game_board.nextBoard
    assert MAX_SIZE == len(game_board.board)
    assert MAX_SIZE == len(game_board.nextBoard)
    for list in game_board.board:
        assert MAX_SIZE == len(list)
    for list in game_board.nextBoard:
        assert MAX_SIZE == len(list)

def test_clearBoard():
    game_board = GameBoard.GameBoard(MIN_SIZE, MIN_SIZE)
    game_board.randomizeBoard(50)
    starting_board = copy.deepcopy(game_board.board)

    game_board.clearBoard()
    assert starting_board != game_board.board
    for list in game_board.board:
        for entry in list:
            assert 0 == entry

def test_processTick():
    game_board = GameBoard.GameBoard(MIN_SIZE, MIN_SIZE)
    game_board.toggleGridEntity(1,2)
    game_board.toggleGridEntity(2,2)
    game_board.toggleGridEntity(3,2)

    starting_board = copy.deepcopy(game_board.board)

    target_board = [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,1,1,1,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]

    game_board.processTick()
    assert starting_board == game_board.nextBoard
    assert target_board == game_board.board

def test_randomizeBoard():
    game_board = GameBoard.GameBoard(MIN_SIZE, MIN_SIZE)
    game_board.toggleGridEntity(2,1)
    game_board.toggleGridEntity(2,2)
    game_board.toggleGridEntity(2,3)

    starting_board = copy.deepcopy(game_board.board)

    game_board.randomizeBoard(0)
    assert starting_board == game_board.board

    game_board.randomizeBoard(-1)
    assert starting_board == game_board.board

    game_board.randomizeBoard(101)
    assert starting_board == game_board.board

    random_percent = 60
    game_board.randomizeBoard(random_percent)
    assert starting_board != game_board.board
    sum_alive = 0
    for list in game_board.board:
        for entry in list:
            sum_alive += entry
    assert sum_alive == (MIN_SIZE * MIN_SIZE) * (random_percent / 100.0)
    
    
def test_getCurrentBoard():
    game_board = GameBoard.GameBoard(MIN_SIZE, MAX_SIZE)
    starting_board  = copy.deepcopy(game_board.board)
    starting_height = copy.deepcopy(game_board.height)
    starting_width  = copy.deepcopy(game_board.width)

    height, width, board = game_board.getCurrentBoard()
    assert starting_board == board
    assert game_board.board == board
    assert starting_height == height
    assert game_board.height == height
    assert starting_width == width
    assert game_board.width == width

# Constructor is tested implicitly, as all it does is call resizeBoard()