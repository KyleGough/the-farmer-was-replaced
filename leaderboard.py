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
	Leaderboards.Hay_Single: "hay_single",
	Leaderboards.Maze_Single: "maze_reusable",
	Leaderboards.Dinosaur: "dinosaur_simple",
	Leaderboards.Carrots_Single: "carrot_single",
	Leaderboards.Wood_Single: "wood_single",
	Leaderboards.Sunflowers_Single: "sunflower_single",
	Leaderboards.Cactus_Single: "cactus_single"
}

def run(leaderboard):
	leaderboard_run(leaderboard, filename[leaderboard], 1000)

if __name__ == "__main__":
	run(Leaderboards.Fastest_Reset)
