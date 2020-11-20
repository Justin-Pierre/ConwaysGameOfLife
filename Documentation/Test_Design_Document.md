# <p align="right"> Test Plan </p>  

<br>  

**<p align="right"> for </p>**  
  
<br>  
<br>
  
**<p align="right"> Conway's Game of Life </p>**
  
<br>  
<br>
  
**<p align="right"> Version 1.0 approved </p>**

<br>  
<br>

**<p align="right"> Team Amy </p>**

<br>  
<br>

**<p align="right"> Tuesday October 20th, 2020 </p>**  

# Table of Contents  
**1. Introduction**  
&nbsp;&nbsp;&nbsp;&nbsp; 1.1 Revisions  
&nbsp;&nbsp;&nbsp;&nbsp; 1.2 Purpose  
&nbsp;&nbsp;&nbsp;&nbsp; 1.3 Test Plan Objectives
  
**2. Test Strategy**  
&nbsp;&nbsp;&nbsp;&nbsp; 2.1 System Test  
&nbsp;&nbsp;&nbsp;&nbsp; 2.2 Stress/Performance Test  
&nbsp;&nbsp;&nbsp;&nbsp; 2.3 Automated Test  
&nbsp;&nbsp;&nbsp;&nbsp; 2.4 Documentation Test  
  
**3. Testing Environment**  
&nbsp;&nbsp;&nbsp;&nbsp; 3.1.1 Windows  
&nbsp;&nbsp;&nbsp;&nbsp; 3.1.2 Mac  
&nbsp;&nbsp;&nbsp;&nbsp; 3.1.3 Ubuntu  

**4. Functions to be Tested**  
&nbsp;&nbsp;&nbsp;&nbsp; 4.1 Grid Initialization  
&nbsp;&nbsp;&nbsp;&nbsp; 4.2 Set Alive/Dead  
&nbsp;&nbsp;&nbsp;&nbsp; 4.3 Clear  
&nbsp;&nbsp;&nbsp;&nbsp; 4.4 Load  
&nbsp;&nbsp;&nbsp;&nbsp; 4.5 Set Dimensions  
&nbsp;&nbsp;&nbsp;&nbsp; 4.6 Set Speed  
&nbsp;&nbsp;&nbsp;&nbsp; 4.7 Randomize  
&nbsp;&nbsp;&nbsp;&nbsp; 4.8 Run/Pause  
&nbsp;&nbsp;&nbsp;&nbsp; 4.9 Save  

<br>

# 1. Introduction  

## 1.1 Revisions  
<This template serves as a basis for a Software Design Specification. As in the SRS document, all italics refer to the 
“comment” style. Comments in blue are general and apply to any SDS, these that are in black are applicable specifically 
for this course. This template is based on the work by Karl. E Wiegers, Steve McConnel of CXOne group and the IEEE 
standards.>  


## 1.2 Purpose  
This document shall detail the test plan for Team Amy's implementation of Conway's Game of Life. In this document will be 
all details regarding how we intend to confirm each added function, as well as the base requirements of the game.  


## 1.3 Test Plan Objective  

The purpose of this test plan is to verify (did I make the thing right?) and validate (did I make the right thing?) Team 
Amy's version of Conway's game of life in addition to the added features. Those features being: Save/Load, set grid size, 
set speed, and randomize. The base requirements we will check being: Grid implementation, set grid element alive/dead, 
clear, and run/pause.  

<br>

# 2. Test Strategy  
<For each of the following, is explained how we plan on testing our application, each test type is provided with a brief 
description, and possibly scenario/example of how we will accomplish that sort of test.>


## 2.1 System Test  
System testing is done on the system as a whole. This is done to assure each part of the system works and does its intended purpose. This will be done by attempting to perform each of the specifications. Each function of the application will be tested with this method. 


## 2.2 Stress/Performance Test  
Stress/Performance testing checks the reliability and stability of the application being tested. This is done by applying a large amount of stress to the system in order to see if the system can handle it or if it will break. This can only be done on a smaller scale for Conway's Game of Life by testing multiple functions at once to ensure the application can handle the multiple changes. The functions that will be tested overlapping are set dimensions, and randomize. 


## 2.3 Automated Test  
Automated testing compares the actual output of the application to the expected output. This will be performed by using unit tests to ensure the functions do not only display properly but also perform correctly. These unit tests will be done on setting an element to dead/alive, resizing the grid, and randomize.


## 2.4 Documentation Test  
Documentation testing is non-functional testing. This is done by making sure you have proper documentation throughout the production of an application, as well as consistancy between the requirements in the documents. This also entails creating a test plan. For this application of Conway's Game of Life, proper documentation has been done in each phase. The requirements outlined in the SRS and then detailed in the SDD are consistent with one another, and reflected in this Test Plan. 

<br>

# 3. Testing Environment  
<Here we will define the environment(s) that we will use for testing. The SRS outlined three different environments that this application of Conway's Game of Life must be supported by.>  


## 3.1.1 Windows  
One of the environments that we will be running all of the tests on is Windows. Windows is specified in the SRS as an operating system that must be able to support Conway's Game of Life. By running all of the tests on a device with windows operating system we will be able to discover if the application has any issues running with this environment.  

## 3.1.2 Mac  
One of the environments that we will be running all of the tests on is Mac. Mac is specified in the SRS as an operating system that must be able to support Conway's Game of Life. By running all of the tests on a device with Mac operating system we will be able to discover if the application has any issues running with this environment.  

## 3.1.3 Ubuntu  
One of the environments that we will be running all of the tests on is Ubuntu. Ubuntu is specified in the SRS as an operating system that must be able to support Conway's Game of Life. By running all of the tests on a device with Ubuntu operating system we will be able to discover if the application has any issues running with this environment. 

<br>

# 4. Functions to be Tested  
<This section is critical for validation (did I make the right thing?), and maps the functions and requirements laid out 
in the SRS that need to be validated.>  


## 4.1.1 Grid Initialization  
The grid initialization will be tested using system testing, that is when the application is ran, does an empty grid of 21 x 21 elements appear on the screen to the user. 


## 4.2.1 Set Alive/Dead  
Setting an element to alive or dead will be tested using system testing. This will be done by clicking several elements of the grid at random to make sure they switch from dead to alive. Next the alive elements will then be clicked again to ensure they switch back to dead.  

## 4.2.2 Set Alive/Dead  
Setting an element to alive or dead will be tested using a unit test. This is done by setting a certain grid element value to alive and saving this grid set up in a temp grid. Then using the set alive/dead function to set the choosen element to alive, and testing to see if the two grids are the same. Thus checking that the grid accuratly sets an elements state to alive or dead.


## 4.3.1 Clear  
The clear function will be tested with system testing. First several random elements will be clicked to ensure there are alive elements within the board. Next the clear button will be clicked to ensure it does set all the grid elements back to dead. 


## 4.4.1 Load  
The load function will be tested using system testing. First the save function must be tested and a save file available. This function will have 2 tests. The first is to use the available save file, this way will input the correct save file path to ensure it opens the file and reads in properly. The second way will not enter a valid save path in order to confirm the error is caught and a pop up window with a message to the user is given. 


## 4.5.1 Set Dimensions  
Setting new dimensions for the grid will be tested using system testing. First the dimensions for both height and width will be changed, then update clicked to ensure the grid resizes to the new dimensions given. Next just height will be changed, then update clicked to make sure only the height of the grid resizes. Lastly, the width only will be changed, then update clicked to ensure only the width of the grid is resized.  

## 4.5.2 Set Dimensions  
Setting new dimensions will be stress tested by ensuring the application can hanlde more than one change at a time. This will be done by setting new dimensions, and a percentage to randomize. Then update will be clicked checking that the grid is able to resize and randomize at the same time. 

## 4.5.3 Set Dimensions  
Setting new dimensions will be tested using a unit test. This is done by having a temp grid with specified dimensions, and another with the specified new dimensions. The test will check that the current grid dimensions align with the specified dimensions in the temp grid. Next the resize function will be used to set the dimensions to the new dimensions. This next grid will be compared to the temp grid with the specified new dimensions to ensure the dimensions were updated. 


## 4.6.1 Set Speed  
The set speed function will be tested using system testing. First the simulation will be run to view the current, initialized speed. Then the application will be paused and the speed changed to a higher value, and re-run. This next run should be faster than the first one done, checking that the speed has been increased. Next the applicaation is paused again and the speed now reduced before re-running. This time the application should move at a speed that is slower than the previous viewing, ensuring that the speed did decrease. 


## 4.7.1 Randomize  
The randomize function will be tested using system testing. A number zero to one hundred will be entered in the randomize percentage, then update clicked. The grid will then re draw to have the percentage given of elements set to alive, and this will be checked visually by counting to make sure the number of alive elements is equilvalent to this value.  

## 4.7.2 Randomize  
The randomize function will be stress tested by ensuring the application can hanlde more than one change at a time. This will be done by setting a percentage to randomize, and a new height or width. Then update will be clicked checking that the grid is able to randomize and resize at the same time.  

## 4.7.3 Randomize  
The randomize function will be tested using unit tests. This will be done by using the randomize function with a specified size and percentage. The number of alive elements will already be known based on the specified dimensions and percentage. The number of alive elements produced by the randomize function will be compared to the expected value of alive elements.


## 4.8.1 Run/Pause  
The run and pause features will be tested using system testing. This will be done by clicking play and watching the application run while the application is active the pause button will be clicked. This is done to ensure the current state of each grid element freezes on what they were when pause was clicked. The play button will then be clicked again to ensure it continues after being paused. This time the application will run until the game is over to ensure it runs all the way through properly. 


## 4.9.1 Save  
The save application will be tested using system testing. First the save will be tested using a valid path to save to. Next the tester will go to the specifed location to ensure the file saved in the location. The second way to test will be done with an invalid save location to ensure an error message in a pop up window is displayed to the user. 

