import streamlit as st
from speech_to_text import recognize_speech
from sql_generator import natural_language_to_sql
from query_parser import execute_sql_query

st.title("🎙️ VoiceQuery AI: Intelligent Speech-to-SQL System")

lang = st.selectbox("Select Language", ["en-US", "ta-IN", "hi-IN"])
st.info("Click below and speak your question related to the database...")

if st.button("🎤 Start Recording"):
    input_text = recognize_speech(language_code=lang)
    st.success(f"🗣️ You said: {input_text}")

    if input_text:
        sql_query = natural_language_to_sql(input_text)
        st.code(sql_query, language='sql')

        result = execute_sql_query(sql_query)
        st.write("🔍 Query Result:")
        st.dataframe(result)
