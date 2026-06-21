from utils import toil, water
from movement import goto

def spawn_drones_binary_tree(fn, workers, halt, start, end):
	count = end - start
	if count == 1:
		x, y, size = workers[start]
		fn(x, y, size, halt)
		return

	mid = start + count // 2
	spawn_drone(spawn_drones_binary_tree, fn, workers, halt, mid, end)
	spawn_drones_binary_tree(fn, workers, halt, start, mid)

def distribute_binary_tree(fn, workers, halt):
	spawn_drones_binary_tree(fn, workers, halt, 0, len(workers))
