hats = [Hats.Brown_Hat, Hats.Gold_Hat, Hats.Gray_Hat, Hats.Green_Hat, Hats.Purple_Hat]

def equipHat(i):
	change_hat(hats[i % len(hats)])
	# Delay
	for n in range(10):
		till()

def execute():
	for i in range(max_drones() - 1):
		spawn_drone(equipHat, i + 1)
	equipHat(0)
	
if __name__ == "__main__":
	execute()