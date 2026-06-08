import utils
import movement

def move_down(n):
	for _ in range(n):
		move(South)

def init_drone(height, index, harvest_fn, halt):
	movement.goto(0, get_world_size() - (index + 1) * height)

	while not halt():
		harvest_height(height, harvest_fn)

def harvest_height(height, harvest_fn):
	for _ in range(height):
		for _ in range(get_world_size()):
			utils.water()
			harvest_fn()
			move(East)
		move(South)
	for _ in range(height):
		move(North)

def execute(harvest_fn, halt):
	utils.reset()
	if num_drones() < max_drones():
		partition = get_world_size() / max_drones()
		for i in range(max_drones() - 1):
			spawn_drone(init_drone, partition, i + 1, harvest_fn, halt)
		init_drone(partition, 0, harvest_fn, halt)
