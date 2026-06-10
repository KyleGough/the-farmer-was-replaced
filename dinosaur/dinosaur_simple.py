import utils
from movement import goto, goto_x, goto_y


start = num_items(Items.Bone)
required = start + 33488928

def leaderboard_halt():
	return num_items(Items.Bone) >= required

length_threshold = 44

# Update length and apple position if apple present.
def maybe_apple(apple, length):
	m = measure()
	if m:
		return m, length + 1
	else:
		return apple, length

def top_half(apple, length, radius):
	size = get_world_size()
	ax, ay = apple

	# If apple is not present, skip top half.
	if ay < radius:
		for _ in range(size - 1):
			move(East)
		return apple, length

	# Bands to force explore due to tail length.
	force_bands = max((length - size - size) // size, 0)

	# Iterate over each band.
	for band in range(radius):
		ax, ay = apple
		band_x = 2 * (ax // 2)
		# Explore, if apple contained in the current band.
		if (band_x == get_pos_x() and ay >= radius) or band < force_bands:
			apple, length = maybe_apple(apple, length)
			for _ in range(radius - 1):
				move(North)
				apple, length = maybe_apple(apple, length)
			move(East)
			apple, length = maybe_apple(apple, length)
			for _ in range(radius - 1):
				move(South)
				apple, length = maybe_apple(apple, length)
		else:
			move(East)
		move(East)

	return apple, length

def bottom_half(apple, length, radius):
	size = get_world_size()
	ax, ay = apple

	# If apple is not present, skip bottom half.
	if ay < radius or length > length_threshold:
		for _ in range(radius):
			ax, ay = apple
			x = 2 * (ax // 2) + 1
			# Explore, if apple contained in the current band.
			if (x == get_pos_x() and ay < radius) or length > length_threshold:
				apple, length = maybe_apple(apple, length)
				for _ in range(radius - 1):
					move(South)
					apple, length = maybe_apple(apple, length)
				move(West)
				apple, length = maybe_apple(apple, length)
				for _ in range(radius - 1):
					move(North)
					apple, length = maybe_apple(apple, length)
			else:
				move(West)
			move(West)
	else:
		for _ in range(size - 1):
			move(West)
	return apple, length

def execute(halt):
	set_world_size(16)
	size = get_world_size()
	radius = size / 2

	while not halt():
		goto_y(size / 2)
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
	execute(utils.never_halt)
