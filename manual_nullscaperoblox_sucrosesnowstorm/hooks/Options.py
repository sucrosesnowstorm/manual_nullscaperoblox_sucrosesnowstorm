# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions, OptionSet
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#

class ClassSelect(OptionSet):
    """
    Exclude specific classes from the randomizer (except Charger/Diver).
    These are "grappler", "spirit", "glider", "prisoner", and "wanted" (case sensitive).
    Each class contains a significant amount of locations, so avoid removing too many without also removing items to compensate.
    """
    display_name = "Classes Excluded"
    valid_keys = frozenset([
        "prisoner",
        "wanted",
        "spirit",
        "grappler",
        "glider"
    ])
    default = frozenset([])

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    #Add the options to the options dict so that they are defined in the Options Creator
    options["class_select"] = ClassSelect
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"
    options.type_hints["goal"].options.clear()
    options.type_hints["goal"].options.update({"reach level 10": 0, "reach level 15": 1, "reach level 20": 2})

    options.type_hints["goal"].name_lookup.clear()
    options.type_hints["goal"].name_lookup.update({0: "reach level 10", 1: "reach level 15", 2: "reach level 20"})
    options.type_hints["goal"].default = 0
    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    groups["Class Options"].append(ClassSelect)
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
