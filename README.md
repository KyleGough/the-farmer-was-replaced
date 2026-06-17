# The Farmer Was Replaced

Automation scripts for [**The Farmer Was Replaced**](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/), a programming game where you control drones on a grid farm. You write code in a Python-like language to plant, harvest, move, and eventually coordinate multiple drones. All code in this repository is my own work and was not written with AI.

<img width="1933" height="1057" alt="image" src="https://github.com/user-attachments/assets/ceff82a8-a2b6-49c6-a396-79ef95eafe0e" /> <br />

<br />

## Leaderboard Results

| Demo | Algorithm |
| ---- | --------- |
| <img width="200" height="113" alt="Maze" src="https://github.com/user-attachments/assets/fd621219-b85e-4b27-84e3-ba6e86c76d28" /> | **[`Maze`](maze/maze_optimised.py)** · 1m 53s · 20<sup>th</sup><br><br>Drones run staggered 8×8 and 4×4 mazes in parallel. Each maze builds an adjacency graph via wall-hugging, then runs BFS repeatedly to find the shortest path to the treasure. |
| <img width="200" height="113" alt="FastestReset" src="https://github.com/user-attachments/assets/71335127-6d8c-4f11-a6e8-2ee14cabf071" /> | **[`Fastest_Reset`](fastest_reset.py)** · 1h 12m 24s · 41<sup>st</sup><br><br>Starts from a fresh save and unlocks the Leaderboard by running the lightest script for each stage. Each stage looks up the next unlock cost, farms until requirements are met, and calls `unlock()` as soon as resources are ready. |
| <img width="200" height="113" alt="Maze" src="https://github.com/user-attachments/assets/fd621219-b85e-4b27-84e3-ba6e86c76d28" /> | **[`Maze_Single`](maze/maze_reusable.py)** · 2m 43s · 53<sup>rd</sup><br><br>A single drone solves one 8×8 maze at a time using BFS flood-fill on a wall-hugging adjacency graph. The route is followed repeatedly, with the graph updated when shortcuts are discovered. |
| | **[`Dinosaur`](dinosaur/dinosaur_simple.py)** · 14m 41s · 55<sup>th</sup><br><br>The dinosaur-hat snake alternates between the top and bottom halves of the grid. As the tail grows, it forces exploration of additional horizontal bands to avoid trapping itself before the grid is full. |
| <img width="200" height="113" alt="Polyculture" src="https://github.com/user-attachments/assets/f6811abe-7e51-40ee-b26c-546902a17bf1" /> | **[`Hay_Single`](polyculture/hay_single.py)** · 3m 04s · 65<sup>th</sup><br><br>A single drone harvests hay on a repeating four-tile loop with pre-planted bush companions. It waters and replants between harvests on a small fixed grid. |
| <img width="200" height="113" alt="Polyculture" src="https://github.com/user-attachments/assets/f6811abe-7e51-40ee-b26c-546902a17bf1" /> | **[`Wood_Single`](polyculture/wood_single.py)** · 8m 41s · 70<sup>th</sup><br><br>Single-drone polyculture on an 8×8 grid: one tree per four-tile cluster with companion planting to avoid harvest wait time. |
| <img width="200" height="113" alt="Polyculture" src="https://github.com/user-attachments/assets/f6811abe-7e51-40ee-b26c-546902a17bf1" /> | **[`Carrot_Single`](polyculture/carrot_single.py)** · 8m 13s · 78<sup>th</sup><br><br>Single-drone polyculture on an 8×8 grid using the same four-tile cluster pattern as the multi-drone carrot run. |
| <img width="200" height="113" alt="Polyculture" src="https://github.com/user-attachments/assets/f6811abe-7e51-40ee-b26c-546902a17bf1" /> | **[`Carrots`](polyculture/carrot_polyculture.py)** · 5m 28s · 79<sup>th</sup><br><br>Each drone owns a cluster of four primary tiles tiled across the grid. Companion planting is performed for each tile to avoid harvest wait time. |
| <img width="200" height="113" alt="Polyculture" src="https://github.com/user-attachments/assets/f6811abe-7e51-40ee-b26c-546902a17bf1" /> | **[`Wood`](polyculture/tree_polyculture.py)** · 5m 53s · 88<sup>nd</sup><br><br>Same four-tile polyculture cluster pattern as carrots, with trees as the primary crop and bush companions. |
| | **[`Sunflowers_Single`](sunflowers/sunflowers_single.py)** · 6m 09s · 98<sup>th</sup><br><br>Plants every tile, records petal counts, then harvests in descending petal order to maximise power yield per cycle. |
| | **[`Sunflowers`](sunflowers/sunflowers.py)** · 4m 03s · 105<sup>th</sup><br><br>Simple row-by-row sunflower farm using the shared `simple_farm` harvest loop until the power target is reached. |
| <img width="200" height="113" alt="Cactus" src="https://github.com/user-attachments/assets/f338c34a-90d4-4dbb-9439-bd7a49da3ecc" /> | **[`Cactus_Single`](cactus/cactus_single.py)** · 0m 25s · 105<sup>th</sup><br><br>Single-drone insertion sort: rows are sorted west-to-east, then columns south-to-north, before harvesting the fully sorted grid. |
| <img width="200" height="113" alt="Pumpkin" src="https://github.com/user-attachments/assets/7041ba9b-6e33-432c-ad15-befe44d60519" /> | **[`Pumpkins_Single`](pumpkin/single_pumpkin.py)** · 9m 01s · 130<sup>th</sup><br><br>Single drone scans row by row, planting and watering until the east-most and west-most tiles on a row share the same `measure()` value, then harvests. |
| <img width="200" height="113" alt="Cactus" src="https://github.com/user-attachments/assets/f338c34a-90d4-4dbb-9439-bd7a49da3ecc" /> | **[`Cactus`](cactus/cactus_odd_even_sort.py)** · 0m 43s · 151<sup>st</sup><br><br>After an initial planting pass, each half of the grid performs a parallel column odd-even sort, followed by a row odd-even sort. |
| <img width="200" height="113" alt="Polyculture" src="https://github.com/user-attachments/assets/f6811abe-7e51-40ee-b26c-546902a17bf1" /> | **[`Hay`](polyculture/hay_polyculture.py)** · 3m 15s · 161<sup>st</sup><br><br>Drones tile the grid with a polyculture hay pattern, pre-planting bushes and replanting once if a companion is not a bush. |
| <img width="200" height="113" alt="Pumpkin" src="https://github.com/user-attachments/assets/7041ba9b-6e33-432c-ad15-befe44d60519" /> | **[`Pumpkins`](pumpkin/pumpkin_optimised.py)** · 9m 00s · 209<sup>th</sup><br><br>Drones partition the farm into horizontal bands and repeatedly scan their rows, replanting dead pumpkins until all tiles in a band are ready to harvest. |

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
