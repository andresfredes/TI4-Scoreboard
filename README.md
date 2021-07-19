TI4-Scoreboard
==============

Description
-----------
A program to display a scoreboard for Twilight Imperium 4.
Suited for laptop (as control interface) connected to external display
(for scoreboard display) with both running at 1920 x 1080.

Usage
-----
### Graphical User interface:
`python scoreboard.py`
The GUI will be generated, with an option under the "Display" menu to open
the secondary scoreboard window.

### Executables:
Pyinstaller can be used for executable packaging, with the command:
`pyinstaller -wF scoreboard.py`
This will generate a local-OS specific executable, with no python or package
requirements.
Note that the `icons/` will need to be in the same folder as the generated
executable for the images to be generated correctly.

Files
-----
## config.py
Basic configuration variables and constants for various parts of the program.

## custom_widgets.py
The definition of all custom classes based on PyQT5.

## display.py
The definitions for the secondary display.

## gui.py
The main Graphical User interface code and core logic for the program as a whole.

## player.py
Definition of the Player data class.

## README.md
This file.

## scoreboard.py
The run file.

## requirements.txt
list of required python packages to run program

Requirements
------------
Python 3.8+
Packages listed in requirements.txt

License
-------
Copyright 2021, Andres Fredes, <andres.hector.fredes@gmail.com>

This file is part of TI4-Scoreboard.
 
    TI4-Scoreboard is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    TI4-Scoreboard is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with TI4-Scoreboard.  If not, see <https://www.gnu.org/licenses/>.