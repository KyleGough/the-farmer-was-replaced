import utils
import movement
import maze_reusable

start = num_items(Items.Gold)
required = start + 9863168

workers = [
	(4, 28, 8),
	(12, 12, 8),
	(12, 20, 8),
	(12, 28, 8),
	(20, 12, 8),
	(20, 20, 8),
	(20, 28, 8),
	(28, 4, 8),
	(28, 12, 8),
	(28, 20, 8),
	(28, 28, 8),
	(6, 22, 4),
	(6, 18, 4),
	(6, 14, 4),
	(6, 10, 4),
	(2, 22, 4),
	(2, 18, 4),
	(2, 14, 4),
	(2, 10, 4),
	(22, 6, 4),
	(22, 2, 4),
	(18, 6, 4),
	(18, 2, 4),
	(14, 6, 4),
	(14, 2, 4),
	(10, 6, 4),
	(10, 2, 4),
	(6, 6, 4),
	(6, 2, 4),
	(2, 6, 4),
	(2, 2, 4),
]

def prepare_drone(x, y, size, halt):
	movement.goto(x, y)
	utils.sleep(12 * (500 - x - y))
	maze_reusable.execute(size, 300, x, y, halt)

def execute(halt):
	utils.reset()
	
	for (x, y, size) in workers:
		spawn_drone(prepare_drone, x, y, size, halt)
	while not halt():
		do_a_flip()
	
def leaderboard_halt():
	return num_items(Items.Gold) >= required

if __name__ == "__main__":
	execute(leaderboard_halt)