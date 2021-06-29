"""
Author: Ruben Rudov
Date: 28/06/2021
Purpose: Basic speech recognition program for using in more advanced tasks later..
"""

import speech_recognition as sr
from datetime import datetime
from gtts import gTTS
import os
import playsound

RECOGNIZER = sr.Recognizer()


# TODO: Add TTS for program responding


def say(text, FILE_COUNT):
    """
    :param FILE_COUNT:
    :param text: str that contains the proffered voice output
    :return: None
    """
    text_to_speech = gTTS(text=text, lang='en')
    text_to_speech.save(f'audio{FILE_COUNT}.mp3')
    playsound.playsound(f'audio{FILE_COUNT}.mp3')
    os.remove(f'audio{FILE_COUNT}.mp3')


class CommandListener:
    def __init__(self, count):
        self.recognizer = RECOGNIZER
        self.command = "DEFAULT"
        self.tts_mute = False
        self.file_count = count

    def basic_commands_listener(self):
        """
        :purpose: Do easy commands by voice commanding and TTS answer
        :return: Boolean if function should run or not
        """
        with sr.Microphone() as source:
            print("Listening for commands")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

            try:
                print("Recognizing command...")
                query = self.recognizer.recognize_google(audio)

                if query == "time":
                    say(datetime.strftime(datetime.now(), "%H:%M:%S"), self.get_count())
                    print(str(datetime.now()))

                elif query == "stop":
                    # For turning of the listening system
                    say("Shutting down voice assistant", self.get_count())
                    # FIXME: Add some normal shut down speech ...
                    return False

                elif query == "mute":
                    self.tts_mute = True

                elif str(query).replace(" ", "") == "unmute":
                    self.tts_mute = False

                # TODO: Add more voice commands for the system
                #  that contains real-life actions like move forward (and then control with Rpi)

                else:
                    print("Command not in the commands list")
                    return False

            except sr.UnknownValueError:
                print("Could not understand the command")

            print(f"Debug: {query.lower()}")

        return True

    def get_count(self):
        # Accessor for audio files count
        return self.file_count