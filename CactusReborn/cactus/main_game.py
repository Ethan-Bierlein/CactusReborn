"""
main_game.py

The classes and methods in this file are used to create,
and specify and additional data about your game, and then
wrap it up in a nice container, ready to play.
"""
import sys


class MainGame:
    """Represents a game in Cactus.

    This class represents a game in Cactus.

    Keyword arguments:
    name            -- The name of the game.
    description     -- The description of the game.
    prompt          -- The game's prompt.
    flowchart       -- The flowchart that the player traverses.
    case_sensitive  -- Whether or not user input is lowered.
    error_message   -- The message to display when the user enters invalid input.
    global_commands -- Global commands that can be executed anywhere.
    """
    def __init__(self, *, 
                 name, 
                 description, 
                 prompt, 
                 flowchart, 
                 case_sensitive, 
                 error_message,
                 player_object,
                 global_command_starting_char,
                 global_commands):
        self.name = name
        self.description = description
        self.prompt = prompt
        self.flowchart = flowchart
        self.case_sensitive = case_sensitive
        self.error_message = error_message
        self.player_object = player_object
        self.global_command_starting_char = global_command_starting_char
        self.global_commands = global_commands

    def play_game(self):
        """Play the user-created game.

        This function does as the name describes, it plays the
        user-created MainGame instance.
        """
        print(self.name + ":")
        print(self.description)
        print("Player name: " + self.player_object.name + "\n")

        current_location = self.flowchart.find_start()
        invalid_input = False
    
        if current_location is not None:
            while True:
                if not invalid_input:
                    current_location.on_enter()

                new_key = current_location.get_user_input(
                    self.prompt, 
                    self.error_message, 
                    self.case_sensitive, 
                    self.global_command_starting_char, 
                    self.global_commands
                )

                if new_key is not None:
                    invalid_input = False
                    current_location.on_exit()

                    if new_key in self.flowchart.locations:
                        new_location = self.flowchart.locations[new_key]

                        if new_location.access_items is not None:
                            if self.player_object.contains_item(new_location.access_items):
                                current_location = new_location
                            else:
                                print("Your player requires the items \"{}\" to proceed.".format(
                                    self.flowchart.locations[new_key].access_items
                                ))
                                invalid_input = True
                        else:
                            current_location = new_location
                    else:
                        raise KeyError("Invalid location key \"{0}\"".format(new_key))
                else:
                    invalid_input = True