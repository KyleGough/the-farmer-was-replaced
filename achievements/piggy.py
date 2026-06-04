import utils

def pet(n):
	for i in range(n):
		pet_the_piggy()

def execute(total_flips):
	n = total_flips / max_drones()
	for i in range(max_drones() - 1):
		spawn_drone(pet, n)
	pet(n)

if __name__ == "__main__":
	utils.reset()
	execute(1000)