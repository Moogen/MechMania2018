# keep these three import statements
import game_API
import fileinput
import json

# your import statements here
import random
import utils

stances = ["Rock", "Paper", "Scissors"]

first_line = True # DO NOT REMOVE
first_node = True # Used for decision making on the first node 
turn_counter = 0 


def duel(): 
    pass 

# main player script logic
# DO NOT CHANGE BELOW ----------------------------
for line in fileinput.input():
    if first_line:
        game = game_API.Game(json.loads(line))
        first_line = False
        continue
    game.update(json.loads(line))
# DO NOT CHANGE ABOVE ---------------------------

    # code in this block will be executed each turn of the game

    me = game.get_self()
    opponent = game.get_opponent()

    turn_counter += 1

    # submit your decision for the turn (This function should be called exactly once per turn)
    game.submit_decision(destination_node, chosen_stance)

    if turn_counter > 300: 
        duel() 



""" 
    if me.location == me.destination: # check if we have moved this turn
        # get all living monsters closest to me
        monsters = game.nearest_monsters(me.location, 1)

        # choose a monster to move to at random
        monster_to_move_to = monsters[random.randint(0, len(monsters)-1)]

        # get the set of shortest paths to that monster
        paths = game.shortest_paths(me.location, monster_to_move_to.location)
        destination_node = paths[random.randint(0, len(paths)-1)][0]
    else:
        destination_node = me.destination

    if game.has_monster(me.location):
        # if there's a monster at my location, choose the stance that damages that monster
        chosen_stance = get_winning_stance(game.get_monster(me.location).stance)
    else:
        # otherwise, pick a random stance
        chosen_stance = stances[random.randint(0, 2)]
"""