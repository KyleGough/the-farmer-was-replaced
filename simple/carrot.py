import utils

def harvest_cell():
	utils.harvest_cell(Entities.Carrot)

def execute(halt):
	utils.simple_farm(harvest_cell, halt)

if __name__ == "__main__":
	execute(utils.never_halt)
