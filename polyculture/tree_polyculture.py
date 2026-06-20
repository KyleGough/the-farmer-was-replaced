import polyculture

start = num_items(Items.Wood)
required = start + 10000000000

def leaderboard_halt():
	return num_items(Items.Wood) >= required

if __name__ == "__main__":
	polyculture.execute(Entities.Tree, leaderboard_halt)

