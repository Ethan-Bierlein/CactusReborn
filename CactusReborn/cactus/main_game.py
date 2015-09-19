"""
main_game.py

The classes and methods in this file are used to create,
and specify and additional data about your game, and then
wrap it up in a nice container, ready to play.
"""
import sys


def play_game(*, name, description, prompt, flowchart, case_sensitive, error_message, global_commands):
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