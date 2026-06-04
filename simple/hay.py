import utils

def harvest_cell():
	if can_harvest():
		harvest()
		
def execute(halt):
	utils.simple_farm(harvest_cell, halt)
		
if __name__ == "__main__":
	execute(utils.never_halt)
	