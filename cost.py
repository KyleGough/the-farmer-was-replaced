import math

def ceil(n):
	return -(-n // 1)

# Amount harvested for a single entity.
def harvest_amount(unlock):
	return 2 ** (num_unlocked(unlock) - 1)
	
# Number of harvests required to reach a certain quantity.
def harvests_required(n, unlock):
	return math.ceil(n / harvest_amount(unlock))

# Number of whole farm scans needed to reach a certain quantity.
def whole_farms_required(n, unlock):
	h = harvests_required(n, unlock)
	tiles = get_world_size() ** 2
	return math.ceil(h / tiles)	
	
	