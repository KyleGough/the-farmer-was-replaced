from utils import never_halt
from movement import goto

start = num_items(Items.Bone)
required = start + 33488928

# Fraction of length to total grid area for the strategy
# to switch to a full circuit.
full_circuit_threshold = 0.40

def leaderboard_halt():
	return num_items(Items.Bone) >= required

# Update length and apple position if apple present.
def maybe_apple(apple, length):
	m = measure()
	if m:
		return m, length + 1
	else:
		return apple, length

# Returns the number of bands to force explore due to tail length.
def range_bucket(x, size):
	step = (size * 2) - 4
	if x <= size:
		return 0
	if x >= (size ** 2) * full_circuit_threshold:
		return 1000
	return (x - size - 1) // step + 1

def top_half(apple, length, radius):
	size = get_world_size()
	ax, ay = apple

	# Bands to force explore due to tail length.
	force_bands = range_bucket(length, size)

	# If apple is not present, skip top half.
	if ay < radius and force_bands == 0:
		for _ in range(size - 1):
			move(East)
		return apple, length

	# Iterate over each band.
	for band in range(radius):
		ax, ay = apple
		band_x = 2 * (ax // 2)
		# Explore, if apple contained in the current band.
		apple_in_band = band_x == get_pos_x() and ay >= radius
		if apple_in_band or band < force_bands:
			if apple_in_band and band >= force_bands:
				branch_length = ay - radius
			else:
				branch_length = radius - 1
			apple, length = maybe_apple(apple, length)
			for _ in range(branch_length):
				move(North)
				apple, length = maybe_apple(apple, length)
			move(East)
			apple, length = maybe_apple(apple, length)
			for _ in range(branch_length):
				move(South)
				apple, length = maybe_apple(apple, length)
		else:
			move(East)
		move(East)

	return apple, length

def bottom_half(apple, length, radius):
	size = get_world_size()
	ax, ay = apple

	# Bands to force explore due to tail length.
	force_bands = range_bucket(length, size)

	# If apple is not present, skip bottom half.
	if ay >= radius and force_bands == 0:
		for _ in range(size - 1):
			move(West)
		return apple, length

	# Iterate over each band.
	for band in range(radius):
		ax, ay = apple
		band_x = (2 * (ax // 2)) + 1
		# Explore, if apple contained in the current band.
		apple_in_band = band_x == get_pos_x() and ay < radius
		if apple_in_band or band < force_bands:
			if apple_in_band and band >= force_bands:
				branch_length = radius - 1 - ay
			else:
				branch_length = radius - 1
			apple, length = maybe_apple(apple, length)
			for _ in range(branch_length):
				move(South)
				apple, length = maybe_apple(apple, length)
			move(West)
			apple, length = maybe_apple(apple, length)
			for _ in range(branch_length):
				move(North)
				apple, length = maybe_apple(apple, length)
		else:
			move(West)
		move(West)

	return apple, length

def execute(halt):
	size = get_world_size()
	radius = size / 2

	while not halt():
		goto(0, radius)
		change_hat(Hats.Dinosaur_Hat)
		apple = measure()
		harvest()
		length = 1
		while length < size * size - 1:
			apple, length = top_half(apple, length, radius)
			move(South)
			apple, length = bottom_half(apple, length, radius)
			move(North)
		change_hat(Hats.Brown_Hat)

if __name__ == "__main__":
	set_world_size(32)
	execute(leaderboard_halt)
