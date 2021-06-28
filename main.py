"""
Author: Ruben Rudov
Date: 29/06/2021
Purpose: Call and handle all the required objects
"""

import VoiceActions.Commands as VoiceCommands


def main():
    run_listener = True
    file_count = 0

    while run_listener:
        command_listener = VoiceCommands.CommandListener(file_count)
        run_listener = command_listener.basic_commands_listener()  # Check if works
        file_count += 1  # Increments the file number for this program


if __name__ == '__main__':
    main()
