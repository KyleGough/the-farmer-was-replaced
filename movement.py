def move_direction(direction, n):
	for _ in range(n):
		move(direction)

def get_positive_dist(x, x0):
	if x > x0:
		return x - x0
	else:
		return get_world_size() - x0 + x
		
def get_negative_dist(x, x0):
	if x < x0:
		return x0 - x
	else:
		return x0 + get_world_size() - x

def goto_x(x):
	x0 = get_pos_x()	

	if x == x0:
		return 

	size = get_world_size()
	
	east_len = get_positive_dist(x, x0)
	west_len = get_negative_dist(x, x0)
	
	if (west_len < east_len):
		move_direction(West, west_len)
	else:
		move_direction(East, east_len)
	
def goto_y(y):
	y0 = get_pos_y()
	
	if y == y0:
		return
		
	size = get_world_size()
	
	north_len = get_positive_dist(y, y0)
	south_len = get_negative_dist(y, y0)
	
	if (south_len < north_len):
		move_direction(South, south_len)
	else:
		move_direction(North, north_len)
		
def goto(x, y):
	goto_x(x)
	goto_y(y)
	