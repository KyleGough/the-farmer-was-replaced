import utils

def perform_flip(n):
	for i in range(n):
		do_a_flip()

def execute(total_flips):
	n = total_flips / max_drones()
	for i in range(max_drones() - 1):
		spawn_drone(perform_flip, n)
	perform_flip(n)

if __name__ == "__main__":
	utils.reset()
	execute(1000)