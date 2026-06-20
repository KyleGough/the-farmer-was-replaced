from utils import reset
import maze

directionNum = {
	North: 0,
	East: 1,
	South: 2,
	West: 3
}

reverseDirectionNum = {
	East: 0,
	North: 1,
	West: 2,
	South: 3
}

directions = [West, North, East, South]
reverseDirections = [South, East, North, West]

# Traverses the maze hugging the left wall.
def traverse(directions, directionNum):
	lastDirection = East
	while True:
		if maze.check_treasure():
			return
		for i in range(4):
			nextIndex = (i + directionNum[lastDirection]) % 4
			nextDirection = directions[nextIndex]

			if move(nextDirection):
				lastDirection = nextDirection
				break

def solve_maze(amount):
	reset()
	maze.init_maze(amount)
	if max_drones() > 1:
		# Spawn a second drone that hugs the right wall.
		spawn_drone(traverse, reverseDirections, reverseDirectionNum)
	traverse(directions, directionNum)

if __name__ == "__main__":
	amount = maze.get_substance_required(get_world_size())
	while True:
		solve_maze(amount)
