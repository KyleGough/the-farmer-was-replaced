import utils

def move_down(n):
	for i in range(n):
		move(South)

def execute(halt):
	utils.reset()
	if num_drones() < max_drones():
		height = get_world_size() / max_drones()
		for i in range(max_drones() - 1):
			spawn_drone(harvest_pumpkin, i + 1, height, halt)
		harvest_pumpkin(0, height, halt)

def harvest_cell():
	utils.water()
	if get_ground_type() == Grounds.Grassland:
		till()
	if not can_harvest():
		plant(Entities.Pumpkin)
		return False
	return True

def harvest_row():
	m = set()
	for i in range(get_world_size()):
		harvest_cell()
		m.add(measure())
		move(East)
	return len(m) == 1

def harvest_pumpkin(id, height, halt):
	move_down(id * height)

	while not halt():
		for i in range(height):
			if harvest_row():
				harvest()
			move(South)
		for i in range(height):
			move(North)

if __name__ == "__main__":
	execute(utils.never_halt)
