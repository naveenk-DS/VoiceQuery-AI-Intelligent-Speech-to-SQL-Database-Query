import speech_recognition as sr

def recognize_speech(language_code='en-US'):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language=language_code)
            print("Recognized Speech:", text)
            return text
        except sr.UnknownValueError:
            return "Sorry, could not understand."
        except sr.RequestError:
            return "API unavailable or quota exceeded."
