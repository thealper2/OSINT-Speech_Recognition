import streamlit as st
from speech_recognition import AudioFile, Recognizer

def transcript(file, keywords):
    found = []
    transcriptions = []
    recognizer = Recognizer()

    with AudioFile(file) as file:
        audio = recognizer.record(file)
        transcriptions.append(recognizer.recognize_google(audio))

    for keyword in keywords:
        for transcription in transcriptions:
            if keyword.lower() in transcription.lower():
                found.append(keyword)

    return found, transcriptions

st.sidebar.title("OSINT Speech Recognition")
uploaded_file = st.sidebar.file_uploader("Choose an audio file")

if uploaded_file is not None:
    keyword = st.sidebar.text_input("Seperate keywords with ,", "")
    if st.sidebar.button("Analyze"):
        st.header("Analysis for " + str(uploaded_file.name))
        keywords = keyword.split(",")
        found, transcriptions = transcript(uploaded_file, keywords)

        st.header("Transcript")
        for transcript in transcriptions:
            st.write(transcript)

        if keyword != "":
            st.header("Keyword Results")
            for keyword in keywords:
                if keyword in found:
                    st.success("Keyword {} found in audio.".format(keyword))

                else:
                    st.warning("Keyword {} not found in audio.".format(keyword))
