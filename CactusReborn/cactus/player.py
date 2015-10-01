"""
player.py

The classes and methods contained in this file are used
to describe a player.
"""


class Player:
    """Describes a player.

    This class is used to describe a player, who "plays"
    a game. The player stores data like items, name, etc.

    Keyword arguments:
    name  -- The name of the player.
    items -- The items the player has. The value is in the format item_name -> item_count.
    """
    def __init__(self, *, name, items):
        self.name = name
        self.items = items

    def contains_item(self, *, item_name, required_count):
        """Check to see if the player has a certain item.

        This will check to see if a certain item is
        contained inside of the item dictionary, and
        if the player has the required count as well.
        This function will return True if the item, and
        item count are appropriate, and False if that
        isn't the case.

        Keyword arguments:
        item_name      -- The name of the item to find.
        required_count -- The required number of items to have.
        """
        if item_name in self.items:
            if self.items[item_name] >= required_count:
                return True
        else:
            return False