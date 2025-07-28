# speech_to_text.py

import speech_recognition as sr
from googletrans import Translator



def recognize_speech(language_code='en-US'):
    r = sr.Recognizer()
    translator = Translator()
    
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language=language_code)
        translated = translator.translate(text, dest='en')
        return translated.text

    except sr.UnknownValueError:
        return "Sorry, could not understand the audio."
    except sr.RequestError:
        return "API unavailable or quota exceeded."
