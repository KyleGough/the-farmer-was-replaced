import utils
import carrot

# Trees and Carrots in a checkerboard pattern.
def harvest_cell():
	utils.water()
		
	if can_harvest():
		harvest()
		
	x = get_pos_x()
	y = get_pos_y()
		
	if ((x + y) % 2 == 0):
		plant(Entities.Tree)
	else:
		carrot.harvest_cell()

	use_item(Items.Fertilizer)
		
def execute(halt):
	utils.simple_farm(harvest_cell, halt)

if __name__ == "__main__":
	execute(utils.never_halt)