import game_API 

# General Imports 
import math 

""" 
Utility functions for the AI Bot
""" 

stances = ["Rock", "Paper", "Scissors"]
stance_counters = {"Rock": "Paper", 
					"Paper": "Scissors",
					"Scissors": "Rock",
					"Invalid Stance": "Paper"}

possible_paths = [['Node_1', 'Node_3', 'Node_2', 'Node_3', 'Node_1', 'Node_0'],
					['Node_1', 'Node_3', 'Node_1', 'Node_0'],
					['Node_1', 'Node_3', 'Node_2', 'Node_4', 'Node_2', 'Node_3', 'Node_1', 'Node_0'],
					['Node_1', 'Node_0'],
					['Node_10', 'Node_0'],
					['Node_6', 'Node_0'],
					['Node_10', 'Node_9', 'Node_8', 'Node_9', 'Node_10', 'Node_0'],
					['Node_6', 'Node_7', 'Node_8', 'Node_7', 'Node_6', 'Node_0'],
					['Node_6', 'Node_5', 'Node_4', 'Node_5', 'Node_6', 'Node_0'],
					['Node_6', 'Node_7', 'Node_8', 'Node_9', 'Node_10', 'Node_0'], 
					['Node_1', 'Node_2', 'Node_4', 'Node_5', 'Node_6', 'Node_0'], 
					['Node_6', 'Node_5', 'Node_4', 'Node_2', 'Node_1', 'Node_0'], 
					['Node_10', 'Node_9', 'Node_8', 'Node_7', 'Node_6', 'Node_0'], 
					["Node_1", 'Node_3', "Node_2", "Node_4", "Node_5", "Node_6", "Node_0"]] 
			  
class Path: 
	"""
	A class that represents a path through a sequence of nodes 
	"""
	def __init__(self, nodes, game):
		"""
		Nodes can just be the list of strings from the cycles global variable 
		"""
		self.path = []
		self.path_indices = [] 
		for node in nodes: 
			self.path.append(game.nodes[int(node[node.index("_") + 1:])]) # Assuming that the list of nodes in the game variable is in order. It should be, based on how the API generates it...
			self.path_indices.append(int(node[node.index("_") + 1:]))

		self.length = len(nodes) 
		self.current_node = 0 

	def get_next_node(self):
		if self.current_node + 1 < self.total_num_nodes:
			return self.path[self.current_node + 1]
		else:
			return None

	def move_next_node(self):
		self.current_node += 1

	def __getitem__(self, key): 
		return self.path_indices[key]

	def __str__(self):
		ret = "" 
		for node in self.path_indices: 
			ret += "Node "
			ret += str(node)
			ret += ", "
		return ret

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
		if other == None: 
			return False
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

	def evaluate_path_score(self, game):
		"""
		Allows us to rank this path based on current board conditions 
		This is hard
		"""
		def weight_cal(monster, attack, speed, p_time, game):
			hpl = hp_loss(monster, attack, speed)
			R_gain, P_gain, S_gain, Spd_gain = gain(monster, attack, speed, game)
			time = time_spend(monster, attack, speed)

			score = (-.4) * hpl + 8 * (R_gain + P_gain + S_gain) + 100 * Spd_gain + (-.25) * time + p_time
			# game.log(str(Spd_gain))
			return score


		def time_spend(monster, attack, speed):
			# attack value is the corresponding resources you have
			move_time = 7 - speed
			kill_time = monster.health / attack

			if move_time <= kill_time:
				time = move_time
			else:
				time = kill_time
			return time

		def hp_loss(monster, attack, speed):
			time = time_spend(monster, attack, speed)
			hp_loss = monster.attack * time

			return hp_loss

		def gain(monster, attack, speed, game):
			move_time = 7 - speed
			kill_time = monster.health / attack

			if move_time < kill_time:
				R_gain = 0
				P_gain = 0
				S_gain = 0
				Spd_gain = 0
			else:
				R_gain = monster.death_effects.rock
				P_gain = monster.death_effects.paper
				S_gain = monster.death_effects.scissors
				Spd_gain = monster.death_effects.speed
				#game.log("{0}, {1}, {2}, {3}, {4}".format(monster.name, R_gain, P_gain, S_gain, Spd_gain))

			return R_gain, P_gain, S_gain, Spd_gain




		#game.log("\n")
		non_count = 0
		my_monsters = []
		for node in self.path_indices:
			monster = game.get_monster(node)
			if monster.name != "No Monster" and not monster.dead: 
				my_monsters.append(monster)
				# game.log("Node {}: {}".format(node, monster.name))
			elif monster.name == 'No Monster' or monster.dead:
				non_count +=1

		p_time = non_count * (-5)

		player = game.get_self()

		weight_sum = 0

		for monster in my_monsters:
			stance = stance_counters[monster.stance]
			if stance == 'Rock':
				attack = player.rock
			elif stance == 'Paper':
				attack = player.paper
			elif stance == 'Scissors':
				attack = player.scissors

			speed = player.speed

			num_R = player.rock
			num_P = player.paper
			num_S = player.scissors

			if (10.3 / num_R) <= (7 - speed):
				if monster.name == 'Paper 3':
					weight_sum +=10
				elif monster.name == 'Scissors 21':
					weight_sum +=20
			elif (7 / num_P) <= (7 - speed):
				if monster.name == 'Paper 3':
					weight_sum += 10
				elif monster.name == 'Scissors 21':
					weight_sum += 20
			elif (12 / num_S) <= (7 - speed):
				if monster.name == 'Paper 3':
					weight_sum += 10
				elif monster.name == 'Scissors 21':
					weight_sum += 20

			val = weight_cal(monster, attack, speed, p_time, game)
			weight_sum = weight_sum + val
		return weight_sum


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