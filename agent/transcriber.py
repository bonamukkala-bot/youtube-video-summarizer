from faster_whisper import WhisperModel
import os

def transcribe_audio(file_path):

    if not os.path.exists(file_path):
        raise FileNotFoundError("Audio file not found!")

    # Force CPU usage
    model = WhisperModel(
        "base",
        device="cpu",          # 🔥 IMPORTANT
        compute_type="int8",   # Optimized for CPU
        cpu_threads=8
    )

    segments, info = model.transcribe(
        file_path,
        beam_size=1,
        vad_filter=True
    )

    full_text = ""
    for segment in segments:
        full_text += segment.text + " "

    return full_text