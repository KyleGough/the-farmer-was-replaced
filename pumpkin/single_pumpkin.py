import utils

start = num_items(Items.Pumpkin)
required = start + 10000000

def leaderboard_halt():
	return num_items(Items.Pumpkin) >= required

def harvest_cell():
	utils.water()
	if not can_harvest():
		plant(Entities.Pumpkin)
		return False
	return True

def plant_stage(size):
	for _ in range(size):
		for _ in range(size):
			till()
			use_item(Items.Water)
			plant(Entities.Pumpkin)
			move(East)
		move(South)

def execute(halt):
	rows = set()
	size = get_world_size()
	plant_stage(size)

	while not halt():
		for i in range(size):
			if i in rows:
				move(South)
				continue
			rowReady = True

			if measure() != None and measure() == measure(West):
				harvest()
				rows = set()
				break

			for _ in range(size - 1):
				rowReady = harvest_cell() and rowReady
				move(East)

			rowReady = harvest_cell() and rowReady
			move(East)

			if rowReady:
				rows.add(i)
			move(South)
		if len(rows) == size:
			harvest()
			rows = set()
	harvest()

if __name__ == "__main__":
	set_world_size(6)
	execute(leaderboard_halt)
