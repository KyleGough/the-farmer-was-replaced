# Fashion Show
# Equip 5 different hats on 5 drones.

hats = [Hats.Brown_Hat, Hats.Gold_Hat, Hats.Gray_Hat, Hats.Green_Hat, Hats.Purple_Hat]

def equipHat(i):
	change_hat(hats[i % len(hats)])
	# Delay
	for n in range(5):
		do_a_flip()

def execute():
	spawn_drone(equipHat, 0)
	spawn_drone(equipHat, 1)
	spawn_drone(equipHat, 2)
	spawn_drone(equipHat, 3)
	equipHat(4)
	