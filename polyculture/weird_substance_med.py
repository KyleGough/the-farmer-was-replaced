from utils import never_halt
from polyculture import drone_execute

workers = (
	(12, 14),
	(4, 14),
	(8, 10),
	(0, 10),
	(12, 6),
	(4, 6),
	(8, 2),
	(0, 2)
)

def execute(halt):
	for (x, y) in workers:
		if num_drones() < max_drones():
			spawn_drone(drone_execute, Entities.Tree, x, y, 16, True, halt)
		else:
			drone_execute(Entities.Tree, x, y, 16, True, halt)
	while not halt():
		continue

if __name__ == "__main__":
	set_world_size(16)
	execute(never_halt)
