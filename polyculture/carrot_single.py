import polyculture

start = num_items(Items.Carrot)
required = start + 100000000

def leaderboard_halt():
	return num_items(Items.Carrot) >= required

def execute(halt):
	polyculture.execute(Entities.Carrot, halt)

if __name__ == "__main__":
	set_world_size(8)
	execute(leaderboard_halt)
