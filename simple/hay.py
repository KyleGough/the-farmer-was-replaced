from utils import never_halt, simple_farm

def harvest_cell():
	if can_harvest():
		harvest()

def execute(halt):
	simple_farm(harvest_cell, halt)

if __name__ == "__main__":
	execute(never_halt)
