import utils
import movement

# Relative positions of the companion drones.
positions = [(0, 0), (3, 1), (2, -2), (5, -1)]

# Plant a primary plant on a specific tile.
def init_plant(primary, x, y):
	movement.goto(x, y)	
	if primary == Entities.Carrot and get_ground_type() == Grounds.Grassland:
		till()
	plant(primary)
	if num_items(Items.Water) > 0:
		use_item(Items.Water)

def harvest_loop(primary, cx, cy, size, weird_substance):
	for (x, y) in positions:
		plant_companion(primary)
		plant_primary(primary, (cx + x) % size, (cy + y) % size, weird_substance)

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
	else:		
		harvest()
	plant(plant_type)
		
def plant_primary(primary, x, y, weird_substance):
	movement.goto(x, y)

	use_item(Items.Water)
	
	while not can_harvest() and get_entity_type() != None:
		if num_items(Items.Fertilizer) > 32:
			use_item(Items.Fertilizer)
			use_item(Items.Weird_Substance)
	
	if weird_substance:
		use_item(Items.Fertilizer)
	harvest()

	plant(primary)
		
def drone_execute(primary, x, y, size, weird_substance, halt):
	for (cx, cy) in positions:
		init_plant(primary, x + cx, y + cy)
	while not halt():
		harvest_loop(primary, x, y, size, weird_substance)
	
def execute(primary, halt, weird_substance = False):
	utils.reset()
	size = get_world_size()	

	for i in range(4):
		for j in range(8):		
			x = (i * 8) + (j * 4)
			y = (j * 4) + 2
			if num_drones() < max_drones():	
				spawn_drone(drone_execute, primary, x  % size, y % size, size, weird_substance, halt)	
			else:	
				drone_execute(primary, x % size, y % size, size, weird_substance, halt)