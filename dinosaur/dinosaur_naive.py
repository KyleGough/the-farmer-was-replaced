# This is a very naive implementation of snake.
# The drone moves in a repeating pattern that does not take into account the position of the apples.

from utils import never_halt,reset

def naive_loop(size):
	horizontal = [East, West]

	move(East)
	for i in range(size - 1):
		horizontal_direction = horizontal[i % 2]
		for _ in range(size - 2):
			move(horizontal_direction)
		move(South)
	for _ in range(size - 1):
		move(West)
	for _ in range(size - 1):
		move(North)

def execute(halt):
	size = get_world_size()

	while not halt():
		reset()
		change_hat(Hats.Dinosaur_Hat)
		while can_move(East):
			naive_loop(size)
		change_hat(Hats.Green_Hat)

if __name__ == "__main__":
	execute(never_halt)
