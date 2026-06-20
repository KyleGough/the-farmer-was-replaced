# A more optimised version of the pumpkin script.
# Each drone harvests a horizontal band of pumpkins.
# Dead pumpkins are recorded in a list and replanted on the next pass.

from utils import reset, sleep, toil, water
from movement import goto_x
import distribute

start = num_items(Items.Pumpkin)
required = start + 200000000

# Distribute drones evenly across rows of the farm.
def execute(halt):
	reset()
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
			toil()
			plant(Entities.Pumpkin)
			move(East)

		# x coordinates of dead pumpkins.
		dead_pumpkins = []

		# Initial scan for dead pumpkins.
		for i in range(size):
			water()
			if not can_harvest():
				water()
				plant(Entities.Pumpkin)
				dead_pumpkins.append(i)
			move(East)

		# Replant dead pumpkins.
		while len(dead_pumpkins):
			for x in dead_pumpkins:
				goto_x(x)

				if get_entity_type() == None:
					# If the pumpkin is not found, the grid has been harvested.
					dead_pumpkins = []
					break
				elif not can_harvest():
					# If the pumpkin is dead, replant it.
					water()
					plant(Entities.Pumpkin)
					if num_items(Items.Fertilizer) > 0:
						use_item(Items.Fertilizer)
				else:
					# If the pumpkin is not dead, remove it from the list.
					dead_pumpkins.remove(x)


		goto_x(0)

		# Wait for the mega pumpkin to be ready.
		while (measure() != measure(West)) and get_entity_type() != None:
			sleep(200)

		harvest()

def leaderboard_halt():
	return num_items(Items.Pumpkin) >= required

if __name__ == "__main__":
	execute(leaderboard_halt)
