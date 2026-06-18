# Used by the fastest reset script.
# Assumes 4 drones with a world size of 12.

import maze_multi

workers = (
	(10, 2, 6),
	(2, 10, 6),
	(10, 10, 6),
	(2, 2, 6)
)

def execute(halt):
	maze_multi.execute(workers, halt)
