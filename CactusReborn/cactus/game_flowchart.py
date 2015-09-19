"""
game_flowchart.py

The classes and methods in this file are used to create a
flowchart. A flowchart is essentialy a "map" of how your
game is played.
"""
import re


class GameFlowchart:
    """Represents a flowchart, or "map".
    
    This class is a representation of a "map" in a
    Cactus game. Essentially, a Flowchart is a
    dictionary, where the keys are locations to
    each position.

    Keyword arguments:
    locations -- A dictionary of socks.
    """
    def __init__(self, *, locations):
        self.locations = locations

    def iterate_locations(self):
        for key, value in self.locations:
            yield (key, value)

    def find_by_reference(self, reference):
        """Find, and obtain the value of a position, by reference.

        This function checks to see if a reference value is in
        the dictionary of locations. If it is, then return the
        value, and if it isn't, then return None.

        Keyword arguments:
        reference -- The reference value.
        """
        if reference in self.locations:
            return self.locations[reference]
        return

    def find_start(self):
        """Returns the "starting position" in the locations.

        This function will find the starting position in
        the locations. It does not matter if the starting
        position is capitalized, contains odd characters, or
        has spaces. As long as it contains the characters
        "start", it (should) work. This will return None
        if the item is not found.
        """
        for key, item in self.locations.items():
            if re.sub(r"([^\s\w]|_)", "", key) == "start":
                return self.locations[key]
        return
