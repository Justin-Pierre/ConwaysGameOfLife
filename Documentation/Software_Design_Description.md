# **<div align="right" style="font-size:300%" > Software Design Document </div>**

<br>

**<div align="right" style="font-size:200%" > for </div>**

<br>
<br>

**<div align="right" style="font-size:200%" > Conway's Game of Life </div>**

<br>
<br>

**<div align="right" style="font-size:200%" > Version 1.0 approved </div>**

<br>
<br>

**<div align="right" style="font-size:200%" > Team Amy </div>**

<br>
<br>

**<div align="right" style="font-size:200%" > 01 OCT 2020 </div>**

<div style="page-break-after: always"></div>

# Table of Contents

1. Introduction  
    1.1 Purpose  
    1.2 System Overview  
    1.3 Definitions, Acryonyms and Abbreviations  
    1.4 Supporting Materials  
2. Architecture  
    2.1 Overview  
    2.2 Component 1..N  
3. External Interface Requirements  
    3.1 View / Model Component 1..N   


<div style="page-break-after: always"></div>

# Revisions

*<This template serves as a basis for a Software Design Specification.  As in the SRS document, all italics refer to the “comment” style. Comments in blue are general and apply to any SDS, these that are in black are applicable specifically for this course. This template is based on the work by Karl. E Wiegers, Steve McConnel of CXOne group and the IEEE standards.>*


<div style="page-break-after: always"></div>

# 1. Introduction

## 1.1 Purpose

&nbsp;&nbsp;&nbsp;&nbsp; 1.1.1 &nbsp;&nbsp; This document shall detail the functionality and requirements for Team Amy's implementation of Conway's Game of Life. In this document will be all details regarding functionality and system requirements. 

## 1.2 System Overview

&nbsp;&nbsp;&nbsp;&nbsp; 1.2.1 &nbsp;&nbsp; Our application for Conway's Game of life shall be encapsulated in one GUI. This GUI shall have two main states; paused and running.

&nbsp;&nbsp;&nbsp;&nbsp; 1.2.2 &nbsp;&nbsp; In the paused state, the user of application will be able to change the parameters of the game. These are: the size of the grid, the state of each tile of the grid, and the speed of the simulation. In addition, the user can specify a percentage of the total grid to populate randomly. Lastly, the user has the option to save the current state of the grid or load a previously saved state.

&nbsp;&nbsp;&nbsp;&nbsp; 1.2.3 &nbsp;&nbsp; In the running state, the system shall simulate Conway's Game of Life using the parameters set by the user. So long as at least one element is in the alive state, the system shall calculate the next grid state according to the rules of Conway's Game of Life [1]. The grid state shall be changed and a new one calculated at an interval determined by the user's choice of simulation speed. During the running state, the only action the user may take is to pause the simulation, which transitions the application back to the paused state.

## 1.3 Definitions, Acronyms and Abbreviations

**GUI** | Graphical User Interface

**Grid** | The game board comprised of a rectangular array of tiles

**Element** | An individual tile of the grid that can be in one of two states; "alive" or "dead"

## 1.4 Supporting Materials

*[1] [Conways' Game of Life](https://www.conwaylife.com/wiki/Conway%27s_Game_of_Life) Available on the LifeWiki. Information also available via [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).*

![Main Interface Mockup](https://i.imgur.com/0PlGxpT.png)  
*(Figure 1.4.a - Main Interface)*  

<br>

# 2. Architecture  

*< The architecture provides the top level design view of a system and provides a basis for more detailed design work. This is the section where you should include your High-Level design Compo-nent Diagram.>*

## 2.1 Overview  

*< This section provides a high level overview of the structural and functional decomposition of the system. Focus on how and why the system was decomposed in a particular way rather than on de-tails of the particular components. Include information on the major responsibilities and roles that the system (or portions of it) must play.>*

![High Level Overview](https://i.imgur.com/g7rEXYL.png)
*(Figure 2.1.a - High Level Overview)* 

## 2.2 Components

### 2.2.1 Game GUI: 

The GUI shall display the current Game of life in real time. The GUI also provides an interface for the user to interact with the program. The GUI provides controls for play/pause, clear, grid size adjustments, speed adjustment, randomization, and grid size adjustment.

### 2.2.2 Game Logic Controller:

The Game Logic Controller allows for the user input to manipulate the application. The GUI forwards to the Game Logic Controller the users input and reacts to it accordingly. With this input the Game Logic Controller is able to controll the state of the game. The game logic controller is also responsible for telling the GUI to re-draw the game grid when it has new information. This acts as the bridge between the user and the features the application offers. 
 
### 2.2.3 Grid State Storage:

The Grid State Storage will keep track of the current board. This includes the grid's dimensions, and simulation speed in addition to the current configurement of alive and dead cells within the grid. Since it keeps track of the speed of the board, this allows for the simulation speed adjustment. Since it keeps track of the dimension of the board, this allows for the boards size to be adjusted.

### 2.2.4 Save/Load Interface:

The Save/Load Interface shall provide the user with two UI elements, Save and Load (given that the game is not running). This is the option of saving the current game or loading a previously saved game. 

Should the user choose Save the application shall allow the user to choose a location to save the current game state, and allow for the user to name this save. The save file will contain the grid dimensions, simulation speed, and current state of the board (that is the current configurement of alive and dead cells within the grid). If an error were to occur during saving the application shall provide the user with an error message. 

Should the user choose Load the application shall allow for the user to choose a previously saved game to load. The load feature will overwrite the current board with the information in the save file. If the user attempts to load a file that is not a saved game state they shall be provided with an error message. If an error were to occur during loading of a saved file,
the application shall provide the user with an error message. 

<br>

# 3. High-Level Design

*< This section describes in further detail elements discussed in the Architecture. Normally this sec-tion would be split into separate documents for different areas of the design. 
High-level designs are most effective if they attempt to model groups of system elements from a number of different views.>*

## 3.1 Game Flow  

The below sequence diagram outlines the flow of the game, showing all possible user actions and how they affect the system.  

![Sequence Diagram](https://i.imgur.com/HBRBN8Q.png)
*(Figure 3.1.a - Sequence Diagram)* 

<br>

### 3.1.1 Interface

The application shall begin with the GUI displaying an empty grid. The user shall have the option to interact with the GUI, setting any element to alive or dead. The user shall have the option to clear the grid, that is to set it back to empty. The user shall have the option to click load, and load a previously saved game. The user shall have the option to input new dimensions for the grid's size. The user shall have the option to input a new speed for the simulation to have game clicks occur at. The user also has the option to input a percentage and have that percentage of the board populate randomly. The user shall have the option to run the application, the application shall run until pause is choosen by the user or there are no elements alive in the grid. The user shall have the option to save the current state of the grid, at a specified location.

### 3.1.2 Setting Alive/Dead & Clear

The user shall have the ability to set any grid element they choose to alive or dead state, in addition they have the ability to clear the grid so all elements are empty. When the user clicks a grid square the GUI has the grid state toggle the state of the element clicked, this way the element can switch easily between alive and dead. Once the grid state has toggled the elements state, drawGrid() is called in the GUI displaying the new state of the element to the user. When the user clicks clear the GUI has the grid state clear the state of each element until the entire grid has been cleared. Once the grid state has cleared all elements, drawGrid() is called in the GUI displaying the now empty grid. These features are unavailable to the user when the application is running.

### 3.1.3 Loading

The user shall have the ability to load a previously saved game from a specified location. When the user clicks load the save/load interface shall prompt the user to input the location of the desired saved game. The save/load interface shall then check if the location given is a valid address or not. If the location is not valid then the save/load interface shall display an error message stating that the location given was not valid, through the GUI to the user. If the address is valid then the game's saved data shall be imported. The save/load interface shall import the saved game speed to the game logic controller to set the speed for the game. The save/load interface shall also import the dimensions of the saved game to the grid state. Then the save/load interface shall import the current state status of each grid element and set the grid state to that configuration. Once the grid state has obtained the new speed, the new dimensions, and the new configuration of element states, drawGrid() is called in the GUI displaying the grid from the saved game to the user. The loading feature is unavailable to the user while the application is running. 

### 3.1.4 Dimensions

The user shall have the ability to change the dimensions of the grid. The input for grid dimensions shall be two integers, height and width. Both the height and width have a minimum value requirement of 5, and a maximum value requirement of 100. The user shall be able to change the height and width independentally of one another. When the user inputs values for the height and/or width deminsions the GUI sends the input values to the game logic controller. The game logic controller checks the values inputted to make sure they fit within the minimum and maximum values allowed. If the new dimensions given are not within the set range, then the game logic controller sends an error message to be displayed through the GUI to the user. If the new dimensions given are within the range of 5 to 100, then the dimensions are sent from the game logic controller to the grid state, where the grid state compares the new values given to the current grid dimensions. If the new grid dimensions are less than the current dimensions then the application will prioritize keeping alive grid elements if possible. Once done checking if prioritization needs to be done, the dimensions in the grid state are set to the values given for height and width respectively. Once the grid state has obtained the new dimensions, and determined if it needs to do prioritization, drawGrid() is called in the GUI displaying the grid with its new dimensions to the user. The dimensions adjustment feature is unavailable to the user when the application is running. 

### 3.1.5 Speed

The user shall have the ability to change the simulation speed. The speed controls the rate at which the game clicks occur. Adjusting the simulation speed shall be a single integer input, speed. The speed has a minimum value requirement of 100 miliseconds between ticks, and a maximum value requirement of 5000 miliseconds between ticks. The speed shall have a default setting of 500 miliseconds between ticks. When the user inputs a value for the speed the GUI sends the speed value to the game logic controller. The game logic controller checks to make sure the input value is within the specified range. If the input value is outside of the range given then an error message is sent from the game logic controller to the GUI to display to the user. If the input value given is within the range specified then the new speed is sent to the grid state where speed is set to the input value. Once the grid state has obtained the new speed the next time the user clicks run the game clicks will occur at the new speed. The speed adjustment feature is unavailable to the user while the application is running. 

### 3.1.6 Randomization

The user shall have the ability to choose a percentage of the grid to randomly populate with alive elements. The randomization feature takes an input percentage from the user and will populate that percentage of the board with alive elements at randomized grid locations. The randomize percent shall have a minimum value requirement of 0, and a maximum value requirement of 100. The randomized percent shall have a default value of 0. When the user inputs a value for the randomize percent the GUI sends the percent value to the game logic controller. The game logic controller checks to make sure the user input value is within the specifed range of 0 to 100. If the user input value is not within the range then the game logic controller sends an error message to the GUI to be displayed to the user. If the user input value is within the range then the game logic controller retreives from the grid state the dimensions of the grid, and the current number of alive elements. With the grid's dimensions, and the input percent the game logic controller is able to calculate the number of elements to set alive. The game logic controller compares this number with the current number of alive elements within the grid. If the current number of alive elements is greater than the determined number to set alive then the grid state is not updated and a message is sent from the game logic controller to the GUI to be displayed to the user informing them the grid already has the percentage given of alive elements. If the current number of alive elements is less than the determined amount to set alive then the game logic controller subtracts from the determined amount the currently existing amount, to find the amount of elements that still need to be toggled to alive in order to have the total number of elements be the determined amount. Once this amount of elements to set to alive is found the game logic controller has the grid state randomly toggle the determined number of elements as alive. Once the grid state has toggled the determined number of elements as alive, drawGrid() is called in the GUI displaying the randomized grid to the user. The randomization feature is unavailable to the user when the application is running. 

### 3.1.7 Run/Pause

The user shall have the ability to run or pause the application. When the user clicks play the GUI will disable the users ability to clear the grid, load a saved game, set new dimensions for the grid, set a new speed for the application, radomization, and saving. Upon play being clicked the GUI starts game logic. The game logic controller checks to see if there is at least one alive element within the grid. If there is at least one element still alive then the game logic controller waits until the next tick then preforms the check over. Between the ticks the game logic controller sends to the grid state confirmation that the grid is not empty, the grid state then updates based upon the rules of the game. Once the grid state has updated, drawGrid() is called within the GUI displaying to the user the grid state between each tick. This loop continues until the game logic controller finds that there are no more alive elements within the grid or the user clicks pause. If there are no more alive elements the game logic controller exits the loop and has the GUI re enable the users ability to use the features. If the user clicks pause then GUI has the game logic controller exit the loop and then the game logic controller has the GUI re enable the users ability to use the features. 

### 3.1.8 Saving

The user shall have the ability to save the current game to a specified location. When the user clicks save the save/load interface shall prompt the user to input the desired location to save at. The save/load interface shall then check if the location given is a valid address or not. If the location is not valid then the save/load interface shall display an error message stating that the location given was not valid, through the GUI to the user. If the address is valid then the game's  data shall be exported and saved to the given location and a message will be sent from the save/load interface to be displayed by the GUI to the user informing them their save was successful. The saving feature is unavailable to the user while the application is running. 
