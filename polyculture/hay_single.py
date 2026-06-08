from utils import sleep, water
from movement import goto
from distribute import distribute_drones

start = num_items(Items.Hay)
required = start + 100000000
	
def leaderboard_halt():
	return num_items(Items.Hay) >= required

# Alternates between two spots to harvest and replant.
def harvest_phase(halt):
	while not halt():
		while not can_harvest():
			water()
		harvest()		
		move(South)
		while not can_harvest():
			water()
		harvest()		
		move(North)

	
def execute(halt):
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
	harvest_phase(halt)
			
if __name__ == "__main__":
	set_world_size(5)
	execute(leaderboard_halt)