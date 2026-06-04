import utils
import movement
import maze_reusable

start = num_items(Items.Gold)
required = start + 9863168 

def t(x, y, size, halt):
	movement.goto(x, y)
	utils.sleep(12 * (500 - x - y))
	maze_reusable.execute(size, 300, x, y, halt)

def execute(halt):
	utils.reset()
	
	for i in range(4):
		for j in range(4):
			if (i == 0 and j < 3) or (j == 0 and i < 3):
				continue
			spawn_drone(t, (i * 8) + 4, (j * 8) + 4, 8, halt)
	for i in range(1, -1, -1):
		for j in range(5, 1, -1):
			spawn_drone(t, (i * 4) + 2, (j * 4) + 2, 4, halt)	
	for i in range(5, -1, -1):
		for j in range(1, -1, -1):
			spawn_drone(t, (i * 4) + 2, (j * 4) + 2, 4, halt)		
	while not halt():
		do_a_flip()
	
def leaderboard_halt():
	return num_items(Items.Gold) >= required

if __name__ == "__main__":
	execute(leaderboard_halt)