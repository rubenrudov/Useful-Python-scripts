"""
Author: Ruben Rudov
Date: 28/06/2021
Purpose: Basic speech recognition program for using in more advanced tasks later..
"""

import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio")
    print(query.lower())
