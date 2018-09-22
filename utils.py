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

cycles = [['Node_6', 'Node_7', 'Node_8', 'Node_9', 'Node_10', 'Node_0'], 
		  ['Node_1', 'Node_2', 'Node_4', 'Node_5', 'Node_6', 'Node_0'], 
		  ['Node_6', 'Node_5', 'Node_4', 'Node_2', 'Node_1', 'Node_0'], 
		  ['Node_10', 'Node_9', 'Node_8', 'Node_7', 'Node_6', 'Node_0'], 
		  ["Node_1", 'Node_3', "Node_2", "Node_4", "Node_5", "Node_6", "Node_0"],
		  ['Node_6', 'Node_5', 'Node_4', 'Node_13', 'Node_12', 'Node_11', 'Node_10', 'Node_0'], 
		  ['Node_1', 'Node_2', 'Node_4', 'Node_13', 'Node_12', 'Node_11', 'Node_10', 'Node_0'], 
		  ['Node_10', 'Node_11', 'Node_12', 'Node_13', 'Node_4', 'Node_5', 'Node_6', 'Node_0'], 
		  ['Node_10', 'Node_11', 'Node_12', 'Node_13', 'Node_4', 'Node_2', 'Node_1', 'Node_0'], 
		  ['Node_1', 'Node_3', 'Node_2', 'Node_4', 'Node_13', 'Node_12', 'Node_11', 'Node_10', 'Node_0'], 
		  ['Node_6', 'Node_5', 'Node_4', 'Node_13', 'Node_14', 'Node_8', 'Node_9', 'Node_10', 'Node_0'], 
		  ['Node_1', 'Node_2', 'Node_4', 'Node_13', 'Node_14', 'Node_8', 'Node_9', 'Node_10', 'Node_0'], 
		  ['Node_1', 'Node_2', 'Node_4', 'Node_13', 'Node_14', 'Node_8', 'Node_7', 'Node_6', 'Node_0'], 
		  ['Node_10', 'Node_9', 'Node_8', 'Node_14', 'Node_13', 'Node_4', 'Node_5', 'Node_6', 'Node_0'], 
		  ['Node_10', 'Node_9', 'Node_8', 'Node_14', 'Node_13', 'Node_4', 'Node_2', 'Node_1', 'Node_0'],
		  ['Node_6', 'Node_7', 'Node_8', 'Node_14', 'Node_13', 'Node_4', 'Node_2', 'Node_1', 'Node_0'], 
		  ['Node_10', 'Node_16', 'Node_12', 'Node_13', 'Node_4', 'Node_2', 'Node_3', 'Node_1', 'Node_0']
		  ['Node_6', 'Node_7', 'Node_8', 'Node_14', 'Node_13', 'Node_12', 'Node_11', 'Node_10', 'Node_0'], 
		  ['Node_1', 'Node_3', 'Node_2', 'Node_4', 'Node_13', 'Node_12', 'Node_16', 'Node_10', 'Node_0'],
		  ['Node_10', 'Node_11', 'Node_12', 'Node_13', 'Node_14', 'Node_8', 'Node_7', 'Node_6', 'Node_0'], 
		  ['Node_1', 'Node_3', 'Node_2', 'Node_4', 'Node_13', 'Node_14', 'Node_8', 'Node_9', 'Node_10', 'Node_0'], 
		  ['Node_1', 'Node_3', 'Node_2', 'Node_4', 'Node_13', 'Node_14', 'Node_8', 'Node_7', 'Node_6', 'Node_0'], 
		  ['Node_10', 'Node_16', 'Node_12', 'Node_22', 'Node_19', 'Node_20', 'Node_13', 'Node_4', 'Node_5', 'Node_6', 'Node_0'], 
		  ['Node_10', 'Node_16', 'Node_12', 'Node_22', 'Node_19', 'Node_20', 'Node_13', 'Node_4', 'Node_2', 'Node_1', 'Node_0'], 
		  ['Node_6', 'Node_5', 'Node_4', 'Node_13', 'Node_20', 'Node_21', 'Node_22', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_1', 'Node_2', 'Node_4', 'Node_13', 'Node_20', 'Node_21', 'Node_22', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_6', 'Node_7', 'Node_8', 'Node_14', 'Node_19', 'Node_20', 'Node_13', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_6', 'Node_5', 'Node_4', 'Node_13', 'Node_20', 'Node_19', 'Node_22', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_1', 'Node_2', 'Node_4', 'Node_13', 'Node_20', 'Node_19', 'Node_22', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_6', 'Node_5', 'Node_4', 'Node_13', 'Node_12', 'Node_16', 'Node_10', 'Node_0', 'Node_10', 'Node_0', 'Node_10'], 
		  ['Node_10', 'Node_16', 'Node_12', 'Node_22', 'Node_21', 'Node_20', 'Node_13', 'Node_4', 'Node_5', 'Node_6', 'Node_0'], 
		  ['Node_10', 'Node_16', 'Node_12', 'Node_22', 'Node_21', 'Node_20', 'Node_13', 'Node_4', 'Node_2', 'Node_1', 'Node_0'], 
		  ['Node_10', 'Node_16', 'Node_12', 'Node_13', 'Node_20', 'Node_19', 'Node_14', 'Node_8', 'Node_7', 'Node_6', 'Node_0'], 
		  ['Node_1', 'Node_3', 'Node_2', 'Node_4', 'Node_13', 'Node_20', 'Node_21', 'Node_22', 'Node_12', 'Node_16', 'Node_10', 'Node_0'],
		  ['Node_1', 'Node_3', 'Node_2', 'Node_4', 'Node_13', 'Node_20', 'Node_19', 'Node_22', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_6', 'Node_5', 'Node_4', 'Node_13', 'Node_12', 'Node_16', 'Node_17', 'Node_18', 'Node_15', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_1', 'Node_2', 'Node_4', 'Node_13', 'Node_12', 'Node_16', 'Node_17', 'Node_18', 'Node_15', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_6', 'Node_7', 'Node_8', 'Node_14', 'Node_13', 'Node_20', 'Node_21', 'Node_22', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_6', 'Node_5', 'Node_4', 'Node_13', 'Node_20', 'Node_19', 'Node_14', 'Node_13', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_1', 'Node_2', 'Node_4', 'Node_13', 'Node_20', 'Node_19', 'Node_14', 'Node_13', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_6', 'Node_7', 'Node_8', 'Node_14', 'Node_13', 'Node_20', 'Node_19', 'Node_22', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_6', 'Node_7', 'Node_8', 'Node_14', 'Node_13', 'Node_12', 'Node_16', 'Node_10', 'Node_0', 'Node_10', 'Node_0', 'Node_10'],
		  ['Node_10', 'Node_16', 'Node_15', 'Node_18', 'Node_17', 'Node_16', 'Node_12', 'Node_13', 'Node_4', 'Node_5', 'Node_6', 'Node_0'], 
		  ['Node_10', 'Node_16', 'Node_15', 'Node_18', 'Node_17', 'Node_16', 'Node_12', 'Node_13', 'Node_4', 'Node_2', 'Node_1', 'Node_0'], 
		  ['Node_10', 'Node_16', 'Node_12', 'Node_22', 'Node_21', 'Node_20', 'Node_13', 'Node_14', 'Node_8', 'Node_7', 'Node_6', 'Node_0'], 
		  ['Node_10', 'Node_16', 'Node_12', 'Node_13', 'Node_14', 'Node_19', 'Node_20', 'Node_13', 'Node_4', 'Node_5', 'Node_6', 'Node_0'], 
		  ['Node_10', 'Node_16', 'Node_12', 'Node_13', 'Node_14', 'Node_19', 'Node_20', 'Node_13', 'Node_4', 'Node_2', 'Node_1', 'Node_0'], 
		  ['Node_10', 'Node_16', 'Node_12', 'Node_22', 'Node_19', 'Node_20', 'Node_13', 'Node_14', 'Node_8', 'Node_7', 'Node_6', 'Node_0'],  
		  ['Node_1', 'Node_3', 'Node_2', 'Node_4', 'Node_13', 'Node_12', 'Node_16', 'Node_17', 'Node_18', 'Node_15', 'Node_16', 'Node_10', 'Node_0'],
 		  ['Node_1', 'Node_3', 'Node_2', 'Node_4', 'Node_13', 'Node_20', 'Node_19', 'Node_14', 'Node_13', 'Node_12', 'Node_16', 'Node_10', 'Node_0'], 
		  ['Node_6', 'Node_7', 'Node_8', 'Node_14', 'Node_13', 'Node_12', 'Node_16', 'Node_17', 'Node_18', 'Node_15', 'Node_16', 'Node_10', 'Node_0'],
		  ['Node_10', 'Node_16', 'Node_15', 'Node_18', 'Node_17', 'Node_16', 'Node_12', 'Node_13', 'Node_14', 'Node_8', 'Node_7', 'Node_6', 'Node_0']] 
		  
class Path: 
	"""
	A class that represents a path through a sequence of nodes 
	"""
	def __init__(self, nodes, game):
		"""
		Nodes can just be the list of strings from the cycles global variable 
		"""
		self.path = [] 
		for node in nodes: 
			path.append(game.nodes[int(node[node.index("_") + 1:])]) # Assuming that the list of nodes in the game variable is in order. It should be, based on how the API generates it...

		self.total_num_nodes = len(nodes) # Might want to do len(nodes) - 1 to exclude Node_0
		self.current_node = 0 

	def get_next_node(self):
		if self.current_node + 1 < self.total_num_nodes:
			return self.path[self.current_node + 1]
		else:
			return None

	def move_next_node(self):
		self.current_node += 1

	""" 
	Overloading comparison operators
	"""
	def __lt__(self, other):
		ps_self = self.evaluate_path_score()
		ps_other = other.evaluate_path_score()
		if ps_self < ps_other: 
			return True 
		else: 
			return False

	def __le__(self, other): 
		ps_self = self.evaluate_path_score()
		ps_other = other.evaluate_path_score()
		if ps_self <= ps_other: 
			return True 
		else: 
			return False

	def __gt__(self, other):
		ps_self = self.evaluate_path_score()
		ps_other = other.evaluate_path_score()
		if ps_self > ps_other: 
			return True 
		else: 
			return False

	def __ge__(self, other): 
		ps_self = self.evaluate_path_score()
		ps_other = other.evaluate_path_score()
		if ps_self >= ps_other: 
			return True 
		else: 
			return False

	def __eq__(self, other):
		ps_self = self.evaluate_path_score()
		ps_other = other.evaluate_path_score()
		if ps_self == ps_other: 
			return True 
		else: 
			return False		

	def __ne__(self, other): 
		ps_self = self.evaluate_path_score()
		ps_other = other.evaluate_path_score()
		if ps_self != ps_other: 
			return True 
		else: 
			return False		

	def evaluate_path_score(self): 
		"""
		Allows us to rank this path based on current board conditions 
		This is hard
		"""
		pass 


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