# Improves upon the generic polyculture script by preplanting bushes and replanting hay once if the companion is not a bush.
# Preplant bush and ensure when planting hay that the companion is a bush. - Saved ~ 2 minutes
# Replant once instead of until indefinitely until the companion is a bush. - Saved ~ 15 seconds.

from utils import sleep, water
from movement import goto
from distribute import distribute_drones

start = num_items(Items.Hay)
required = start + 2000000000
	
def leaderboard_halt():
	return num_items(Items.Hay) >= required

# Initial plant phase to tile the grid with bushes.
def plant_bush_row():
	for _ in range(get_world_size()):
		plant(Entities.Bush)
		move(East)

# Replant if the companion is not a bush.
def replant_companion():
	if get_companion()[0] != Entities.Bush:
		till()
		till()
		plant(Entities.Grass)

# Alternates between two spots to harvest and replant.
def harvest_phase(halt):
	while not halt():
		water()
		while not can_harvest():
			use_item(Items.Fertilizer)
		harvest()
		replant_companion()
		move(South)
		water()
		while not can_harvest():
			use_item(Items.Fertilizer)
		harvest()
		replant_companion()
		move(North)
	
# Executes a drone at a specific position.
def drone_execute(x, y, halt):
	goto(x, y)
	water()
	replant_companion()
	move(South)
	water()
	replant_companion()
	move(North)
	harvest_phase(halt)
	
def execute(halt):
	size = get_world_size()	
	distribute_drones(plant_bush_row)

	# Smallest delay to allow all drones to terminate from plant phase.
	sleep(193)

	for i in range(4):
		for j in range(8):
			k = j * 4	
			x = (i * 8) + k
			y = k + 2
			if num_drones() < max_drones():	
				spawn_drone(drone_execute, x % size, y % size, halt)	
			else:	
				drone_execute(x % size, y % size, halt)
				
if __name__ == "__main__":
	execute(leaderboard_halt)