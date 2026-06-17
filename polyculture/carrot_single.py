import polyculture

start = num_items(Items.Carrot)
required = start + 100000000

def leaderboard_halt():
	return num_items(Items.Carrot) >= required

if __name__ == "__main__":
	set_world_size(8)
	polyculture.execute(Entities.Carrot, leaderboard_halt)
