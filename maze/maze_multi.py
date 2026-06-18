from utils import reset, sleep
from movement import goto
import maze_reusable

def prepare_drone(x, y, size, halt):
	goto(x, y)
	sleep(12 * (500 - x - y))
	maze_reusable.execute(size, 300, x, y, halt)

def execute(workers, halt):
	reset()

	for (x, y, size) in workers:
		if num_drones() < max_drones():
			spawn_drone(prepare_drone, x, y, size, halt)
		else:
			prepare_drone(x, y, size, halt)
