"""
location.py

The classes and methods in this file are used to describe
a location, contained in a GameFlowchart class.
"""
import re
import sys
import time


class Location:
    """Represents a location in a GameFlowchart map.
    
    A location represents a "location" on the game's
    map, and contains data like a title, locations
    to other positions, etc.

    Keyword arguments:
    title       -- The title of the position.
    description -- The description of the position.
    locations  -- A dictionary of possible inputs, and reference keys.
    """
    def __init__(self, *, title, description_enter, description_exit, is_exit, locations):
        self.title = title
        self.description_enter = description_enter
        self.description_exit = description_exit
        self.is_exit = is_exit
        self.locations = locations

    def on_enter(self):
        """This function is run when the user enters.

        When the user "enters" a positions, this function will
        display the title, and position description.
        """
        print("\n" + self.title + ":")
        print("-- " + self.description_enter)

        if len(self.locations) != 0 and not self.is_exit:
            print("-- Locations: {}".format(", ".join(self.locations)))

        if self.is_exit:
            print("-- " + self.description_exit + "\n")
            time.sleep(5)
            sys.exit(0)

    def on_exit(self):
        """This function is run when the user exits.

        When the user "exits" as position, this function will
        display the exit message, and a newline.
        """
        print("-- " + self.description_exit + "\n")

    def get_user_input(self, prompt, error_message, case_sensitive, global_commands):
        """Get user input, and check to make sure it's valid.

        This function takes user input, sanitizes it, and
        then checks to make sure that it's valid by checking
        it against the locations. If it is valid, then the
        referenced map key is returned. It it's invalid, then
        the function returns None.

        Keyword arguments:
        prompt        -- The prompt to use with user input.
        error_message -- The error message to display when the input is invalid.
        """
        if not self.is_exit:
            user_input = re.sub(r"([^\s\w]|_)", "", input(prompt).strip())
            user_input = user_input.lower() if not case_sensitive else user_input
            if user_input in self.locations:
                return self.locations[user_input]

            elif user_input in global_commands:
                global_commands[user_input]()
                return

            print(error_message)
            return