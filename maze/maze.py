directionNum = {
	North: 0,
	East: 1,
	South: 2,
	West: 3
}

directions = [West, North, East, South]

adjacency_relation = {
	North: (0, 1),
	East: (1, 0),
	South: (0, -1),
	West: (-1, 0)
}

def get_substance_required(size):
	return size * 2 ** (num_unlocked(Unlocks.Mazes) - 1)

def init_maze(amount):
	if num_items(Items.Weird_Substance) < amount:
		quick_print("Requires", amount)
		return False
	plant(Entities.Bush)
	restart_maze(amount)
	return True

def restart_maze(amount):
	if not use_item(Items.Weird_Substance, amount):
		harvest()

def check_treasure():
	e = get_entity_type()
	if e == Entities.Treasure or e == Entities.Grass:
		harvest()
		return True

def add_adjacency(graph):
	x = get_pos_x()
	y = get_pos_y()

	for dir in directions:
		if can_move(dir):
			if (x, y) not in graph:
				graph[(x, y)] = set()
			(nx, ny) = adjacency_relation[dir]
			graph[(x, y)].add(((x + nx, y + ny), dir))

# Traverses the maze hugging the left wall.
def build_graph(size):
	graph = {}
	lastDirection = East
	tiles = size ** 2

	while len(graph) < tiles:
		add_adjacency(graph)
		for i in range(4):
			nextIndex = (i + directionNum[lastDirection]) % 4
			nextDirection = directions[nextIndex]

			if move(nextDirection):
				lastDirection = nextDirection
				break

	return graph
