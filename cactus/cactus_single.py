from movement import goto_x, goto_y

def row_sort(size):
	for x in range(size):
		goto_x(x)
		pos = x
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Cactus)
		while pos > 0 and measure() < measure(West):
			swap(West)
			move(West)
			pos -= 1

def column_sort(size):
	for y in range(size):
		goto_y(y)
		pos = y
		while pos > 0 and measure() < measure(South):
			swap(South)
			move(South)
			pos -= 1

def execute():
	size = get_world_size()
	for _ in range(size):
		row_sort(size)
		move(North)
	for _ in range(size):
		column_sort(size)
		move(East)
	harvest()

if __name__ == "__main__":
	execute()
