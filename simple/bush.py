import utils

def execute(halt = utils.never_halt):
	while not halt():
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if can_harvest() or get_entity_type() != Entities.Bush:
					harvest()			
					plant(Entities.Bush)
				move(East)
				w = get_water()
				if (w < 0.75):
					use_item(Items.Water)
			move(South)
	
if __name__ == "__main__":
	utils.reset()
	execute(utils.never_halt)