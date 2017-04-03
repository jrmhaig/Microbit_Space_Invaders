Space Invaders
===========

[![Language](https://img.shields.io/badge/language-python-blue.svg?style=flat
)](https://www.python.org)
[![Module](https://img.shields.io/badge/module-pygame-brightgreen.svg?style=flat
)](http://www.pygame.org/news.html)
[![Release](https://img.shields.io/badge/release-v1.0-orange.svg?style=flat
)](http://www.leejamesrobinson.com/space-invaders.html)

About
-----
Space Invaders is a two-dimensional fixed shooter game in which the player controls a ship with lasers by moving it horizontally
across the bottom of the screen and firing at descending aliens. The aim is to defeat five rows of ten aliens that move
horizontally back and forth across the screen as they advance towards the bottom of the screen. The player defeats an alien,
and earns points, by shooting it with the laser cannon. As more aliens are defeated, the aliens' movement and the game's music
both speed up. 

The aliens attempt to destroy the ship by firing at it while they approach the bottom of the screen. If they reach the bottom,
the alien invasion is successful and the game ends. A special "mystery ship" will occasionally move across the top of the
screen and award bonus points if destroyed. The ship is partially protected by several stationary defense bunkers that are
gradually destroyed by projectiles from the aliens and player.

The original version was created by Lee Robinson: https://github.com/leerob/Space_Invaders

<img src="http://i.imgur.com/u2mss8o.png" width="360" height="300" />
<img src="http://i.imgur.com/mR81p5O.png" width="360" height="300"/>

How To Play
----
Control the ship by tilting the micro:bit left and right to move and press either
button to fire. Use `microbit_com.py` on the micro:bit and then start the game
with:

``` bash
cd SpaceInvaders
python3 spaceinvaders.py
```

Note that this uses the device `/dev/ttyACM0`, as the micro:bit appears in Linux.
The constant `MB_DEVICE` needs to be changed in `spaceinvaders.py` to work with a
different operating system.

Contact
----
See the [original repository](https://github.com/leerob/Space_Invaders) for
contact details.

Released under the MIT License. See the LICENSE file for details.
