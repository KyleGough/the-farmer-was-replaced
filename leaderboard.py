filename = {
	Leaderboards.Hay: "hay_polyculture",
	Leaderboards.Wood: "tree_polyculture",
	Leaderboards.Carrots: "carrot_polyculture",
	Leaderboards.Cactus: "cactus_odd_even_sort",
	Leaderboards.Pumpkins: "pumpkin_optimised",
	Leaderboards.Pumpkins_Single: "single_pumpkin",
	Leaderboards.Sunflowers: "sunflower",
	Leaderboards.Maze: "maze_optimised",
	Leaderboards.Fastest_Reset: "fastest_reset",
	Leaderboards.Hay_Single: "hay_single"
}

def run(leaderboard):
	leaderboard_run(leaderboard, filename[leaderboard], 1000)
  
if __name__ == "__main__":
	run(Leaderboards.Fastest_Reset)
  
  
  