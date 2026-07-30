from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import get_option_value, clamp, get_items_with_value, is_option_enabled 
from BaseClasses import MultiWorld, CollectionState

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
def anyClassLevel(state: CollectionState, player: int, level: str):
    """Has the player reached the given level in any class?"""
    for item in ["Figher Level", "Black Belt Level", "Thief Level", "Red Mage Level", "White Mage Level", "Black Mage Level"]:
        if state.count(item, player) >= int(level):
            return True
    return False

def blossomFragmentReq(world: World, state: CollectionState, player: int):
    """Has the player reached the required number of Blossom Fragments"""
    required_fragments = get_option_value(world.multiworld, player, "blossom_fragments_required")
    return state.has("FRAGMENT OF BLOSSOM", player, required_fragments)

def rootsReq(world: World, state: CollectionState, player: int):
    """Does the player have the roots option enabled?"""

    #If the setting is on, roots are not neeeded to goal, disable the logic for them.
    if not is_option_enabled(world.multiworld, player, "randomize roots"):
        return True
    
    class_to_root = {
            "Diver Class": "ROOTS IN VERSATILITY",
            "Charger Class": "ROOTS IN PERSISTENCE",
            "Grappler Class": "ROOTS IN TRUST",
            "Spirit Class": "ROOTS IN SELF-AWARENESS",
            "Glider Class": "ROOTS IN BRAVERY",
            "Wanted Class": "ROOTS IN DEFIANCE",
            "Prisoner Class": "ROOTS IN CERTAINTY"
        }
    #Check if the player has any of the class items and their corresponding root items
    for class_item, root_item in class_to_root.items():
        if state.has(class_item, player) and state.has(root_item, player):
            return True

    return False

#def ungateGoalReq(world: World, state: CollectionState, player: int):
#    """Changes the logic for the Ungate Levels Required based on the goal selected by the player"""
#    goal_type = world.goal[player].value
#    if goal_type == 1:  # Reach Level 10
#       return state.has("Progressive Ungate Levels", player, 1)
#   elif goal_type == 2:  # Reach Level 15
#        return state.has("Progressive Ungate Levels", player, 2)
#    elif goal_type == 3:  # Reach Level 20
#       return state.has("Progressive Ungate Levels", player, 3)
#    else:
#        return state.has("Progressive Ungate Levels", player, 4)

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresMelee():
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"
