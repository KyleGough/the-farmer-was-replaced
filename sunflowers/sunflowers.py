import utils

start = num_items(Items.Power)
required = start + 100000 # 100k

def harvest_cell():
	utils.harvest_cell(Entities.Sunflower)
	
def execute(halt):
	utils.simple_farm(harvest_cell, halt)
	
def leaderboard_halt():
	return num_items(Items.Power) >= required
		
if __name__ == "__main__":
	execute(leaderboard_halt)		