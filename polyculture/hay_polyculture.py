# Improves upon the generic polyculture script by preplanting bushes and replanting hay once if the companion is not a bush.
# Preplant bush and ensure when planting hay that the companion is a bush. - Saved ~ 2 minutes
# Replant once instead of until indefinitely until the companion is a bush. - Saved ~ 15 seconds.
# Use 4 alternating tiles instead of 2 and improve bush planting. - Saved ~ 1 minute.

from utils import reset, wait_harvest, water
from movement import goto

start = num_items(Items.Hay)
required = start + 2000000000

def leaderboard_halt():
	return num_items(Items.Hay) >= required

def prepare_phase():
	companions = set()

	directions = (
		North, North, North, West,
		South, South, North, West,
		North, North, West, South,
		North, West, North, East,
		East, North, West, East,
		North, East, South, North,
		North, East, South, South,
		East, East, South, East,
		South, West, West, South,
		North, North
	)

	for direction in directions:
		move(direction)
		companions.add((Entities.Bush, (get_pos_x(), get_pos_y())))
		plant(Entities.Bush)

	move(West)
	return companions

def harvest_phase(companions, halt):
	directions = (South, West, North, East)
	while not halt():
		for direction in directions:
			wait_harvest()
			while get_companion() not in companions:
				harvest()
			water()
			move(direction)

def alternate_harvest(entity, required, x, y, halt):
	goto(x, y)
	companions = prepare_phase()
	harvest_phase(companions, halt)

def execute(halt):
	size = get_world_size()

	for i in range(4):
		for j in range(8):
			k = j * 4
			x = (i * 8) + k + 2
			y = k + 1
			if num_drones() < max_drones():
				spawn_drone(alternate_harvest, Entities.Grass, Entities.Bush, x % size, y % size, halt)
			else:
				alternate_harvest(Entities.Grass, Entities.Bush, x % size, y % size, halt)

if __name__ == "__main__":
	reset()
	execute(leaderboard_halt)
