from movement import goto
import maze
import stack

start = num_items(Items.Gold)
required = start + 616448

def leaderboard_halt():
	return num_items(Items.Gold) >= required

def flood_fill(graph):
	treasure = measure()
	visited = set()
	start = (get_pos_x(), get_pos_y())
	frontier = { start: None }
	next_frontier = {}
	previous = {}

	while frontier:
		next_frontier = {}
		for pos in frontier:
			for (neighbour, direction) in graph[pos]:
				if neighbour not in visited:
					previous[neighbour] = (pos, direction)
					if neighbour == treasure:
						return previous, treasure
					next_frontier[neighbour] = pos
					visited.add(pos)
		frontier = next_frontier

	return previous, treasure

# Gets a route from treasure to current position.
def get_route(previous, treasure):
	pos = treasure
	route = None

	while pos in previous:
		pos, dir = previous[pos]
		route = stack.push(route, dir)

	return route

def follow_route(graph, route, i):
	# Heuristic to detect shortcuts every 3 passes.
	# Reduces run-time about 6 seconds.
	search_shortcut = i % 3 == 1

	while route:
		move(stack.peek(route))
		route = stack.pop(route)

		if search_shortcut:
			x = get_pos_x()
			y = get_pos_y()
			for dir in maze.directions:
				if can_move(dir):
					ax, ay = maze.adjacency_relation[dir]
					nx = x + ax
					ny = y + ay
					graph[(x, y)].add(((nx, ny), dir))

def execute(size, iterations, x, y, halt):
	while not halt():
		amount = maze.get_substance_required(size)
		maze.init_maze(amount)
		graph = maze.build_graph(size)

		for i in range(iterations):
			if halt():
				break
			if i > 0:
				maze.restart_maze(amount)
			previous, treasure = flood_fill(graph)
			route = get_route(previous, treasure)
			follow_route(graph, route, i)
		harvest()
		goto(x, y)

if __name__ == "__main__":
	execute(8, 300, 0, 0, leaderboard_halt)
