from utils import never_halt, reset, water

def execute(halt):
	while not halt():
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if can_harvest() or get_entity_type() != Entities.Bush:
					harvest()
					plant(Entities.Bush)
				move(East)
				water()
			move(South)

if __name__ == "__main__":
	reset()
	execute(never_halt)
