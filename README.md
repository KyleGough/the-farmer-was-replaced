# The Farmer Was Replaced

Automation scripts for [**The Farmer Was Replaced**](https://thefarmerwasreplaced.com/), a programming game where you control drones on a grid farm. You write code in a Python-like language to plant, harvest, move, and eventually coordinate multiple drones. All code in this repository is my own work and was not written with AI.

<img width="460" height="215" alt="Farmer was replaced logo" src="https://github.com/user-attachments/assets/4dfed0e9-6bcc-437e-87fd-1fce357e2b15" /><br />

<br />

## Leaderboard Results

| Category          | Target         | Script               | Time       |
| ----------------- | -------------- | -------------------- | ---------- |
| `Fastest_Reset`   | -              | `fastest_reset`      | 1h 31m 28s |
| `Maze`            | 9,863,168      | `maze_optimised`     | 2m 02s     |
| `Carrots`         | 2,000,000,000  | `carrot_polyculture` | 5m 31s     |
| `Wood`            | 10,000,000,000 | `tree_polyculture`   | 6m 09s     |
| `Sunflowers`      | 100,000        | `sunflower_setup`    | 4m 03s     |
| `Cactus`          | 33,554,432     | `cactus_setup`       | 0m 49s     |
| `Hay`             | 2,000,000,000  | `hay_polyculture`    | 5m 10s     |
| `Pumpkins`        | 200,000,000    | `pumpkin_setup`      | 10m 31s    |
| `Pumpkins_Single` | 10,000,000     | `single_pumpkin`     | 10m 03s    |

<br />

## Algorithms by crop

### Fastest Reset

**Files:** `fastest_reset.py`

A single linear script that farms from a fresh save to the Leaderboard unlock. Each block looks up the next unlock cost, runs the lightest script that can produce it (line harvest early on, then `hay` / `bush` / `carrot`, polyculture, pumpkins, mazes, and cactus), and calls `unlock()` as soon as resources are ready. Item targets use a small buffer on expansions and “exhaust” halts where spending down inventory is faster than over-farming.

<br />

### Polyculture: Hay, Carrots, and Wood

**Files:** `polyculture/polyculture.py`

Each drone owns a cluster of 4 primary tiles. This pattern tiles the plane on maximum grid size and drone count. Companion planting is performed for each primary tile to avoid harvest wait time.

<br />

### Pumpkins

**Files:** `pumpkin/pumpkin.py`, `pumpkin/multi_pumpkin.py`, `pumpkin/single_pumpkin.py`

Drones partition the farm into horizontal bands and repeatedly scan their rows, planting and watering immature tiles until every pumpkin in a row shares the same `measure()` value. Dead pumpkins are replanted on the next pass.

<br />

### Cactus

Parallel odd-even sort

**Files:** `cactus/cactus_multi.py`

After an initial planting pass, each half of the grid performs a column odd-even sort with 16 drones each, followed by a row odd-even sort.

<br />

### Maze

Parallel smaller mazes with wall hugging and breadth-first search

**Files:** `maze/maze_optimised.py`, `maze/maze_reusable.py`, `maze/maze.py`

Drones run staggered 8×8 and 4×4 mazes in parallel. Each maze and drone pair first runs a wall-hugging algorithm to build an adjacency graph. Then a BFS is run repeatedly to find the shortest path to the treasure. Adjacency graphs are updated when new shortcuts are discovered.
