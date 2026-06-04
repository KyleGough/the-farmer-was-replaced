import utils
import movement
import maze

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
			
def follow_route(graph, route):
	while len(route):		
		current = route.pop()
		move(current)
		x = get_pos_x()
		y = get_pos_y()
		for dir in maze.directions:
			if can_move(dir):
				(ax, ay) = maze.adjacency_relation[dir]
				nx = x + ax
				ny = y + ay
				graph[(x, y)].add(((nx, ny), dir))
		
def execute(size, iterations, x, y, halt):
	while not halt():
		amount = maze.get_substance_required(size)
		maze.init_maze(amount)
		graph = maze.build_graph(size)
		
		for _ in range(iterations + 1):
			if halt():
				return
			previous = flood_fill(graph)
			route = get_route(previous)
			follow_route(graph, route)
			maze.restart_maze(amount)
		harvest()
		movement.goto(x, y)
	
if __name__ == "__main__":
	utils.reset()
	execute(32, 300)