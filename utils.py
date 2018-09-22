import game_API 

# General Imports 
import math 

""" 
Utility functions for the AI Bot
""" 

stances = ["Rock", "Paper", "Scissors"]
stance_counters = {"Rock": "Paper", 
					"Paper": "Scissors",
					"Scissors", "Rock"}

def get_player_strength(player, stance): 
	"""
	Returns the stat value associated with a certain stance. Can be used for either player. 
	"""
	if stance == "Rock": 
		return player.rock
	elif stance == "Paper": 
		return player.paper
	elif stance == "Scissors": 
		return player.scissors

def calc_num_turns_to_kill_monster(player, monster):
	""" 
	Calculates how many turns it would take to kill a specific monster. Useful for either player.

	Input player should be of type Player 
	Input monster should be of type Monster
	""" 
	monster_hp = monster.health
	monster_stance = monster.stance
	player_strength = get_player_strength(player, stance_counters[monster_stance])
	return math.ceil(monster_hp / player_strength) # Round up on the number of turns needed 