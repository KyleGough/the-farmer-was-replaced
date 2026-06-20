import polyculture

start = num_items(Items.Carrot)
required = start + 2000000000

def leaderboard_halt():
	return num_items(Items.Carrot) >= required

if __name__ == "__main__":
	polyculture.execute(Entities.Carrot, leaderboard_halt)

