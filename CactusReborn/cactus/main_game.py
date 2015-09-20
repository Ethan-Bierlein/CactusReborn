"""
main_game.py

The classes and methods in this file are used to create,
and specify and additional data about your game, and then
wrap it up in a nice container, ready to play.
"""
import sys


def play_game(*, name, description, prompt, flowchart, case_sensitive, error_message, global_commands):
    """Play a user-created game.

    Keyword arguments:
    name            -- The name of the game.
    description     -- The description of the game.
    prompt          -- The game's prompt.
    flowchart       -- The flowchart that the player traverses.
    case_sensitive  -- Whether or not user input is lowered.
    error_message   -- The message to display when the user enters invalid input.
    global_commands -- Global commands that can be executed anywhere.
    """
    current_location = flowchart.find_start()
    
    if current_location is not None:
        while True:
            current_location.on_enter()
            new_key = current_location.get_user_input(prompt, error_message, case_sensitive, global_commands)
            current_location.on_exit()

            if new_key is not None:
                if new_key in flowchart.locations:
                    current_location = flowchart.locations[new_key]
                else:
                    raise KeyError("Invalid location key \"{0}\"".format(new_key))