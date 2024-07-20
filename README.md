
# Float Fall Bouncing
![](https://github.com/raunnieo/Gravity-Simulator/blob/master/ffb_header.gif)

Float Fall Bouncing is a simple Physics Simulator that shows gravity's effect in different mediums and environments built using the Pygame library. The objective of the project is to control the balls and observe the motion of balls on the ground or a medium.

## Features

- Control multiple balls using mouse inputs.
- Balls bounce off the ground with realistic physics.
- Option to switch between different environments, such as "ground" and "water".
- Option to switch between different object, such as "football" and "basketball".
- Display velocity vectors for each ball.
- Control the density of "Water" using arrow keys.
- Drag, drop, and add balls in interactive mode.

## Prerequisites

- Python 3.10
- Pygame library

## Installation

1. Install the required dependencies:

   pip install pygame

## Usage

1. Run the script: main.py
2. Follow the on-screen instructions to interact with the project.
3. Use the spacebar to make the balls bounce.
4. Press 'ESC' to open the menu screen.
5. Press 'A' to add a new ball.
6. Press 'R' to remove the first ball.
7. Use the arrow keys to adjust the density (only available in certain environments).

## File Structure

- `main.py`: The main script to run the project.
- `menu.py`: Contains functions for the menu interface.
- `loadScreen.py`: Contains functions for loading screens and displaying the loading animation.
- `vectors.py`: Provides a function to display velocity vectors for the balls.
- `end.py`: Contains the quit screen logic.
- `window.py`: Handles the window configurations.
- `graphics/`: Directory containing various graphics assets used in the project.
## Project Summary

This project demonstrates bouncing balls in different environments. The user can control the movement of the balls,
make them jump, and add or remove balls. There are three environments: ground, water, and moon. Each environment
has its own gravity setting. The project uses the Pygame library for graphics.

## Credits
- Project by [Raunak Mandil](https://github.com/raunnieo) and [Kavyansh Dhakad](https://github.com/kvyns)

