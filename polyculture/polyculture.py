import utils
import movement

positions = [(0, 0), (3, 1), (2, -2), (5, -1)]

def init_plant(primary, x, y):
	movement.goto(x, y)	
	if primary == Entities.Carrot and get_ground_type() == Grounds.Grassland:
		till()
	plant(primary)
	if num_items(Items.Water) > 0:
		use_item(Items.Water)

def harvest_loop(primary, cx, cy):
	for (x, y) in positions:
		plant_companion(primary)
		plant_primary(primary, cx + x, cy + y)

def plant_companion(primary):
	companion = get_companion()
	if companion == None:
		return
		
	plant_type, (x, y) = companion
	movement.goto(x, y)
	
	# Do nothing if plant type is already correct.
	current = get_entity_type()
	if current == plant_type:
		return
	
	# Till and plant carrot.
	if plant_type == Entities.Carrot and get_ground_type() == Grounds.Grassland:
		till()
		plant(plant_type)
	else:		
		harvest()
		plant(plant_type)
		
def plant_primary(primary, x, y):
	movement.goto(x, y)

	use_item(Items.Water)
	
	while not can_harvest() and get_entity_type() != None:
		if num_items(Items.Fertilizer) > 32:
			use_item(Items.Fertilizer)
			use_item(Items.Weird_Substance)
	
	harvest()

	plant(primary)
		
def drone_execute(primary, x, y, halt):
	for (cx, cy) in positions:
		init_plant(primary, x + cx, y + cy)
	while not halt():
		harvest_loop(primary, x, y)
	
def execute(primary, halt):
	utils.reset()
	size = get_world_size()	

	for i in range(4):
		for j in range(8):		
			x = (i * 8) + (j * 4)
			y = (j * 4) + 2
			if num_drones() < max_drones():	
				spawn_drone(drone_execute, primary, x  % size, y % size, halt)	
			else:	
				drone_execute(primary, x % size, y % size, halt)