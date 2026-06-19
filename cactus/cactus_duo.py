from movement import goto
from cactus_single import row_sort, column_sort

def parallel_row_sort(size, partition, offset):
	goto(0, offset)
	for _ in range(partition):
		row_sort(size)
		move(North)

def parallel_column_sort(size, partition, offset):
	goto(offset, 0)
	for _ in range(partition):
		column_sort(size)
		move(East)

def execute():
	size = get_world_size()
	partition = size / 2
	d1 = spawn_drone(parallel_row_sort, size, partition, partition)
	parallel_row_sort(size, partition, 0)
	wait_for(d1)
	d2 = spawn_drone(parallel_column_sort, size, partition, partition)
	parallel_column_sort(size, partition, 0)
	wait_for(d2)
	harvest()

if __name__ == "__main__":
	execute()
