# Dungeon-Generator

## Abstract
- This is a simple dungeon generator.
- It randomly places rooms within a grid and connects them with L-shaped corridors.
- Floors are represented by a period (`.`), and walls by a hash (`#`).
- The generator produces a fully connected dungeon map.
- You can customize the generated dungeon by adjusting the arguments of the `generate_dungeon` function:
    - Change the overall dungeon size with `width` and `height`.
    - Control the number of rooms with `max_room`.
    - Adjust the size of the rooms with `room_min` and `room_max`.
- This generator was created based on this reference : [Basic BSP Dungeon generation](https://www.roguebasin.com/index.php?title=Basic_BSP_Dungeon_generation).

### Example
`width=40, height=20, max_rooms=4, room_min=1, room_max=10`

Output is like this.
```
########################################
########...#############################
########...#############################
########...#############.###############
########...#############.###############
########.................###############
########...#############.........#######
########...#############.#######.#######
########...#############.#######.#######
########...#############.#######.#######
#########.######################.#######
#########.######################.#######
#########.####...###############.#######
#########.####...###############.#######
#########.####...#############....######
#########........#############....######
##############...#######################
##############...#######################
########################################
########################################
```

Visualizing output by [Grid Editor](https://paruma.github.io/grid-editor/).
![sample](img/grid_sample.png)

## Installation
Install via
```
git clone https://github.com/pantsman-jp/Dungeon-Generator
```

## Usage
Require `Python3`

To run,
```
python src/main.py
```

---
Copyright © 2025 pantsman
