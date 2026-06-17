import polyculture

start = num_items(Items.Wood)
required = start + 500000000

def leaderboard_halt():
	return num_items(Items.Wood) >= required

if __name__ == "__main__":
	set_world_size(8)
	polyculture.execute(Entities.Tree, leaderboard_halt)
