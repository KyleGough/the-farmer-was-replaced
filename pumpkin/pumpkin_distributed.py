from utils import toil, water
from movement import goto
from distribute_binary_tree import distribute_binary_tree

start = num_items(Items.Pumpkin)
required = start + 200000000

def leaderboard_halt():
	return num_items(Items.Pumpkin) >= required

def plant_pumpkin():
	toil()
	water()
	plant(Entities.Pumpkin)

vertical_direction = (North, South)

def harvest_half(x, y, size):
	dead_pumpkins = set()

	def check_dead_pumpkin():
		if not can_harvest():
			plant(Entities.Pumpkin)
			dx = get_pos_x()
			dy = get_pos_y()
			dead_pumpkins.add((dx, dy))

	def scan_grid(fn):
		for i in range(size / 2):
			for _ in range(size - 1):
				fn()
				move(vertical_direction[i % 2])
			fn()
			move(East)

	# Plant phase.
	goto(x, y)
	scan_grid(plant_pumpkin)

	# Check phase.
	goto(x, y)
	scan_grid(check_dead_pumpkin)

	# Replant phase.
	while len(dead_pumpkins):
		next_pass = set()
		for (rx, ry) in dead_pumpkins:
			goto(rx, ry)
			if not can_harvest():
				plant(Entities.Pumpkin)
				next_pass.add((rx, ry))
		dead_pumpkins = next_pass

def harvest_pumpkin(x, y, size, halt):
	goto(x, y)
	while not halt():
		# Right half.
		d = spawn_drone(harvest_half, x + size // 2, y, size)
		# Left half.
		harvest_half(x, y, size)
		wait_for(d)
		harvest()

workers = (
	(0, 0, 8),
	(9, 0, 8),
	(0, 9, 8),
	(8, 16, 8),
	(0, 18, 7),
	(0, 26, 6),
	(9, 9, 6),
	(7, 25, 7),
	(18, 0, 7),
	(26, 0, 6),
	(16, 8, 8),
	(25, 7, 7),
	(17, 17, 6),
	(24, 15, 8),
	(15, 24, 8),
	(24, 24, 8)
)

def execute(halt):
	distribute_binary_tree(harvest_pumpkin, workers, halt)

if __name__ == "__main__":
	clear()
	execute(leaderboard_halt)
