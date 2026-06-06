# This is a very naive implementation of snake.
# The drone moves in a repeating pattern that does not take into account the position of the apples.
# Implementing a proper algorithm here would reduce the fastest reset time dramatically.

import utils

def init():
	utils.reset()
	change_hat(Hats.Dinosaur_Hat)
	return measure()
	
def simple_loop():
	size = get_world_size()
	horizontal = [East, West]
	
	move(East)	
	for i in range(size - 1):
		horizontal_direction = horizontal[i % 2]
		for j in range(size - 2):
			move(horizontal_direction)
		move(South)
	for i in range(size - 1):
		move(West)
	for i in range(size - 1):
		move(North)
	
if __name__ == "__main__":
	while True:
#		set_world_size(16)
		pos = init()
		while can_move(East):
			simple_loop()	
		change_hat(Hats.Brown_Hat)
	