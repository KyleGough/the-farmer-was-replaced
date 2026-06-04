import polyculture
	
start = num_items(Items.Hay)
required = start + 2000000000 # 2b
	
def leaderboard_halt():
	return num_items(Items.Hay) >= required

if __name__ == "__main__":
	polyculture.execute(Entities.Grass, leaderboard_halt)
	
	