# Used by the fastest reset script.
# Assumes 8 drones with a world size of 16.

import maze_multi

workers = (
	(2, 12, 8),
	(12, 12, 8),
	(14, 6, 4),
	(14, 2, 4),
	(10, 6, 4),
	(10, 2, 4),
	(6, 6, 4),
	(6, 2, 4)
)

def execute(halt):
	maze_multi.execute(workers, halt)
