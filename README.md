# Dungeon_Generator

## Abstract
This is a simple dungeon generator.
It randomly places rooms within a grid and connects them using L-shaped corridors.
Floors are represented by `.`, and walls are represented by `#`.
The generator produces a fully connected dungeon map.

This was created based on this reference;
[Basic BSP Dungeon generation](https://www.roguebasin.com/index.php?title=Basic_BSP_Dungeon_generation).

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

Visualizing that.
![sample](img/grid_sample.png)

## Installation
Install via
```
git clone https://github.com/pantsman-jp/Dungeon_Generator
```

## Usage
Require `Python3`.

To run,
```
python src/main.py
```

---
Copyright © 2025 pantsman