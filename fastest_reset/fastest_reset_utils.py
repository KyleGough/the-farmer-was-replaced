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

def wait_harvest():
	while not can_harvest():
		continue
	harvest()

def toil():
	if get_ground_type() == Grounds.Grassland:
		till()
