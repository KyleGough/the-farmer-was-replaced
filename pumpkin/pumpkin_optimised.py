# A more optimised version of the pumpkin script.
# Each drone harvests a horizontal band of pumpkins.
# Dead pumpkins are recorded in a list and replanted on the next pass.

import utils
import movement
import distribute

start = num_items(Items.Pumpkin)
required = start + 200000000

# Distribute drones evenly across rows of the farm.
def execute(halt):
	utils.reset()
	size = get_world_size()
	distribute.distribute_drones(harvest_pumpkin_closure(size, halt))

def harvest_pumpkin_closure(size, halt):
	def wrapper():
		return harvest_pumpkin(size, halt)
	return wrapper

def harvest_pumpkin(size, halt):
	while not halt():
		# Plant a new row of pumpkins.
		for _ in range(size):
			use_item(Items.Water)
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Pumpkin)
			move(East)

		# x coordinates of dead pumpkins.
		dead_pumpkins = []

		# Initial scan for dead pumpkins.
		for i in range(size):
			utils.water()
			if not can_harvest():
				utils.water()
				plant(Entities.Pumpkin)
				dead_pumpkins.append(i)
			move(East)

		# Replant dead pumpkins.
		while len(dead_pumpkins):
			for x in dead_pumpkins:
				movement.goto_x(x)

				if get_entity_type() == None:
					# If the pumpkin is not found, the grid has been harvested.
					dead_pumpkins = []
					break
				elif not can_harvest():
					# If the pumpkin is dead, replant it.
					utils.water()
					plant(Entities.Pumpkin)
					if num_items(Items.Fertilizer) > 0:
						use_item(Items.Fertilizer)
				else:
					# If the pumpkin is not dead, remove it from the list.
					dead_pumpkins.remove(x)


		movement.goto_x(0)

		# Wait for the mega pumpkin to be ready.
		while (measure() != measure(West)) and get_entity_type() != None:
			utils.sleep(200)

		harvest()

def leaderboard_halt():
	return num_items(Items.Pumpkin) >= required

if __name__ == "__main__":
	execute(leaderboard_halt)
