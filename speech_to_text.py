import speech_recognition as sr

def recognize_speech(language_code='en-US'):
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language=language_code)
        return text
    except sr.UnknownValueError:
        return "Sorry, could not understand the audio."
    except sr.RequestError:
        return "API unavailable or quota exceeded."
