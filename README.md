# The Farmer Was Replaced

Automation scripts for [**The Farmer Was Replaced**](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/), a programming game where you control drones on a grid farm. You write code in a Python-like language to plant, harvest, move, and eventually coordinate multiple drones. All code in this repository is my own work and was not written with AI.

<img width="1933" height="1057" alt="image" src="https://github.com/user-attachments/assets/ceff82a8-a2b6-49c6-a396-79ef95eafe0e" /> <br />

<br />

## Leaderboard Times

| Category                                             | Time         | Rank  |
| ---------------------------------------------------- | ------------ | ----- |
| [Maze](maze/maze_32_drones.py)                       | `1m 53s`     | `20`  |
| [Fastest_Reset](fastest_reset.py)                    | `1h 03m 06s` | `37`  |
| [Maze_Single](maze/maze_reusable.py)                 | `2m 43s`     | `53`  |
| [Sunflowers_Single](sunflowers/sunflowers_single.py) | `5m 35s`     | `54`  |
| [Dinosaur](dinosaur/dinosaur_simple.py)              | `14m 41s`    | `55`  |
| [Hay_Single](polyculture/hay_single.py)              | `3m 04s`     | `65`  |
| [Wood_Single](polyculture/wood_single.py)            | `8m 41s`     | `70`  |
| [Carrot_Single](polyculture/carrot_single.py)        | `8m 13s`     | `78`  |
| [Carrots](polyculture/carrot_polyculture.py)         | `5m 28s`     | `79`  |
| [Wood](polyculture/tree_polyculture.py)              | `5m 53s`     | `88`  |
| [Sunflowers](sunflowers/sunflower.py)                | `4m 03s`     | `105` |
| [Cactus_Single](cactus_single.py)                    | `0m 25s`     | `105` |
| [Pumpkins_Single](pumpkin/single_pumpkin.py)         | `9m 01s`     | `130` |
| [Cactus](cactus/cactus_odd_even_sort.py)             | `0m 43s`     | `151` |
| [Hay](polyculture/hay_polyculture.py)                | `3m 15s`     | `161` |
| [Pumpkins](pumpkin/pumpkin_optimised.py)             | `9m 00s`     | `209` |

<br />

## Algorithms by Leaderboard

| `Demo` | `Description` |
| ------ | ------------- |
| <img width="400" height="225" alt="FastestReset" src="https://github.com/user-attachments/assets/71335127-6d8c-4f11-a6e8-2ee14cabf071" /> | **`Fastest Reset`** <br> Starts from a fresh save all the way to the Leaderboard unlock. Calls `unlock()` as soon as resources are ready. Most stages reuse existing scripts for simplicity, utilising item requirement or exhaustion detection. |
| <img width="400" height="225" alt="Polyculture" src="https://github.com/user-attachments/assets/f6811abe-7e51-40ee-b26c-546902a17bf1" /> | **`Trees and Carrots Polyculture`** <br> Each drone owns a cluster of 4 primary tiles. This pattern tiles the plane on maximum grid size and drone count. Companion planting is performed for each primary tile to avoid harvest wait time. |
| <img width="400" height="225" alt="Hay Polyculture" src="https://github.com/user-attachments/assets/62a3724b-c159-4346-bc20-612300d2ba10" /> | **`Hay Polyculture`** <br> Improves upon the generic polyculture script by preplanting bushes and replanting hay once if the companion is not a bush. |
| <img width="400" height="225" alt="Maze" src="https://github.com/user-attachments/assets/fd621219-b85e-4b27-84e3-ba6e86c76d28" /> | **`Maze`** <br> Drones solve 8×8 and 4×4 mazes in parallel. Each maze and drone pair first runs a wall-hugging algorithm to build an adjacency graph. Then a BFS is run repeatedly to find the shortest path to the treasure. Adjacency graphs are updated when new shortcuts are discovered.
| <img width="400" height="225" alt="Pumpkin" src="https://github.com/user-attachments/assets/7041ba9b-6e33-432c-ad15-befe44d60519" /> | **`Pumpkins`** <br> Drones partition the farm into horizontal bands and repeatedly scan their rows, planting and watering immature tiles until the east-most and west-most tiles share the same `measure()` value. Dead pumpkins are identified and replanted on subsequent passes. |
| <img width="400" height="225" alt="Cactus" src="https://github.com/user-attachments/assets/f338c34a-90d4-4dbb-9439-bd7a49da3ecc" /> | **`Cactus`** <br> Each half of the grid performs a column odd-even sort with 16 drones each, followed by a row odd-even sort. |
| <img width="400" height="225" alt="Dinosaur" src="https://github.com/user-attachments/assets/59169436-f678-4f45-8412-f61b8db63fe2" /> | **`Dinosaur`** <br> Alternates between the top and bottom halves of the grid. As the tail grows, it forces exploration of additional horizontal bands to avoid trapping itself before the grid is full. |
| <img width="400" height="225" alt="Hay Single" src="https://github.com/user-attachments/assets/86448bbf-1e1a-4c9c-b3b7-8f20ebea7c9d" /> | **`Hay Single`** <br> A single drone harvests hay on a repeating four-tile loop with pre-planted bush companions. It waters and replants between harvests on a small fixed grid. |
| <img width="400" height="225" alt="Sunflowers Single" src="https://github.com/user-attachments/assets/3d2d0fe8-7205-4658-889b-b32bf809c061" /> | **`Sunflowers Single`** <br> Plants every tile, records petal counts, then harvests in descending petal order to maximise power yield per cycle. |
| <img width="400" height="225" alt="Cactus Single" src="https://github.com/user-attachments/assets/8ce6f10b-5f29-4f25-afb0-a7bd56d86276" /> | **`Cactus Single`** <br> Single-drone insertion sort. Rows are sorted as cacti are planted, then columns, before harvesting the fully sorted grid. |

