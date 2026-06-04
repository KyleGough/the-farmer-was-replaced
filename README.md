# The Farmer Was Replaced

Automation scripts for [**The Farmer Was Replaced**](https://thefarmerwasreplaced.com/), a programming game where you control a drone on a grid farm. You write code in a Python-like language to plant, harvest, move, and eventually coordinate multiple drones.

The in-game API is documented in [`__builtins__.py`](__builtins__.py).

## Leaderboard results

| Category | Target | Script | Time |
|----------|--------|--------|------|
| `Fastest_Reset` | - | `fastest_reset` | 1h 31m 28s |
| `Maze` | 9,863,168 | `maze_optimised` | 2m 02s |
| `Carrots` | 2,000,000,000 | `carrot_polyculture` | 5m 31s |
| `Wood` | 10,000,000,000 | `tree_polyculture` | 6m 09s |
| `Sunflowers` | 100,000 | `sunflower_setup` | 4m 03s |
| `Cactus` | 33,554,432 | `cactus_setup` | 0m 49s |
| `Hay` | 2,000,000,000 | `hay_polyculture` | 5m 10s |
| `Pumpkins` | 200,000,000 | `pumpkin_setup` | 10m 31s |
| `Pumpkins_Single` | 10,000,000 | `single_pumpkin` | 10m 03s |

## Algorithms by crop

### Polyculture: Hay, Carrots, and Wood

**Files:** `polyculture/polyculture.py`

Each drone owns a cluster of 4 primary tiles. This pattern tiles the plane on maximum grid size and drone count.

1. **Init** — spawn up to 32 drones on a grid of cluster origins; each drone plants its four primary tiles.
2. **Companion planting** — call `get_companion()` on the primary crop, `goto` to the companion coordinate, and plant the requested companion type if the tile mismatches.
3. **Primary harvest** — return to each cluster tile, water, wait until `can_harvest()`, optionally apply fertilizer + weird substance, harvest, and replant.
4. **Movement** — `goto` picks the shorter path around the toroidal farm (wrap-around edges).

Polyculture boosts yield by keeping companion plants satisfied. Water levels are kept topped up. Fertilizer accelerates grow time when a plant is not ready to be harvested.

### Pumpkins — row mega-pumpkin

**Files:** `pumpkin/pumpkin.py`, `pumpkin/multi_pumpkin.py`, `pumpkin/single_pumpkin.py`

Drones partition the farm into horizontal bands and repeatedly scan their rows, planting and watering immature tiles until every pumpkin in a row shares the same `measure()` value. Harvests the mega pumpkin for **n³** yield. Dead pumpkins are replanted on the next pass.

### Sunflowers — full-farm scan

**Files:** `sunflower.py`

Drones split the farm into rows and sweep each tile to water, till, harvest when ready, and replant sunflowers. Does not yet exploit the 5× power bonus for harvesting the max-petal sunflower last.

### Cactus — parallel odd-even sort

**Files:** `cactus/cactus_multi.py`, `cactus/plant_stage.py`

Parallel drones plant the full grid, then odd-even sort columns and rows (via `measure()` + `swap()`) until the field is sorted, triggering a recursive harvest worth **n²** cactus.

### Maze — flood fill on a shared graph

**Files:** `maze/maze_optimised.py`, `maze/maze_reusable.py`, `maze/maze.py`

Many drones run staggered 8×8 and 4×4 mazes in parallel: each wall-follows once to build an adjacency graph, flood-fills to the treasure (located via `measure()`), walks the route, and repeats the maze 300 times.
