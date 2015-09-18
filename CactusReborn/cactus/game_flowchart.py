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
    dictionary, where the keys are references to
    each position.

    Keyword arguments:
    references -- A dictionary of socks.
    """
    def __init__(self, *, references):
        self.references = references

    def find_by_reference(self, reference):
        """Find, and obtain the value of a position, by reference.

        This function checks to see if a reference value is in
        the dictionary of references. If it is, then return the
        value, and if it isn't, then return None.

        Keyword arguments:
        reference -- The reference value.
        """
        if reference in self.references:
            return self.references[reference]
        return None

    def find_start(self):
        """Returns the "starting position" in the references.

        This function will find the starting position in
        the references. It does not matter if the starting
        position is capitalized, contains odd characters, or
        has spaces. As long as it contains the characters
        "start", it (should) work. This will return None
        if the item is not found.
        """
        for key, item in self.references.items():
            if re.sub(r"([^\s\w]|_)", "", key) == "start":
                return self.references[item]
        return None
