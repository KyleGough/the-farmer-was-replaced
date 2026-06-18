from utils import never_halt, water
from movement import goto_x

def harvest_column(pos, size, halt):
	goto_x(pos)
	while not halt():
		for _ in range(size):
			if get_ground_type() == Grounds.Grassland:
				till()
				plant(Entities.Carrot)
				water()
			if can_harvest():
				harvest()
				plant(Entities.Carrot)
				water()
			plant_type, (x, y) = get_companion()
			if plant_type != Entities.Grass or x == pos:
				till()
				till()
				plant(Entities.Carrot)
			move(North)

def execute(halt):
	size = get_world_size()
	spawn_drone(harvest_column, size / 2, size, halt)
	harvest_column(0, size, halt)

if __name__ == "__main__":
	set_world_size(8)
	execute(never_halt)
