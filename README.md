# The Farmer Was Replaced

Automation scripts for [**The Farmer Was Replaced**](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/), a programming game where you control drones on a grid farm. You write code in a Python-like language to plant, harvest, move, and eventually coordinate multiple drones. All code in this repository is my own work and was not written with AI.

<img width="1933" height="1057" alt="image" src="https://github.com/user-attachments/assets/ceff82a8-a2b6-49c6-a396-79ef95eafe0e" /> <br />

<br />

## Leaderboard Results

| Category                                               | Time         | Rank               |
| ------------------------------------------------------ | ------------ | ------------------ |
| [`Maze`](maze/maze_optimised.py)                       | 1m 53s       | 20<sup>th</sup>    |
| [`Fastest_Reset`](fastest_reset.py)                    | 1h 12m 24s   | 41<sup>th</sup>    |
| [`Maze_Single`](maze/maze_reusable.py)                 | 2m 43s       | 53<sup>rd</sup>    |
| [`Dinosaur`](dinosaur/dinosaur_simple.py)              | 14m 41s      | 55<sup>th</sup>    |
| [`Hay_Single`](polyculture/hay_single.py)              | 3m 04s       | 65<sup>th</sup>    |
| [`Wood_Single`](polyculture/wood_single.py)            | 8m 41s       | 70<sup>th</sup>    |
| [`Carrot_Single`](polyculture/carrot_single.py)        | 8m 13s       | 78<sup>th</sup>    |
| [`Carrots`](polyculture/carrot_polyculture.py)         | 5m 28s       | 79<sup>th</sup>    |
| [`Wood`](polyculture/tree_polyculture.py)              | 5m 53s       | 88<sup>nd</sup>    |
| [`Sunflowers_Single`](sunflowers/sunflowers_single.py) | 6m 09s       | 98<sup>th</sup>    |
| [`Sunflowers`](sunflowers/sunflower.py)                | 4m 03s       | 105<sup>th</sup>   |
| [`Cactus_Single`](cactus_single.py)                    | 0m 25s       | 105<sup>th</sup>   |
| [`Pumpkins_Single`](pumpkin/single_pumpkin.py)         | 9m 01s       | 130<sup>th</sup>   |
| [`Cactus`](cactus/cactus_odd_even_sort.py)             | 0m 43s       | 151<sup>th</sup>   |
| [`Hay`](polyculture/hay_polyculture.py)                | 3m 15s       | 161<sup>th</sup>   |
| [`Pumpkins`](pumpkin/pumpkin_optimised.py)             | 9m 00s       | 209<sup>th</sup>   |

<br />

## Algorithms by crop

### Fastest Reset

Starts from a fresh save all the way to the Leaderboard unlock. Each stage looks up the next unlock cost, runs the lightest script that can produce it (line harvest early on, then simple crop scripts, polyculture, pumpkins, mazes, and cactus), and calls `unlock()` as soon as resources are ready. Most stages reuse existing scripts for simplicity, utilising item requirement or exhaustion detection.

<img width="400" height="225" alt="FastestReset" src="https://github.com/user-attachments/assets/71335127-6d8c-4f11-a6e8-2ee14cabf071" />

<br />

### Polyculture: Hay, Carrots, and Wood

Each drone owns a cluster of 4 primary tiles. This pattern tiles the plane on maximum grid size and drone count. Companion planting is performed for each primary tile to avoid harvest wait time.

<img width="400" height="225" alt="Polyculture" src="https://github.com/user-attachments/assets/f6811abe-7e51-40ee-b26c-546902a17bf1" />

<br />

### Maze

Parallel smaller mazes with wall hugging and breadth-first search

Drones run staggered 8×8 and 4×4 mazes in parallel. Each maze and drone pair first runs a wall-hugging algorithm to build an adjacency graph. Then a BFS is run repeatedly to find the shortest path to the treasure. Adjacency graphs are updated when new shortcuts are discovered.

<img width="400" height="225" alt="Maze" src="https://github.com/user-attachments/assets/fd621219-b85e-4b27-84e3-ba6e86c76d28" />

<br />

### Pumpkins

Drones partition the farm into horizontal bands and repeatedly scan their rows, planting and watering immature tiles until the east-most and west-most tiles share the same `measure()` value. Dead pumpkins are identified and replanted on subsequent passes.

<img width="400" height="225" alt="Pumpkin" src="https://github.com/user-attachments/assets/7041ba9b-6e33-432c-ad15-befe44d60519" />

<br />

### Cactus

Parallel odd-even sort

After an initial planting pass, each half of the grid performs a column odd-even sort with 16 drones each, followed by a row odd-even sort.

<img width="400" height="225" alt="Cactus" src="https://github.com/user-attachments/assets/f338c34a-90d4-4dbb-9439-bd7a49da3ecc" />
