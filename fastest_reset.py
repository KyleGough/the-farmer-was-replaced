import hay
import bush
import carrot
import trees_carrots
import sunflower
import pumpkin
import weird_substance
import maze
import maze_reusable
import maze_optimised
import cactus_odd_even_sort
import dinosaur
import polyculture
import utils

item_unlock_map = {
  Items.Hay: Unlocks.Grass,
  Items.Carrot: Unlocks.Carrots
}

# Current unlock amounts.
unlock_amount = {
	Unlocks.Grass: 1
}

def buffer():
	return 2 * (get_world_size() ** 2)

def item_halt(item, n):
	def halt():
		return num_items(item) >= n
	return halt

def exhaust_item(item):
	def halt():
		return num_items(item) <= 2 ** num_unlocked(item_unlock_map[item])
	return halt

def stationary_hay(n):
	while num_items(Items.Hay) < n:
		if can_harvest():
			harvest()

def line_harvest_hay(n):
	while num_items(Items.Hay) < n:
		harvest()
		move(North)

def line_harvest_bush(n):
	while num_items(Items.Wood) < n:
		plant(Entities.Bush)
		move(North)
		if can_harvest():
			harvest()

def line_harvest_carrot(n):
	while num_items(Items.Carrot) < n:
		plant(Entities.Carrot)
		move(North)
		if can_harvest():
			harvest()

def unlock_check(u):
	unlock(u)
	if u in unlock_amount:
		unlock_amount[u] += 1
	else:
		unlock_amount[u] = 1
	quick_print("Unlocked: ", u, unlock_amount[u])

def get_unlock_cost(u):
	if u in unlock_amount:
		level = unlock_amount[u]
	else:
		level = 0
	return get_cost(u, level)

# Speed 1
cost = get_unlock_cost(Unlocks.Speed)[Items.Hay]
stationary_hay(cost)
unlock_check(Unlocks.Speed)

# Expand 1
cost = get_unlock_cost(Unlocks.Expand)[Items.Hay]
stationary_hay(cost)
unlock_check(Unlocks.Expand)

# Plant
cost = get_unlock_cost(Unlocks.Plant)[Items.Hay]
line_harvest_hay(cost)
unlock_check(Unlocks.Plant)

# Speed 2
cost = get_unlock_cost(Unlocks.Speed)[Items.Wood]
line_harvest_bush(cost)
unlock_check(Unlocks.Speed)

# Expand 2
cost = get_unlock_cost(Unlocks.Expand)[Items.Wood]
line_harvest_bush(cost)
unlock_check(Unlocks.Expand)

# Carrots 1
speed_cost = get_unlock_cost(Unlocks.Speed)
carrot_cost = get_unlock_cost(Unlocks.Carrots)
cost = carrot_cost[Items.Wood]
cost += speed_cost[Items.Wood]
cost += speed_cost[Items.Carrot]
cost += get_world_size() ** 2
bush.execute(item_halt(Items.Wood, cost))
unlock_check(Unlocks.Carrots)

# Speed 3
cost = speed_cost[Items.Carrot]
hay.execute(item_halt(Items.Hay, cost))
carrot.execute(item_halt(Items.Carrot, cost))
unlock_check(Unlocks.Speed)

# Grass 2
grass_cost = get_unlock_cost(Unlocks.Grass)
cost = grass_cost[Items.Hay]
hay.execute(item_halt(Items.Hay, cost))
unlock_check(Unlocks.Grass)

# Expand 3
expand_cost = get_unlock_cost(Unlocks.Expand)
cost = expand_cost[Items.Carrot]
hay.execute(item_halt(Items.Hay, cost))
cost = expand_cost[Items.Wood] + expand_cost[Items.Carrot]
cost += buffer()
bush.execute(item_halt(Items.Wood, cost))
cost = expand_cost[Items.Carrot]
carrot.execute(item_halt(Items.Carrot, cost))
unlock_check(Unlocks.Expand)

# Tree 1
tree_cost = get_unlock_cost(Unlocks.Trees)
cost = tree_cost[Items.Carrot]
hay.execute(item_halt(Items.Hay, cost))
cost = tree_cost[Items.Wood] + tree_cost[Items.Carrot] + buffer()
bush.execute(item_halt(Items.Wood, cost))
cost = tree_cost[Items.Carrot]
carrot.execute(item_halt(Items.Carrot, cost))
unlock_check(Unlocks.Trees)

# Watering 1
# Carrots 2
water_cost = get_unlock_cost(Unlocks.Watering)
carrot_cost = get_unlock_cost(Unlocks.Carrots)
cost = water_cost[Items.Wood] + carrot_cost[Items.Wood]
trees_carrots.execute(item_halt(Items.Wood, cost))
unlock_check(Unlocks.Watering)
unlock_check(Unlocks.Carrots)

# Expand 4
expand_cost = get_unlock_cost(Unlocks.Expand)
cost = expand_cost[Items.Wood]
if num_items(Items.Wood) < cost:
	trees_carrots.execute(item_halt(Items.Wood, cost))
unlock_check(Unlocks.Expand)

# Trees 2
tree_cost = get_unlock_cost(Unlocks.Trees)
cost = tree_cost[Items.Hay]
hay.execute(item_halt(Items.Hay, cost))
unlock_check(Unlocks.Trees)

# Speed 4
# Watering 2
# Grass 3
speed_cost = get_unlock_cost(Unlocks.Speed)
cost = speed_cost[Items.Carrot]
hay.execute(item_halt(Items.Hay, cost))
trees_carrots.execute(item_halt(Items.Carrot, cost))
unlock_check(Unlocks.Speed)
unlock_check(Unlocks.Watering)
unlock_check(Unlocks.Grass)

# Carrots 3
carrot_cost = get_unlock_cost(Unlocks.Carrots)
cost = carrot_cost[Items.Wood]
trees_carrots.execute(item_halt(Items.Wood, cost))
unlock_check(Unlocks.Carrots)

# Speed 5
speed_cost = get_unlock_cost(Unlocks.Speed)
cost = speed_cost[Items.Carrot]
trees_carrots.execute(item_halt(Items.Carrot, cost))
unlock_check(Unlocks.Speed)

# Trees 3
# Watering 3
# Fertilizer 1
tree_cost = get_unlock_cost(Unlocks.Trees)
sunflower_cost = get_cost(Unlocks.Sunflowers)
cost = tree_cost[Items.Hay] + sunflower_cost[Items.Carrot]
hay.execute(item_halt(Items.Hay, cost))
unlock_check(Unlocks.Trees)
unlock_check(Unlocks.Watering)
unlock_check(Unlocks.Fertilizer)

# Fertilizer 2
# Watering 4
# Pumpkins 1
fertilizer_cost = get_unlock_cost(Unlocks.Fertilizer)
water_cost = get_unlock_cost(Unlocks.Watering)
pumpkin_cost = get_unlock_cost(Unlocks.Pumpkins)
cost = fertilizer_cost[Items.Wood] + water_cost[Items.Wood] + pumpkin_cost[Items.Wood]
trees_carrots.execute(item_halt(Items.Wood, cost))
unlock_check(Unlocks.Fertilizer)
unlock_check(Unlocks.Watering)
unlock_check(Unlocks.Sunflowers)
unlock_check(Unlocks.Pumpkins)

# Grass 4
grass_cost = get_unlock_cost(Unlocks.Grass)
cost = grass_cost[Items.Wood]
sunflower.execute(exhaust_item(Items.Carrot))
trees_carrots.execute(item_halt(Items.Wood, cost))
unlock_check(Unlocks.Grass)

# Trees 4
# Trees 5
hay.execute(item_halt(Items.Hay, 30000))
unlock_check(Unlocks.Trees)
unlock_check(Unlocks.Trees)

# Carrots 4
carrot_cost = get_unlock_cost(Unlocks.Carrots)
cost = carrot_cost[Items.Wood]
trees_carrots.execute(item_halt(Items.Wood, cost))
unlock_check(Unlocks.Carrots)

# Carrots 5
carrot_cost = get_unlock_cost(Unlocks.Carrots)
cost = carrot_cost[Items.Wood]
trees_carrots.execute(item_halt(Items.Wood, cost + buffer()))
unlock_check(Unlocks.Carrots)

# Watering 5
# Fertilizer 2
# Pumpkins 2
# Pumpkins 3
# Grass 5
trees_carrots.execute(exhaust_item(Items.Hay))
unlock_check(Unlocks.Watering)
unlock_check(Unlocks.Fertilizer)
unlock_check(Unlocks.Pumpkins)
unlock_check(Unlocks.Pumpkins)
unlock_check(Unlocks.Grass)

# Expand 5
expand_cost = get_unlock_cost(Unlocks.Expand)
cost = expand_cost[Items.Pumpkin]
pumpkin.execute(item_halt(Items.Pumpkin, cost))
unlock_check(Unlocks.Expand)

# Expand 6
expand_cost = get_unlock_cost(Unlocks.Expand)
cost = expand_cost[Items.Pumpkin]
pumpkin.execute(item_halt(Items.Pumpkin, cost))
unlock_check(Unlocks.Expand)

# Polyculture 1
# Cactus 1
# Cactus 2
pumpkin.execute(exhaust_item(Items.Carrot))
unlock_check(Unlocks.Polyculture)
unlock_check(Unlocks.Cactus)
unlock_check(Unlocks.Cactus)

# Trees 6
cost = 5000
polyculture.execute(Entities.Grass, item_halt(Items.Hay, cost))
polyculture.execute(Entities.Carrot, item_halt(Items.Carrot, cost))
sunflower.execute(item_halt(Items.Power, cost))
tree_cost = get_unlock_cost(Unlocks.Trees)
cost = tree_cost[Items.Hay]
polyculture.execute(Entities.Grass, item_halt(Items.Hay, cost))
unlock_check(Unlocks.Trees)

# Fertilizer 3
# Watering 6
# Carrots 6
water_cost = get_unlock_cost(Unlocks.Watering)
fertilizer_cost = get_unlock_cost(Unlocks.Fertilizer)
carrot_cost = get_unlock_cost(Unlocks.Carrots)
cost = water_cost[Items.Wood] + fertilizer_cost[Items.Wood] + carrot_cost[Items.Wood]
polyculture.execute(Entities.Tree, item_halt(Items.Wood, cost))
unlock_check(Unlocks.Fertilizer)
unlock_check(Unlocks.Watering)
unlock_check(Unlocks.Carrots)

# Mazes 1
maze_cost = get_unlock_cost(Unlocks.Mazes)
maze_startup_amount = (5 * maze.get_substance_required(get_world_size()))
cost = maze_cost[Items.Weird_Substance] + maze_startup_amount
weird_substance.execute(item_halt(Items.Weird_Substance, cost))
unlock_check(Unlocks.Mazes)

# Megafarm 1
# Megafarm 2
# Megafarm 3
megafarm_cost = get_unlock_cost(Unlocks.Megafarm)
cost = megafarm_cost[Items.Gold] * 21
utils.reset()
maze_reusable.execute(get_world_size(), 300, 0, 0, item_halt(Items.Gold, cost))
unlock_check(Unlocks.Megafarm)
unlock_check(Unlocks.Megafarm)
unlock_check(Unlocks.Megafarm)

# Hats
# Pumpkin 4
expand_cost = get_unlock_cost(Unlocks.Expand)
cost = expand_cost[Items.Pumpkin]
polyculture.execute(Entities.Grass, item_halt(Items.Hay, cost))
polyculture.execute(Entities.Carrot, item_halt(Items.Carrot, cost))
unlock_check(Unlocks.Hats)
unlock_check(Unlocks.Pumpkins)

# Expand 7
pumpkin.execute(item_halt(Items.Pumpkin, cost))
unlock_check(Unlocks.Expand)

# Mazes 2
# Mazes 3
# Mazes 4
# Dinosaurs 1
# Dinosaurs 2
# Dinosaurs 3
# Dinosaurs 4
maze_cost = get_unlock_cost(Unlocks.Mazes)
cost = maze_cost[Items.Cactus] * 2
pumpkin.execute(exhaust_item(Items.Carrot))
cactus_odd_even_sort.execute_half(8, item_halt(Items.Cactus, 1050000))
unlock_check(Unlocks.Mazes)
unlock_check(Unlocks.Mazes)
unlock_check(Unlocks.Mazes)
unlock_check(Unlocks.Dinosaurs)
unlock_check(Unlocks.Dinosaurs)
unlock_check(Unlocks.Dinosaurs)
unlock_check(Unlocks.Dinosaurs)

# Leaderboard
polyculture.execute(Entities.Carrot, item_halt(Items.Carrot, 2000))
sunflower.execute(item_halt(Items.Power, 2000))
polyculture.execute(Entities.Tree, item_halt(Items.Weird_Substance, 175000), True)
utils.reset()
workers = [
	(12, 12, 8),
	(12, 0, 8),
	(0, 12, 8),
	(6, 6, 4),
	(2, 6, 4),
	(6, 2, 4),
	(2, 2, 4)
]
maze_optimised.execute(item_halt(Items.Gold, 1000000), workers)
set_world_size(16)
dinosaur.execute(item_halt(Items.Bone, 2000000))
unlock_check(Unlocks.Leaderboard)
