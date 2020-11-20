# Software Requirement Specification

## Conway's Game of Life
<br>

### Team Amy
<br>

### Authors: Jasmine Day, Tanner Harvey, Justin Pierre, Anders Pike, and Nicholas Sevilla
<br>

# Table of Contents
1. Introduction  
    1.1 Purpose  
    1.2 References  
2. Overall Description  
    2.1 Product Functions  
    2.2 User Classes and Characteristics  
    2.3 Operating Environment
3. External Interface Requirements  
    3.1 User Interfaces  
4. System Features  
    4.1 User Interface Elements  
    4.2 Simulation Specification  
    4.3 Simulation Speed Adjustment Feature  
    4.4 Grid Size Adjustment Feature  
    4.5 Randomization Feature  
    4.6 Gamestate Save and Load Feature  
5. Other Nonfunctional Requirements  
    5.1 Performance Requirements  
6. Other Requirements  
7. Appendix  
    A: Glossary

# 1. Introduction


## 1.1 Purpose
*The Game of Life program is a program used to simulate the game of life. The first goal is to allow the user to populate a grid. The second goal is to allow the user to view the simulation as it plays. The final goal is to allow the user to customize the grid to various configurations.*


## 1.2 References

*[1] [Conways' Game of Life](https://www.conwaylife.com/wiki/Conway%27s_Game_of_Life) Available on the LifeWiki. Information also available via [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).*


# 2. Overall Description


## 2.1 Product Functions

### Grid Initialization
Before the simulation is started, the system shall allow the user to set the state of any grid element to alive or dead.

### Real Time Simulation Display
The system shall dynamically display the simulation of the game of life on the current grid in real time.

### Simulation Speed
The system shall allow the user to change the speed of the simulation in between a minimum and maximum value.

### Grid Size
The system shall allow the user to define the dimensions of the grid within a certain minimum and maximum value for both x and y dimensions.

### Randomized Starting Grid
The system shall allow the user to select a percentage and randomly populate that percent of the current grid.

### Saving
While the game is paused, the system shall allow the user to save the current grid state and give it a name.

### Loading
The system shall allow the user to load any saved grid state which will replace the current grid state.


## 2.2 User Classes and Characteristics

### General User
All users of the application will fall into this type. Has full access to all features of the application.

## 2.3 Operating Environment
The Game of Life shall be functional on any platform running the latest Windows, Mac, or Ubuntu Operating System. The Game of Life is not designed for mobile devices. 


# 3. External Interface Requirements  


##  3.1 User Interfaces  
Conway’s Game of Life includes an interface that will resemble a grid with empty cells. Conway’s Game of Life’s interface is used by game players by allowing them to choose which slots are to be filled. As the player completes selecting desired slots they wish to fill, the slots filled on the grid shall be updated according to the guidelines of the game.  

- Main Interface (Figure 3.1.a)  
- Save (Figure 3.1.b)  
- Load (Figure 3.1.c)  

![Main Interface Mockup](https://i.imgur.com/0PlGxpT.png)  
**Figure 3.1.a (Main Interface)**  
This is the main interface where the game is played and the grid may be customized. 
<br>  
![Save Interface Mockup](https://i.imgur.com/AUt0AH3.png)   
**Figure 3.1.b (Save)**  
This screen shall appear when the user selects save from the main interface. The system shall allow the user to enter a name for the grid state they wish to save.  
<br>  
![Save Interface Mockup](https://i.imgur.com/pbCfA3l.png)  
**Figure 3.1.c (Load)**  
This screen shall appear when the user selects load from the main interface. The system shall allow the user to enter a name for the grid state they wish to load, or select it via the GUI.  
<br>  

# 4. System Features  


##  4.1 User Interface Elements
&nbsp;&nbsp;
    4.1.2 Description  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        When the application is initialized, the application shall present the user interface as outlined in Figure 3.1.a.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        This user interface shall contain the game grid. The user interface shall also contain UI elements for controlling the game


&nbsp;&nbsp;
    4.1.3 Functional Requirements  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.1.3.01&nbsp;&nbsp;&nbsp;&nbsp;
        The game grid shall contain no alive elements on initialization.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.1.3.02&nbsp;&nbsp;&nbsp;&nbsp;
        Every grid element shall allow the user to interact by clicking on it.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.1.3.03&nbsp;&nbsp;&nbsp;&nbsp;
        When a grid element is clicked while the game is not running, the application shall toggle its state from dead to alive or vice versa.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.1.3.03&nbsp;&nbsp;&nbsp;&nbsp;
        The application shall provide the user a UI element to reset the game grid (set every grid element to dead).  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.1.3.04&nbsp;&nbsp;&nbsp;&nbsp;
        The application shall initialize the game grid to a size of 21 by 21 grid elements.    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.1.3.05&nbsp;&nbsp;&nbsp;&nbsp;
        When the simulation is paused, the application shall provide the user a UI element to start the simulation.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        See feature 4.2 for specification of simulation gamestate.  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.1.3.06&nbsp;&nbsp;&nbsp;&nbsp;
        When the simulation is running, the application shall provide the user a UI element to pause the simulation.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        See feature 4.2 for specification of simulation gamestate.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.1.3.07&nbsp;&nbsp;&nbsp;&nbsp;
        The application shall provide the user a UI element to adjust the speed of the simulation, in milliseconds per tick.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        See feature 4.3 for specification of simulation speed adjustment feature.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.1.3.08&nbsp;&nbsp;&nbsp;&nbsp;
        The application shall provide the user a UI element to save changes to the grid size.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        See feature 4.4 for specification of grid size adjustment feature.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.1.3.09&nbsp;&nbsp;&nbsp;&nbsp;
        The application shall provide the user a UI element to select a percentage of the grid to be randomly set to the "Alive" state.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        See feature 4.5 for specification of randomization feature.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.1.3.10&nbsp;&nbsp;&nbsp;&nbsp;
        The application shall provide the user a UI element to save the current gamestate to a file.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        See feature 4.6 for specification of gamestate save and load feature.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.1.3.11&nbsp;&nbsp;&nbsp;&nbsp;
        The application shall provide the user a UI element to load a previously saved gamestate, overwriting the current gamestate.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        See feature 4.6 for specification of gamestate save and load feature.  


##  4.2 Simulation Specification
&nbsp;&nbsp;
    4.2.2 Description  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        When the user selects the start UI element, the application shall run the simulation as outlined in section 4.2.3.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        The simulation shall run until it is either paused or no grid elements are alive.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        These requirements were written based upon the rules provided online by *LifeWiki*. See section 1.2, reference 1 for more information.  

&nbsp;&nbsp;
    4.2.3 Functional Requirements  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.2.3.01&nbsp;&nbsp;&nbsp;&nbsp;
        All game grid elements shall have two states, dead and alive.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.2.3.02&nbsp;&nbsp;&nbsp;&nbsp;
        The application shall stop running the simulation once there are 0 alive grid elements.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.2.3.03&nbsp;&nbsp;&nbsp;&nbsp;
        Each game element shall have 8 neighboring elements for the purposes of applying the game rules..  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.2.3.04&nbsp;&nbsp;&nbsp;&nbsp;
        The 8 neighboring elements specified above shall be the 4 directly adjacent elements, as well as the 4 diagonally adjacent elements.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.2.3.05&nbsp;&nbsp;&nbsp;&nbsp;
        The top edge of the game grid shall be considered adjacent to the bottom edge of the game grid, and vice versa.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.2.3.06&nbsp;&nbsp;&nbsp;&nbsp;
        The left edge of the game grid shall be considered adjacent to the right edge of the game grid, and vice versa.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.2.3.07&nbsp;&nbsp;&nbsp;&nbsp;
        The application shall apply the following rules to all grid elements at the same time. This shall be called a "tick".              
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.2.3.08&nbsp;&nbsp;&nbsp;&nbsp;
        During the simulation, any live game grid element that has fewer than two live neighbors shall die on the next tick.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.2.3.09&nbsp;&nbsp;&nbsp;&nbsp;
        During the simulation, any live game grid element that has more than three live neighbors shall die on the next tick.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.2.3.10&nbsp;&nbsp;&nbsp;&nbsp;
        During the simulation, any live game grid element that has either two or three live neighbors shall live unchanged on the next tick.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.2.3.11&nbsp;&nbsp;&nbsp;&nbsp;
        During the simulation, any dead game grid element that has exactly three live neighbors shall come alive on the next tick.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.2.3.12&nbsp;&nbsp;&nbsp;&nbsp;
        The application shall ensure ticks are spaced apart by the user provided number of milliseconds per tick.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            See feature 4.3 for specification of simulation speed adjustment feature.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.2.3.13&nbsp;&nbsp;&nbsp;&nbsp;
        If the user clicks the "pause" UI element while the simulation is running, the simulation shall stop processing game ticks.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.2.3.14&nbsp;&nbsp;&nbsp;&nbsp;
        If the user clicks the "reset" UI element while the simulation is running, the simulation shall stop processing game ticks.


##  4.3 Simulation Speed Adjustment Feature
*Additional feature*  
&nbsp;&nbsp;
    4.3.2 Description  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        The rate at which game ticks occur shall be user adjustable, in order to allow the user to more easily see patterns emerge in simulations.   

&nbsp;&nbsp;
    4.3.3 Functional Requirements  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.3.3.01&nbsp;&nbsp;&nbsp;&nbsp;
        The UI element specified in REQ 4.1.3.07 shall control the simulation speed.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.3.3.02&nbsp;&nbsp;&nbsp;&nbsp;
        The simulation speed adjustment input shall be in the unit "Milliseconds per Tick".  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.3.3.03&nbsp;&nbsp;&nbsp;&nbsp;
        The simulation speed adjustment shall have a minimum of 100 milliseconds between ticks.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.3.3.04&nbsp;&nbsp;&nbsp;&nbsp;
        The simulation speed adjustment shall have a maximum of 5000 milliseconds between ticks.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.3.3.05&nbsp;&nbsp;&nbsp;&nbsp;
        The simulation speed adjustment shall be initialized to 500 milliseconds between ticks as a default.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.3.3.06&nbsp;&nbsp;&nbsp;&nbsp;
        The simulation speed adjustment shall have no effect on the game rules specified in section 4.2.3.   


##  4.4 Grid Size Adjustment Feature
*Additional feature*  
&nbsp;&nbsp;
    4.4.2 Description  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        The grid size shall be user adjustable. This allows the user to create larger grids for large simulations, or smaller grids to just simulate a small section. 

&nbsp;&nbsp;
    4.4.3 Functional Requirements  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.4.3.01&nbsp;&nbsp;&nbsp;&nbsp;
        The UI element specified in REQ 4.1.3.08 shall control the grid size.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.4.3.02&nbsp;&nbsp;&nbsp;&nbsp;
        The grid size adjustment input shall be a pair of integer numbers, representing height and width.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.4.3.03&nbsp;&nbsp;&nbsp;&nbsp;
        The grid size adjustment shall have a minimum size of 5 grid elements for both height and width.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.4.3.04&nbsp;&nbsp;&nbsp;&nbsp;
        The grid size adjustment shall have a maximum size of 100 grid elements for both height and width.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.4.3.05&nbsp;&nbsp;&nbsp;&nbsp;
        The grid size adjustment shall be initialized to the size specified in REQ 4.1.3.04 as a default.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.4.3.06&nbsp;&nbsp;&nbsp;&nbsp;
        The grid height and width shall be adjustable independently of each other.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.4.3.07&nbsp;&nbsp;&nbsp;&nbsp;
        The grid size shall not adjustable while the simulation is running.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.4.3.08&nbsp;&nbsp;&nbsp;&nbsp;
        When the grid size is adjusted to a smaller size than current, the application shall prioritize keeping alive grid elements if possible.  

##  4.5 Randomization Feature
*Additional feature*  
&nbsp;&nbsp;
    4.5.2 Description  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        The application shall provide the user a way to randomly set a given percentage of the current grid to the alive state.
         

&nbsp;&nbsp;
    4.5.3 Functional Requirements  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.5.3.01&nbsp;&nbsp;&nbsp;&nbsp;
        The UI elements specified in REQ 4.1.3.09 shall control the randomization feature.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.5.3.02&nbsp;&nbsp;&nbsp;&nbsp;
        The randomization input shall be a percentage, representing the percentage of the grid that the user wants to set to the alive state.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.5.3.03&nbsp;&nbsp;&nbsp;&nbsp;
        The randomization input shall have a minimum of 0 percent.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.5.3.04&nbsp;&nbsp;&nbsp;&nbsp;
        The randomization input shall have a maximum of 100 percent.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.5.3.05&nbsp;&nbsp;&nbsp;&nbsp;
        The randomization input shall be initialized to 0 percent as a default.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.5.3.06&nbsp;&nbsp;&nbsp;&nbsp;
        If the grid currently contains alive elements, these elements shall be counted as part of the percentage that is set to the alive state.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.5.3.07&nbsp;&nbsp;&nbsp;&nbsp;
        If the grid currently contains alive elements, the randomization feature shall not change the state of these elements.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.5.3.08&nbsp;&nbsp;&nbsp;&nbsp;
        If the randomization percentage is lower than the percent of the grid that is currently alive, the grid shall be unchanged.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.5.3.09&nbsp;&nbsp;&nbsp;&nbsp;
        The grid shall not be able to be randomized while the game is running.  

##  4.6 Gamestate Save and Load Feature
*Additional feature*  
&nbsp;&nbsp;
    4.6.2 Description  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        The application shall provide the user a way to save the current gamestate to a file, and load previously saved gamestates. 

&nbsp;&nbsp;
    4.6.3 Functional Requirements  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.6.3.01&nbsp;&nbsp;&nbsp;&nbsp;
        The UI elements specified in REQ 4.1.3.10 and REQ 4.1.3.11 shall control the gamestate save and load feature.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.6.3.02&nbsp;&nbsp;&nbsp;&nbsp;
        The save UI element shall allow the user to specify the file name and location to save the current game state to.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.6.3.03&nbsp;&nbsp;&nbsp;&nbsp;
        The load UI element shall allow the user to specify the file name and location to load a previously saved gamestate from.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.6.3.04&nbsp;&nbsp;&nbsp;&nbsp;
        The save feature shall save the following information within the save file:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            Grid height and width  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            Simulation speed  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            The current dead and alive elements within the game grid  
        
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.6.3.05&nbsp;&nbsp;&nbsp;&nbsp;
        The load feature shall load the information specified to be saved in REQ 4.6.3.04, overwriting the current gamestate with the loaded one.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.6.3.06&nbsp;&nbsp;&nbsp;&nbsp;
        The gamestate shall not be able to be saved or loaded while the simulation is running.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.6.3.07&nbsp;&nbsp;&nbsp;&nbsp;
        If the user attempts to load a file that is not a saved gamestate, the application shall provide an error message to the user.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.6.3.08&nbsp;&nbsp;&nbsp;&nbsp;
        If an error occurs during loading of a gamestate, the current gamestate shall not be changed.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        REQ 4.6.3.09&nbsp;&nbsp;&nbsp;&nbsp;
        If an error occurs during saving of a gamestate, the application shall provide an error message to the user.  


# 5. Other Nonfunctional Requirements  


##  5.1 Performance Requirements  

The application shall run smoothly with no major performance drop at any speed the user may set the simulation.


# 6. Other Requirements 

The application shall run on Windows 10.
The application shall run on the latest version of Linux.
The application shall run on the latest version of MacOS.
The application shall run as a standalone application.



# 7. Appendix  


##  A: Glossary

**GUI** | Graphical User Interface

**Grid** | The game board comprised of a rectangular array of tiles

**Element** | An individual tile of the grid that can be in one of two states; "alive" or "dead"

**Tick** | One instance in time of the grid and the state of all its elements at said time




