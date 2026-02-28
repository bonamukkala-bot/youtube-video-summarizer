import streamlit as st
import os
from agent.downloader import download_audio
from agent.transcriber import transcribe_audio
from agent.summarizer import summarize_text


st.set_page_config(page_title="YouTube AI Agent", layout="centered")

st.title("🎥 YouTube Video Summarizer Agent")
st.markdown("Summarize any YouTube video in 1–2 minutes ⚡")

url = st.text_input("Enter YouTube Video URL")

if st.button("Generate Summary"):

    if not url.strip():
        st.warning("⚠ Please enter a valid YouTube URL.")
        st.stop()

    try:
        # Step 1: Download
        with st.spinner("📥 Downloading audio..."):
            audio_path = download_audio(url)

        if not os.path.exists(audio_path):
            st.error("❌ Audio file not found after download.")
            st.stop()

        if os.path.getsize(audio_path) == 0:
            st.error("❌ Downloaded audio file is empty.")
            st.stop()

        st.success("✅ Audio downloaded successfully.")

        # Step 2: Transcribe
        with st.spinner("🧠 Transcribing audio..."):
            transcript = transcribe_audio(audio_path)

        if not transcript.strip():
            st.error("❌ Transcription failed or returned empty text.")
            st.stop()

        st.success("✅ Transcription completed.")

        # Step 3: Summarize
        with st.spinner("✍ Summarizing video..."):
            summary = summarize_text(transcript)

        st.success("🎉 Summary Generated Successfully!")

        st.subheader("📌 Video Summary")
        st.write(summary)

        # Optional: Show transcript (expandable)
        with st.expander("📜 View Full Transcript"):
            st.write(transcript)

    except Exception as e:
        st.error(f"🚨 Error occurred: {str(e)}")