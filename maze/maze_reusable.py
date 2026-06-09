import utils
import movement
import maze

start = num_items(Items.Gold)
required = start + 616448

def leaderboard_halt():
	return num_items(Items.Gold) >= required

def flood_fill(graph):
	t = measure()
	visited = set()
	start = (get_pos_x(), get_pos_y())
	frontier = { start: None }
	next_frontier = {}
	found_treasure = False
	previous = {}

	while not found_treasure:
		next_frontier = {}
		for pos in frontier:
			if pos == t:
				found_treasure = True
				break

			for (n, d) in graph[pos]:
				if n not in visited:
					next_frontier[n] = pos
					previous[n] = (pos, d)
					visited.add(pos)
		frontier = next_frontier

	return previous

# Gets a route from treasure to current position.
def get_route(previous):
	pos = measure()
	route = []

	while pos in previous:
		pos, dir = previous[pos]
		route.append(dir)

	return route

def follow_route(graph, route, i):
	# Heuristic to detect shortcuts every 4 passes.
	# Reduces run-time about 6 seconds.
	search_shortcut = i % 3 == 1

	while len(route):
		move(route.pop())
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
			previous = flood_fill(graph)
			route = get_route(previous)
			follow_route(graph, route, i)
		harvest()
		movement.goto(x, y)

if __name__ == "__main__":
	execute(8, 300, 0, 0, leaderboard_halt)
