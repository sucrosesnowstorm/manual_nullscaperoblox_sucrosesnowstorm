from typing import Optional, Any, TYPE_CHECKING
from BaseClasses import MultiWorld, Item, Location

if TYPE_CHECKING:
    from ..Items import ManualItem
    from ..Locations import ManualLocation

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    excluded_classes = multiworld.worlds[player].options.class_select.value
    class_names = ["Prisoner", "Wanted", "Charger", "Diver", "Spirit", "Grappler", "Glider"]
    if category_name in class_names:
        return category_name not in excluded_classes
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item: dict[str, Any]) -> Optional[bool]:
    excluded_items = multiworld.worlds[player].options.class_select.value
    #List of items that correspond to classes, and their corresponding class names; for removal purposes duh.
    class_item_map = {
        "Prisoner Class": "Prisoner",
        "Wanted Class": "Wanted",
        "Charger Class": "Charger",
        "Diver Class": "Diver",
        "Spirit Class": "Spirit",
        "Grappler Class": "Grappler",
        "Glider Class": "Glider",
        "ROOTS IN DEFIANCE": "Prisoner",
        "ROOTS IN CERTAINTY": "Wanted",
        "ROOTS IN PERSISTENCE": "Charger",
        "ROOTS IN VERSATILITY": "Diver",
        "ROOTS IN SELF-AWARENESS": "Spirit",
        "ROOTS IN TRUST": "Grappler",
        "ROOTS IN BRAVERY": "Glider",
    }
    if item["name"] in class_item_map:
        return class_item_map[item["name"]] not in excluded_items
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
