"""
location.py

The classes and methods in this file are used to describe
a location, contained in a GameFlowchart class.
"""
import re

class Location:
    """Represents a location in a GameFlowchart map.
    
    A location represents a "location" on the game's
    map, and contains data like a title, references
    to other positions, etc.

    Keyword arguments:
    title       -- The title of the position.
    description -- The description of the position.
    references  -- A dictionary of possible inputs, and reference keys.
    """
    def __init__(self, *, title, description_enter, description_exit, references):
        self.title = title
        self.description_enter = description_enter
        self.description_exit = description_exit
        self.references = references

    def on_enter(self):
        """This function is run when the user enters.

        When the user "enters" a positions, this function will
        display the title, and position description.
        """
        print(self.title)
        print("-" * len(self.title))
        print(self.description_enter)

    def on_exit(self):
        """This function is run when the user exits.

        When the user "exits" as position, this function will
        display the exit message, and a newline.
        """
        print(self.description_exit)
        print("-" * len(self.title) + "\n")

    def get_user_input(self, prompt, error_message):
        """Get user input, and check to make sure it's valid.

        This function takes user input, sanitizes it, and
        then checks to make sure that it's valid by checking
        it against the references. If it is valid, then the
        referenced map key is returned.

        Keyword arguments:
        prompt        -- The prompt to use with user input.
        error_message -- The error message to display when the input is invalid.
        """
        user_input = re.sub(r"([^\s\w]|_)", input(prompt).strip())
        if user_input in self.references:
            return self.references[user_input]

        print(error_message)
        return