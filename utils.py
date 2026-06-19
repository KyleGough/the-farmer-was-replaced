import multi_drone

def reset():
	clear()
	move(South)

def sleep(ticks):
	list(range(ticks - 3))

# Runs a scan until a condition is met.
def execute_until(fn, halt):
	size = get_world_size()
	while not halt():
		for _ in range(size):
			for _ in range(size):
				fn()
				move(East)
			move(South)

# Conditionally runs simple execute or multi-drone execute.append
def simple_farm(fn, halt):
	reset()
	if max_drones() > 1:
		multi_drone.execute(fn, halt)
	else:
		execute_until(fn, halt)

def water():
	if get_water() < 0.75:
		use_item(Items.Water)

def harvest_cell(entity):
	water()
	if get_ground_type() == Grounds.Grassland:
		till()
		plant(entity)
	if can_harvest():
		harvest()
	if get_entity_type() == None:
		plant(entity)

def never_halt():
	return False
