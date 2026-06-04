import utils

start = num_items(Items.Pumpkin)
required = start + 10000000 # 10m

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
	utils.reset()
	rows = set()
	size = get_world_size()	
	plant_stage(size)
	
	while not halt():
		ready = True
		
		for i in range(size):
			if i in rows:
				move(South)
				continue
			rowReady = True
			for _ in range(size):
				rowReady = harvest_cell() and rowReady
				move(East)
			if rowReady:
				rows.add(i)
			move(South)
		if len(rows) == size:
			harvest()
			rows = set()
	harvest()

def leaderboard_halt():
	return num_items(Items.Pumpkin) >= required
	
if __name__ == "__main__":
	execute(leaderboard_halt)	
	
		