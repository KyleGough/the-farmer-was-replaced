from utils import sleep, water
from movement import goto
from distribute import distribute_drones

start = num_items(Items.Hay)
required = start + 100000000

def leaderboard_halt():
	return num_items(Items.Hay) >= required

# Prepares the farm by planting bushes.
def prepare_phase():
	companions = set()
	directions = (
		North, North, North, East,
		North, North, North, North,
		East, North, North, North,
		North, East, North, North,
		North, North, North, East,
		North, North
	)

	for dir in directions:
		move(dir)
		companions.add((Entities.Bush, (get_pos_x(), get_pos_y())))
		plant(Entities.Bush)

	move(North)
	return companions

# Alternates between four spots to harvest and replant.
def harvest_phase(companions, halt):
	while not halt():
		for direction in (North, East, South, West):
			while not can_harvest():
				continue
			harvest()
			while get_companion() not in companions:
				harvest()
			water()
			move(direction)

if __name__ == "__main__":
	set_world_size(5)
	companions = prepare_phase()
	harvest_phase(companions, leaderboard_halt)
