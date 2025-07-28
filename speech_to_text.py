# speech_to_text.py

import speech_recognition as sr

def recognize_speech(language_code='en-US'):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language=language_code)
        print(f"✅ Recognized: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Speech not understood.")
        return "Could not understand audio"
    except sr.RequestError as e:
        print(f"❌ Error with the request: {e}")
        return "Speech recognition error"
