from utils import sleep, water
from movement import goto
from distribute import distribute_drones

start = num_items(Items.Hay)
required = start + 100000000
	
def leaderboard_halt():
	return num_items(Items.Hay) >= required

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
	
def drone_execute(halt):
	water()
	
	directions = [
		North, East, North, West,
		North, East, North, East,
		South, East, North, East,
		South, South, South, South,
		West, North, West, South,
		West
	]
	
	for dir in directions:
		move(dir)
		plant(Entities.Bush)
		
	move(West)
	water()
	replant_companion()
	move(South)
	water()
	replant_companion()
	move(North)
	harvest_phase(halt)
	
def execute(halt):
	set_world_size(5)	
	drone_execute(halt)
				
if __name__ == "__main__":
	execute(leaderboard_halt)