import streamlit as st
from speech_to_text import recognize_speech
from sql_generator import natural_language_to_sql
from query_parser import execute_sql_query
from speech_to_text import recognize_speech_from_audio
from speech_to_text import recognize_speech


audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3"])

if audio_file is not None:
    text = recognize_speech_from_audio(audio_file)
    st.write("Recognized Text:", text)
st.set_page_config(page_title="VoiceQuery AI", layout="wide")
st.title("🎤 VoiceQuery AI: Speak to SQL")

lang = st.selectbox("🎙️ Choose Your Language", ["en-US", "ta-IN", "hi-IN", "te-IN", "fr-FR", "es-ES", "de-DE"])

if st.button("🎙️ Start Voice Input"):
    with st.spinner("Listening..."):
        input_text = recognize_speech(language_code=lang)
        st.success(f"✅ Transcribed: {input_text}")

        sql = natural_language_to_sql(input_text)
        st.code(sql, language='sql')

        result = execute_sql_query(sql)
        st.write("📊 Query Result:")
        st.dataframe(result)
uploaded_audio = st.file_uploader("Upload audio file", type=["wav", "mp3"])
if uploaded_audio:
    with open("temp.wav", "wb") as f:
        f.write(uploaded_audio.read())
    input_text = recognize_speech_from_audio("temp.wav", language_code=lang)
