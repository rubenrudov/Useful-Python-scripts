import VoiceActions.Commands as VoiceCommands


def main():
    command_listener = VoiceCommands.CommandListener()
    command_listener.basic_commands_listener()  # Check if works


if __name__ == '__main__':
    main()
