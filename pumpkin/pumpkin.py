import utils
import single_pumpkin
import multi_pumpkin

def execute(halt = utils.never_halt):
	utils.reset()
	if max_drones() > 1:
		multi_pumpkin.execute(halt)
	else:
		single_pumpkin.execute(halt)
		
if __name__ == "__main__":
	execute()
	
	