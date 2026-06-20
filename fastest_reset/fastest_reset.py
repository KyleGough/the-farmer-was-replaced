from custom_harvest import static_harvest, line_harvest, bush_3x3, hay_line, balanced_3x3, balanced_3x3_tree, balanced_4x4, tree_carrot_6x6, balanced_6x6, hay_6x6, prepare_bush_polyculture_medium, prepare_bush_polyculture_large
from movement import goto_y
import sunflowers_single
import sunflowers
import pumpkin_single
import pumpkin_multi
import carrot_duo
import polyculture
import maze_reusable
import maze_multi
import hay_single
import cactus_duo
import cactus_odd_even_sort
import dinosaur_simple
import trees_carrots
import polyculture_medium
import polyculture_large
import weird_substance_med

# Current unlock amounts.
unlock_amount = {
	Unlocks.Grass: 1
}

def upgrade(u):
	if not unlock(u):
		quick_print("Unable to unlock", u)
		while True:
			do_a_flip()
	if u in unlock_amount:
		unlock_amount[u] += 1
	else:
		unlock_amount[u] = 1
	quick_print("[", get_time(), "]", u, unlock_amount[u])

def item_halt(item, n):
	def halt():
		return num_items(item) >= n
	return halt

def execute():
	# Speed 1
	static_harvest(20)
	upgrade(Unlocks.Speed)

	# Plant 1
	static_harvest(50)
	upgrade(Unlocks.Plant)

	# Expand 1
	static_harvest(30)
	upgrade(Unlocks.Expand)

	# Expand 2
	halt = item_halt(Items.Wood, 20)
	line_harvest(Entities.Bush, halt)
	upgrade(Unlocks.Expand)

	# Speed 2
	halt = item_halt(Items.Wood, 20)
	bush_3x3(halt)
	upgrade(Unlocks.Speed)

	# Carrots 1
	halt = item_halt(Items.Wood, 50)
	bush_3x3(halt)
	upgrade(Unlocks.Carrots)

	# Grass 2
	halt = item_halt(Items.Hay, 300)
	hay_line(halt)
	upgrade(Unlocks.Grass)

	# Trees 1
	halt = item_halt(Items.Carrot, 70)
	balanced_3x3(halt)
	halt = item_halt(Items.Wood, 50)
	balanced_3x3(halt)
	upgrade(Unlocks.Trees)

	# Trees 2
	halt = item_halt(Items.Hay, 300)
	hay_line(halt)
	upgrade(Unlocks.Trees)

	# Expand 3
	halt = item_halt(Items.Carrot, 30)
	balanced_3x3_tree(halt)
	halt = item_halt(Items.Wood, 20)
	balanced_3x3_tree(halt)
	upgrade(Unlocks.Expand)

	# Speed 3
	halt = item_halt(Items.Wood, 50)
	balanced_4x4(halt)
	halt = item_halt(Items.Carrot, 50)
	balanced_4x4(halt)
	upgrade(Unlocks.Speed)

	# Carrots 2
	halt = item_halt(Items.Wood, 250)
	balanced_4x4(halt)
	upgrade(Unlocks.Carrots)

	# Expand 4
	halt = item_halt(Items.Wood, 100)
	balanced_4x4(halt)
	halt = item_halt(Items.Carrot, 50)
	balanced_4x4(halt)
	upgrade(Unlocks.Expand)

	# Watering 1
	halt = item_halt(Items.Wood, 50)
	balanced_4x4(halt)
	upgrade(Unlocks.Watering)

	# Watering 2
	halt = item_halt(Items.Wood, 200)
	balanced_4x4(halt)
	upgrade(Unlocks.Watering)

	# Carrots 3
	halt = item_halt(Items.Wood, 1750)
	tree_carrot_6x6(halt)
	upgrade(Unlocks.Carrots)

	# Grass 3
	upgrade(Unlocks.Grass)

	# Sunflowers
	halt = item_halt(Items.Carrot, 500)
	tree_carrot_6x6(halt)
	upgrade(Unlocks.Sunflowers)

	# Power
	clear()
	halt = item_halt(Items.Carrot, 500)
	balanced_6x6(halt)
	clear()
	halt = item_halt(Items.Power, 300)
	sunflowers_single.execute(halt)

	# Fertilizer 1
	clear()
	halt = item_halt(Items.Wood, 500)
	balanced_6x6(halt)
	upgrade(Unlocks.Fertilizer)

	# Watering 3
	halt = item_halt(Items.Wood, 800)
	balanced_6x6(halt)
	upgrade(Unlocks.Watering)

	# Speed 4
	halt = item_halt(Items.Carrot, 500)
	balanced_6x6(halt)
	upgrade(Unlocks.Speed)

	# Pumpkins 1
	clear()
	halt = item_halt(Items.Wood, 500)
	tree_carrot_6x6(halt)
	halt = item_halt(Items.Carrot, 200)
	tree_carrot_6x6(halt)
	upgrade(Unlocks.Pumpkins)

	# Watering 4
	clear()
	halt = item_halt(Items.Hay, 2000)
	hay_6x6(halt)
	clear()
	halt = item_halt(Items.Wood, 3200)
	balanced_6x6(halt)
	upgrade(Unlocks.Watering)

	# Pumpkins 2
	upgrade(Unlocks.Pumpkins)

	# Polyculture 1
	halt = item_halt(Items.Carrot, 750)
	balanced_6x6(halt)
	clear()
	halt = item_halt(Items.Pumpkin, 3000)
	pumpkin_single.execute(halt)
	upgrade(Unlocks.Polyculture)

	# Speed 5
	clear()
	halt = item_halt(Items.Wood, 500)
	polyculture.drone_execute(Entities.Tree, 0, 0, 6, True, halt)
	clear()
	halt = item_halt(Items.Carrot, 1000)
	polyculture.drone_execute(Entities.Carrot, 0, 0, 6, False, halt)
	upgrade(Unlocks.Speed)

	# Expand 5
	halt = item_halt(Items.Carrot, 350)
	polyculture.drone_execute(Entities.Carrot, 0, 0, 6, False, halt)
	clear()
	halt = item_halt(Items.Pumpkin, 1000)
	pumpkin_single.execute(halt)
	upgrade(Unlocks.Expand)

	# Fertilizer 2
	clear()
	halt = item_halt(Items.Wood, 1500)
	polyculture.drone_execute(Entities.Tree, 0, 0, 8, True, halt)
	upgrade(Unlocks.Fertilizer)

	# Mazes 1
	halt = item_halt(Items.Weird_Substance, 2500)
	polyculture.drone_execute(Entities.Tree, 0, 0, 8, True, halt)
	upgrade(Unlocks.Mazes)

	# Megafarm 1
	clear()
	halt = item_halt(Items.Gold, 2000)
	maze_reusable.execute(8, 300, 0, 0, halt)
	upgrade(Unlocks.Megafarm)

	# Grass 4
	upgrade(Unlocks.Grass)

	# Hats
	upgrade(Unlocks.Hats)

	# Power TODO
	halt = item_halt(Items.Carrot, 900)
	clear()
	polyculture.drone_execute(Entities.Carrot, 0, 0, 8, False, halt)
	halt = item_halt(Items.Power, 3500)
	clear()
	sunflowers_single.execute(halt)

	# Trees 3 TODO - multi drone
	halt = item_halt(Items.Hay, 9200)
	hay_single.execute(halt)
	upgrade(Unlocks.Trees)

	# Trees 4
	upgrade(Unlocks.Trees)

	# Carrots 4
	upgrade(Unlocks.Carrots)

	# Watering 5
	clear()
	halt = item_halt(Items.Wood, 12800)
	polyculture.drone_execute(Entities.Tree, 0, 0, 8, False, halt)
	upgrade(Unlocks.Watering)

	# Pumpkins 3
	set_world_size(8)
	halt = item_halt(Items.Carrot, 4000)
	polyculture.drone_execute(Entities.Carrot, 0, 0, 8, False, halt)
	upgrade(Unlocks.Pumpkins)

	# Expand 6
	clear()
	halt = item_halt(Items.Carrot, 3250)
	carrot_duo.execute(halt)
	halt = item_halt(Items.Pumpkin, 8000)
	pumpkin_multi.execute(halt)
	upgrade(Unlocks.Expand)

	# Cactus 1
	halt = item_halt(Items.Pumpkin, 5000)
	pumpkin_multi.execute(halt)
	upgrade(Unlocks.Cactus)

	# Dinosaurs 1
	clear()
	halt = item_halt(Items.Cactus, 2000)
	cactus_duo.execute()
	upgrade(Unlocks.Dinosaurs)

	# Dinosaurs 2
	halt = item_halt(Items.Cactus, 12000)
	while not halt():
		cactus_duo.execute()
	upgrade(Unlocks.Dinosaurs)

	# Polyculture 2
	halt = item_halt(Items.Bone, 10000)
	dinosaur_simple.execute(halt)
	upgrade(Unlocks.Polyculture)

	# Mazes 2
	halt = item_halt(Items.Cactus, 12000)
	while not halt():
		cactus_duo.execute()
	upgrade(Unlocks.Mazes)

	# Mazes 3
	clear()
	halt = item_halt(Items.Carrot, 1500)
	carrot_duo.execute(halt)
	clear()
	halt = item_halt(Items.Pumpkin, 2000)
	pumpkin_multi.execute(halt)
	clear()
	halt = item_halt(Items.Cactus, 72000)
	while not halt():
		cactus_duo.execute()
	upgrade(Unlocks.Mazes)

	# Megafarm 2 TODO
	set_world_size(12)
	halt = item_halt(Items.Weird_Substance, 6000)
	polyculture.drone_execute(Entities.Tree, 0, 0, 12, True, halt)
	clear()
	halt = item_halt(Items.Gold, 8000)
	maze_reusable.execute(12, 300, 0, 0, halt)
	upgrade(Unlocks.Megafarm)

	# Megafarm 3
	halt = item_halt(Items.Gold, 32000)
	maze_multi.execute(halt)
	upgrade(Unlocks.Megafarm)

	# Trees 5 TODO
	clear()
	set_world_size(5)
	halt = item_halt(Items.Hay, 19200)
	hay_single.execute(halt)
	upgrade(Unlocks.Trees)

	set_world_size(12)

	def harvest_hay_row(y):
		def harvest_fn():
			goto_y(y)
			while True:
				harvest()
				move(East)
		return harvest_fn
	spawn_drone(harvest_hay_row(5))
	spawn_drone(harvest_hay_row(6))

	# Fertilizer 3
	clear()
	halt = item_halt(Items.Wood, 9000)
	polyculture_medium.execute(Entities.Tree, Entities.Grass, halt)
	upgrade(Unlocks.Fertilizer)

	# Fertilizer 4
	clear()
	halt = item_halt(Items.Wood, 54000)
	polyculture_medium.execute(Entities.Tree, Entities.Grass, halt)
	upgrade(Unlocks.Fertilizer)

	# Watering 6
	clear()
	halt = item_halt(Items.Wood, 51200)
	polyculture_medium.execute(Entities.Tree, Entities.Grass, halt)
	upgrade(Unlocks.Watering)

	# Carrots 5
	clear()
	halt = item_halt(Items.Wood, 31200)
	polyculture_medium.execute(Entities.Tree, Entities.Grass, halt)
	upgrade(Unlocks.Carrots)

	# Carrots 6
	clear()
	halt = item_halt(Items.Hay, 17500)
	prepare_bush_polyculture_medium()
	polyculture_medium.execute(Entities.Grass, Entities.Bush, halt)
	clear()
	halt = item_halt(Items.Wood, 175000)
	polyculture_medium.execute(Entities.Tree, Entities.Grass, halt)
	upgrade(Unlocks.Carrots)

	# Pumpkins 4
	clear()
	halt = item_halt(Items.Carrot, 96000)
	polyculture_medium.execute(Entities.Carrot, Entities.Grass, halt)
	clear()
	upgrade(Unlocks.Pumpkins)

	# Pumpkins 5
	upgrade(Unlocks.Pumpkins)

	# Expand 7
	clear()
	halt = item_halt(Items.Pumpkin, 64000)
	pumpkin_multi.execute(halt)
	upgrade(Unlocks.Expand)

	# Megafarm 4
	set_world_size(16)
	clear()
	halt = item_halt(Items.Gold, 128000)
	maze_multi.execute(halt)
	upgrade(Unlocks.Megafarm)

	# Final power restock.
	clear()
	halt = item_halt(Items.Hay, 9500)
	prepare_bush_polyculture_large()
	polyculture_large.execute(Entities.Grass, Entities.Grass, halt)
	clear()
	halt = item_halt(Items.Carrot, 4500)
	polyculture_large.execute(Entities.Carrot, Entities.Grass, halt)
	clear()
	halt = item_halt(Items.Power, 8100)
	sunflowers.execute(halt)

	# Cactus 2
	clear()
	halt = item_halt(Items.Carrot, 50000)
	trees_carrots.execute(halt)
	halt = item_halt(Items.Pumpkin, 20000)
	pumpkin_multi.execute(halt)
	upgrade(Unlocks.Cactus)

	# Cactus 3
	halt = item_halt(Items.Pumpkin, 160000)
	pumpkin_multi.execute(halt)
	upgrade(Unlocks.Cactus)

	# Dinosaurs 3
	clear()
	halt = item_halt(Items.Cactus, 72000 + 432000 + 2590000 + 432000 + 20000)
	cactus_odd_even_sort.execute(16, halt)
	upgrade(Unlocks.Dinosaurs)

	# Dinosaurs 4
	upgrade(Unlocks.Dinosaurs)

	# Dinosaurs 5
	upgrade(Unlocks.Dinosaurs)

	# Mazes 4
	upgrade(Unlocks.Mazes)

	# Leaderboard
	clear()
	halt = item_halt(Items.Hay, 5000)
	prepare_bush_polyculture_large()
	polyculture_large.execute(Entities.Grass, Entities.Grass, halt)
	halt = item_halt(Items.Weird_Substance, 260000)
	weird_substance_med.execute(halt)
	clear()
	halt = item_halt(Items.Bone, 2000000)
	dinosaur_simple.execute(halt)
	halt = item_halt(Items.Gold, 1000000)
	maze_multi.execute(halt)
	clear()
	upgrade(Unlocks.Leaderboard)

if __name__ == "__main__":
	execute()
