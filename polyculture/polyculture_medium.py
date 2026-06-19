# Used by the fastest reset script.
# Assumes 8 drones with a world size of 12.

from utils import never_halt
from polyculture_utils import alternate_harvest

workers = (
	(1, 2),
	(5, 2),
	(9, 2),
	(3, 5),
	(7, 5),
	(11, 5),
	(1, 8),
	(5, 8)
)

def execute(entity, required, halt):
	for (x, y) in workers:
			if num_drones() < max_drones():
				spawn_drone(alternate_harvest, entity, required, x, y, halt)
			else:
				alternate_harvest(entity, required, x, y, halt)

if __name__ == "__main__":
	set_world_size(12)
	execute(Entities.Tree, Entities.Grass, never_halt)
