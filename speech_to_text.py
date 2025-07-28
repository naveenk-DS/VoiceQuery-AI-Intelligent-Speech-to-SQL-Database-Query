import speech_recognition as sr
import tempfile
import os

def recognize_speech_from_audio(audio_file, language_code='en-US'):
    r = sr.Recognizer()
    
    # Save uploaded audio to a temp WAV file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio_file.read())
        temp_audio_path = temp_audio.name

    with sr.AudioFile(temp_audio_path) as source:
        audio = r.record(source)
    
    try:
        text = r.recognize_google(audio, language=language_code)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio."
    except sr.RequestError:
        return "Speech recognition service unavailable."
    finally:
        os.remove(temp_audio_path)
