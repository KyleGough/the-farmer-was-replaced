# The Farmer Was Replaced

Automation scripts for [**The Farmer Was Replaced**](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/), a programming game where you control drones on a grid farm. You write code in a Python-like language to plant, harvest, move, and eventually coordinate multiple drones. All code in this repository is my own work and was not written with AI.

<img width="1933" height="1057" alt="image" src="https://github.com/user-attachments/assets/ceff82a8-a2b6-49c6-a396-79ef95eafe0e" /> <br />


<br />

## Leaderboard Results

| Category          | Script               | Time       | Rank  |
| ----------------- | -------------------- | ---------- | ----- |
| `Fastest_Reset`   | `fastest_reset`      | 1h 18m 22s | 51th  |
| `Maze`            | `maze_optimised`     | 1m 56s     | 24th  |
| `Carrots`         | `carrot_polyculture` | 5m 28s     | 79th  |
| `Wood`            | `tree_polyculture`   | 5m 53s     | 88nd  |
| `Sunflowers`      | `sunflower`          | 4m 03s     | 105th |
| `Cactus`          | `cactus_multi`       | 0m 45s     | 185th |
| `Pumpkins_Single` | `single_pumpkin`     | 10m 03s    | 186th |
| `Pumpkins`        | `pumpkin_optimised`  | 9m 00s     | 209th |
| `Hay`             | `hay_polyculture`    | 5m 08s     | 355th |

<br />

## Algorithms by crop

### Fastest Reset

**Files:** `fastest_reset.py`

A single linear script that farms from a fresh save to the Leaderboard unlock. Each block looks up the next unlock cost, runs the lightest script that can produce it (line harvest early on, then `hay` / `bush` / `carrot`, polyculture, pumpkins, mazes, and cactus), and calls `unlock()` as soon as resources are ready. Item targets use a small buffer on expansions and “exhaust” halts where spending down inventory is faster than over-farming.

<img width="400" height="225" alt="FastestReset" src="https://github.com/user-attachments/assets/71335127-6d8c-4f11-a6e8-2ee14cabf071" />

<br />

### Polyculture: Hay, Carrots, and Wood

**Files:** `polyculture/polyculture.py`

Each drone owns a cluster of 4 primary tiles. This pattern tiles the plane on maximum grid size and drone count. Companion planting is performed for each primary tile to avoid harvest wait time.

<img width="400" height="225" alt="Polyculture" src="https://github.com/user-attachments/assets/f6811abe-7e51-40ee-b26c-546902a17bf1" />

<br />

### Maze

Parallel smaller mazes with wall hugging and breadth-first search

**Files:** `maze/maze_optimised.py`, `maze/maze_reusable.py`, `maze/maze.py`

Drones run staggered 8×8 and 4×4 mazes in parallel. Each maze and drone pair first runs a wall-hugging algorithm to build an adjacency graph. Then a BFS is run repeatedly to find the shortest path to the treasure. Adjacency graphs are updated when new shortcuts are discovered.

<img width="400" height="225" alt="Maze" src="https://github.com/user-attachments/assets/fd621219-b85e-4b27-84e3-ba6e86c76d28" />

<br />

### Pumpkins

**Files:** `pumpkin/pumpkin.py`, `pumpkin/multi_pumpkin.py`, `pumpkin/single_pumpkin.py`

Drones partition the farm into horizontal bands and repeatedly scan their rows, planting and watering immature tiles until every pumpkin in a row shares the same `measure()` value. Dead pumpkins are replanted on the next pass.

<img width="400" height="225" alt="Pumpkin" src="https://github.com/user-attachments/assets/d36c4581-2709-4e66-b162-af1bf5235698" />

<br />

### Cactus

Parallel odd-even sort

**Files:** `cactus/cactus_multi.py`

After an initial planting pass, each half of the grid performs a column odd-even sort with 16 drones each, followed by a row odd-even sort.

<img width="400" height="225" alt="Cactus" src="https://github.com/user-attachments/assets/f338c34a-90d4-4dbb-9439-bd7a49da3ecc" />

