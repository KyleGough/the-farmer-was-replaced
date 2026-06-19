from fastest_reset_utils import toil, wait_harvest
from movement import goto, goto_y

def static_harvest(n):
	while num_items(Items.Hay) < n:
		wait_harvest()

def line_harvest(entity, halt):
	while not halt():
		wait_harvest()
		plant(entity)
		move(North)

def bush_3x3(halt):
	while not halt():
		for _ in range(3):
			wait_harvest()
			plant(Entities.Bush)
			move(North)
		move(East)

def hay_line(halt):
	while not halt():
		for _ in range(3):
			harvest()
			move(North)

def balanced_3x3(halt):
	while not halt():
		for _ in range(3):
			harvest()
			move(North)
		move(East)
		for _ in range(3):
			wait_harvest()
			plant(Entities.Bush)
			move(North)
		move(East)
		for _ in range(3):
			wait_harvest()
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Carrot)
			move(North)
		move(East)


def balanced_3x3_tree(halt):
	while not halt():
		# First column.
		goto(0, 0)
		wait_harvest()
		plant(Entities.Tree)
		move(North)
		wait_harvest()
		move(North)
		wait_harvest()
		plant(Entities.Tree)
		move(North)
		move(East)

		# Second column
		for _ in range(3):
			harvest()
			move(North)
		move(East)

		# Third column.
		for _ in range(3):
			harvest()
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Carrot)
			move(North)
		move(East)

def balanced_4x4(halt):
	while not halt():
		for _ in range(2):
			for _ in range(2):
				harvest()
				plant(Entities.Tree)
				move(North)
				harvest()
				toil()
				plant(Entities.Carrot)
				move(North)
			move(East)
			for _ in range(4):
				harvest()
				move(North)
			move(East)

def tree_carrot_6x6(halt):
	while not halt():
		for _ in range(3):
			for _ in range(3):
				harvest()
				plant(Entities.Tree)
				move(North)
				harvest()
				toil()
				plant(Entities.Carrot)
				move(North)
			move(East)
			for _ in range(3):
				harvest()
				toil()
				plant(Entities.Carrot)
				move(North)
				harvest()
				plant(Entities.Tree)
				move(North)
			move(East)

def balanced_6x6(halt):
	while not halt():
		for _ in range(2):
			for _ in range(3):
				wait_harvest()
				plant(Entities.Tree)
				move(North)
				harvest()
				toil()
				plant(Entities.Carrot)
				move(North)
			move(East)
			for _ in range(3):
				harvest()
				toil()
				plant(Entities.Carrot)
				move(North)
				wait_harvest()
				plant(Entities.Tree)
				move(North)
			move(East)
			for _ in range(6):
				harvest()

def hay_6x6(halt):
	while not halt():
		for _ in range(6):
			for _ in range(6):
				harvest()
				move(North)
			move(East)

def plant_bush_section(y, height):
	goto_y(y)
	for _ in range(height):
		for _ in range(12):
			plant(Entities.Bush)
			move(East)
		move(South)

def prepare_bush_polyculture_medium():
	for i in range(6):
		if num_drones() < max_drones():
			spawn_drone(plant_bush_section, i * 2, 2)
		else:
			plant_bush_section(i * 2, 2)

def prepare_bush_polyculture_large():
	for i in range(16):
		if num_drones() < max_drones():
			spawn_drone(plant_bush_section, i, 1)
		else:
			plant_bush_section(i, 1)
