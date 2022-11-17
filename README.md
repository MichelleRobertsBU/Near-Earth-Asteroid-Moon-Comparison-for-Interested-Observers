# Near-Earth-Asteroid-Moon-Comparison-for-Interested-Observers
Near-Earth-Asteroid-Moon-Comparison-for-Interested-Observers
Dataset of near Earth asteroids with distance and size in comparison to the Moon.

This is my final project for my Code Louisville Data Analysis Course 1. My goal is to 
anaylize near Earth asteroids in terms of distance and size, comparing them to the Moon
for better comprehension. 

Prerequisites
Before you continue, ensure you have met the following requirements:
* You have installed the latest version of Python
* You have a basic understanding of graph theory.

Installation
* Download the project from GitHub with this link:
 https://github.com/MichelleRobertsBU/Near-Earth-Asteroid-Moon-Comparison-for-Interested-Observers.git
* Extract the files
* Run the program in your IDE. The program was written in 
 Python 3.10.6 in Visual Studio 2022. 
* Run file NearEarthAsteroid.py
* Close out of each Plot to continue program.
* There are 3 relative links: NEO_Earth_Close_Approaches.csv, NEO_Earth_Diameter.csv, and an
image file, PIA25329_small.jpg

The project requirements have been met as listed below and in the code itself.
1. Read in data from a local csv file with Pandas read_functions.
2. Manipulate and clean data by creating 2 diameter columns to illustrate the variation in
estimated diameter of each asteroid.
3. Do 5 basic calculations with Pandas or use 5 different built-in Python functions. Number of
rows, columns, mean, standard deviation, median, and maximum and minimum values were found.
4. Visualize your data. A scatter plot, pie chart, bar graph, and several tables were created 
with matplotlib.
5. Make sure your README explains your project and markdowns were used. 

The NEO_Earth_Diameter.csv and PIA25329_small.jpg with informational data were all obtained from NASA's open data portal.

The following is my project plan for Code Louisville Data Analysis Course 1 final 
project. This project will be titled Near Earth Asteroid Moon Comparison for Interested
Observers. The dataset I plan to use came from NASA’s open data portal and is referenced
as follows: Bauer, J. M. and Lawrence, K. J., Eds. (2020). Near Earth Asteroid Tracking
V1.0. urn:nasa:pds:gbo.ast.neat.survey::1.0. NASA Planetary Data System;
https://doi.org/10.26033/xkmy-me08. My final project will show a dataset of near earth
asteroids, their characteristics such as distance and size, which will be used to 
perform calculations and comparisons with the diameter/size of the moon. My project 
will be uploaded to Github, coded using Python in Visual Studio. Instructions will be 
included for running the program as well as accessing the data. For example, NASA’s 
data portal instructs to run funpack to recover the data and the FITSIO package will 
be needed. Markdown cells will be used throughout the coded project to describe how 
the data has been scraped and utilized in the project, to explain the pandas and numpy 
functions used to clean the data, find the median distances, median sizes of the 
asteroids, as well as to explain the functions used for comparison to the size and 
diameter of the moon. I plan to use matplotlib to visualize the 10 largest asteroids 
and the 10 closest asteroids, with an explanation of what these graphs demonstrate. 
I also plan to include some recent visual links regarding NASA’s DART mission that test-
crashed a spacecraft on the asteroid Dimorphos, which altered its orbit and created a 
debris trail. I hope this project will create interest and a better understanding of the
asteroids near Earth. 

Differences from my original plan include not using funpack to recover the data and not 
using FITSIO. The dataset I used was small enough to include in an CSV file. I decided 
to do most of my numpy functions on the distances rather than the size or diameter, due
to the diameters being estimated values with a large range. 
