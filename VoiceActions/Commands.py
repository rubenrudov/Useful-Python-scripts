"""
Author: Ruben Rudov
Date: 28/06/2021
Purpose: Basic speech recognition program for using in more advanced tasks later..
"""

import speech_recognition as sr
from datetime import datetime
RECOGNIZER = sr.Recognizer()

# TODO: Add TTS for program responding


class CommandListener:
    def __init__(self):
        self.recognizer = RECOGNIZER
        self.command = "DEFAULT"
        self.tts_mute = False

    def basic_commands_listener(self):
        """
        :purpose: Do easy commands by voice commanding and TTS answer
        :return:
        """
        with sr.Microphone() as source:
            print("Listening for commands")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

            try:
                print("Recognizing command")
                query = self.recognizer.recognize_google(audio)

                if query == "time":
                    print(datetime.now())

                elif query == "turn off":
                    print("Not gonna happen...")

                elif query == "mute responses":
                    self.tts_mute = True

                elif str(query).replace(" ", "") == "unmuteresponse":
                    self.tts_mute = False

                else:
                    print("Command not in the commands list")

            except sr.UnknownValueError:
                print("Could not understand the command")

            print(f"Debug: {query.lower()}")

