import utils
import movement

start = num_items(Items.Cactus)
required = start + 33554432

def delay_drone(i, drone_count):
	utils.sleep(i * (602 + 2))

def plant_cacti_partition(height):
	for _ in range(height):
		for _ in range(get_world_size()):
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Cactus)
			move(East)
		move(South)

def plant_cacti():
	partition = get_world_size() / max_drones()
	for _ in range(max_drones() - 1):
		spawn_drone(plant_cacti_partition, partition)
		for _ in range(partition):
			move(South)
	plant_cacti_partition(partition)
	
	
def sort_column():
	for i in range(get_world_size()):
		if i % 2 == 0:
			if get_pos_y() != get_world_size() - 1 and measure(North) < measure():
				swap(North)
			else:
				utils.sleep(200)
		else:
			if measure() < measure(South):
				swap(South)
			else:
				utils.sleep(200)

def sort_row():
	for i in range(get_world_size()):
		if i % 2 == 0:
			if get_pos_x() != get_world_size() - 1 and measure(East) < measure():
				swap(East)
			else:
				utils.sleep(200)
		else:
			if measure() < measure(West):
				swap(West)
			else:
				utils.sleep(200)
		
def sort_all_columns(i, drone_count, partition):
	delay_drone(i, drone_count)
	for _ in range(get_world_size() / partition):
		sort_column()
		move(East)
		
def sort_all_rows(i, drone_count, partition):
	delay_drone(i, drone_count)
	for _ in range(get_world_size() / partition):
		sort_row()
		move(North)
		
def column_sort(drone_count, partition):
	height = get_world_size() / drone_count
	for i in range(drone_count - 1):
		spawn_drone(sort_all_columns, drone_count - i, drone_count, partition)
		for _ in range(height):
			move(South)
	sort_all_columns(1, drone_count, partition)

def row_sort(drone_count, partition):
	height = get_world_size() / drone_count
	for i in range(drone_count - 1):
		spawn_drone(sort_all_rows, drone_count - i, drone_count, partition)
		for _ in range(height):
			move(East)
	sort_all_rows(1, drone_count, partition)
	
def parallel_column_sort(drone_count):
	movement.goto(get_world_size() / 2, get_world_size() - 1)
	column_sort(drone_count, 2)
	
def parallel_row_sort(drone_count):
	movement.goto(get_world_size() - 1, get_world_size() / 2)
	row_sort(drone_count, 2)
	
def execute(drone_count, halt):
	utils.reset()
	d = drone_count / 2
	while not halt():
		plant_cacti()
		pcs_drone = spawn_drone(parallel_column_sort, d)
		column_sort(d, 2)		
		movement.goto(get_world_size() - 1, 0)
		wait_for(pcs_drone)
		prs_drone = spawn_drone(parallel_row_sort, d)
		row_sort(d, 2)
		wait_for(prs_drone)
		harvest()
		
def execute_half(drone_count, halt):
	utils.reset()
	while not halt():
		plant_cacti()
		movement.goto(0, get_world_size() - 1)
		utils.sleep(1200)
		column_sort(drone_count, 1)
		movement.goto(get_world_size() - 1, 0)
		row_sort(drone_count, 1)
		harvest()
		

def leaderboard_halt():
	return num_items(Items.Cactus) >= required

if __name__ == "__main__":
	execute(32, leaderboard_halt)