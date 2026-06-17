from utils import reset, simple_farm, water
from movement import goto

start = num_items(Items.Power)
required = start + 10000

def leaderboard_halt():
	return num_items(Items.Power) >= required

# Plants sunflowers and records the number of petals on each tile.
def plant_phase():
	size = get_world_size()
	petal_map = {
		7: set(),
		8: set(),
		9: set(),
		10: set(),
		11: set(),
		12: set(),
		13: set(),
		14: set(),
		15: set()
	}

	for y in range(size):
		for x in range(size):
			water()
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Sunflower)
			petals = measure()
			petal_map[petals].add((x, y))
			move(East)
		move(North)

	return petal_map

# Harvests sunflowers in order of most petals to least petals.
def harvest_phase(petal_map):
	for count in range(15, 6, -1):
		coords = petal_map[count]
		for (x, y) in coords:
			goto(x, y)
			harvest()

def execute(halt):
	while not halt():
		petal_map = plant_phase()
		harvest_phase(petal_map)
		goto(0, 0)

if __name__ == "__main__":
	execute(leaderboard_halt)
