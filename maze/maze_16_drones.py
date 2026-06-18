# Used by the fastest reset script.
# Assumes 16 drones with a world size of 16.remove

import maze_multi

workers = (
	(14, 14, 4),
	(14, 10, 4),
	(14, 6, 4),
	(14, 2, 4),
	(10, 14, 4),
	(10, 10, 4),
	(10, 6, 4),
	(10, 2, 4),
	(6, 14, 4),
	(6, 10, 4),
	(6, 6, 4),
	(6, 2, 4),
	(2, 14, 4),
	(2, 10, 4),
	(2, 6, 4),
	(2, 2, 4)
)

def execute(halt):
	maze_multi.execute(workers, halt)
