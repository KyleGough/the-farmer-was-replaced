from utils import water
from movement import goto

# Replant if the companion is the required companion.
def replant_companion(entity, required):
	if get_companion()[0] != required:
		till()
		till()
		plant(entity)

# Alternates between two spots to harvest and replant.
def harvest_phase(entity, required, halt):
	while not halt():
		water()
		while not can_harvest():
			use_item(Items.Fertilizer)
		harvest()
		replant_companion(entity, required)
		move(South)
		water()
		while not can_harvest():
			use_item(Items.Fertilizer)
		harvest()
		replant_companion(entity, required)
		move(North)

# Executes a drone at a specific position.
def alternate_harvest(entity, required, x, y, halt):
	goto(x, y)
	water()
	if entity == Entities.Carrot:
		till()
	replant_companion(entity, required)
	move(South)
	water()
	if entity == Entities.Carrot:
		till()
	replant_companion(entity, required)
	move(North)
	harvest_phase(entity, required, halt)
