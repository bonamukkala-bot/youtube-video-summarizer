

# 🎥 YouTube AI Video Summarizer Agent

> Turn any YouTube video into a clean, readable summary using AI 🤖
> Built using Python, Whisper, LangChain, Ollama & Streamlit

---

## 🌟 What This Project Does

This project:

1. 📥 Downloads audio from a YouTube video
2. 🧠 Converts speech into text (Transcription)
3. ✍ Summarizes the text using AI
4. 🌐 Shows the summary in a simple web app

So instead of watching a 1-hour video, you can read the summary in 1–2 minutes ⚡

---

# 🧠 How This Project Works (Simple Explanation)

Let’s understand step by step:

### Step 1 — Download Audio

We use:

```
yt_dlp
```

It downloads only the audio from the YouTube video.

---

### Step 2 — Convert Speech to Text

We use:

```
faster-whisper
```

It listens to the audio and converts it into text (like subtitles).

---

### Step 3 — Summarize Text

We use:

```
LangChain + Ollama (Gemma model)
```

AI reads the transcript and creates a short summary.

---

### Step 4 — Show in Web App

We use:

```
Streamlit
```

To create a simple website interface.

---

# 🏗 Project Folder Structure

```
youtube-ai-agent/
│
├── app.py
├── requirements.txt
│
├── agent/
│   ├── downloader.py
│   ├── transcriber.py
│   ├── summarizer.py
│
└── README.md
```

---

# 💻 Step-by-Step Installation Guide

Follow carefully 👇

---

## 🔹 Step 1: Install Python

Download Python from:

👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

After installing, check:

```bash
python --version
```

If it shows version number ✅ Good!

---

## 🔹 Step 2: Create Project Folder

```bash
mkdir youtube-ai-agent
cd youtube-ai-agent
```

---

## 🔹 Step 3: Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

### Windows:

```bash
venv\Scripts\activate
```

### Mac/Linux:

```bash
source venv/bin/activate
```

---

## 🔹 Step 4: Install Required Libraries

Create `requirements.txt` file and add:

```
streamlit
yt-dlp
faster-whisper
langchain
langchain-community
langchain-text-splitters
ollama
```

Now install:

```bash
pip install -r requirements.txt
```

---

## 🔹 Step 5: Install FFmpeg (IMPORTANT)

Whisper needs FFmpeg.

Download from:
👉 [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

After installing, check:

```bash
ffmpeg -version
```

If it shows version ✅ Good!

---

## 🔹 Step 6: Install Ollama

Download Ollama:

👉 [https://ollama.com/download](https://ollama.com/download)

After installing, run:

```bash
ollama --version
```

---

## 🔹 Step 7: Pull AI Model (Gemma 2B)

```bash
ollama pull gemma:2b
```

This downloads the AI model.

---

# ▶ How To Run The Project

Inside project folder:

```bash
streamlit run app.py
```

It will open:

```
http://localhost:8501
```

Paste YouTube URL → Click Generate Summary 🎉

---

# 📜 Code Explanation (Beginner Friendly)

## downloader.py

* Uses `yt_dlp`
* Downloads best audio
* Converts to mp3

---

## transcriber.py

* Uses `WhisperModel`
* Converts speech → text
* Uses CPU mode

---

## summarizer.py

* Uses `Ollama`
* Splits text into chunks
* Sends chunks to AI
* Combines summaries

---

## app.py

Main app file:

* Takes YouTube link
* Calls downloader
* Calls transcriber
* Calls summarizer
* Displays result

---

# 🚀 Technologies Used

| Tool           | Purpose                |
| -------------- | ---------------------- |
| Python         | Programming language   |
| Streamlit      | Web interface          |
| yt-dlp         | Download YouTube audio |
| Faster-Whisper | Speech to text         |
| LangChain      | Text processing        |
| Ollama         | Run AI model locally   |
| Gemma 2B       | AI summarization model |

---

# 🎯 Why This Project Is Powerful

✅ Works offline (after model download)
✅ No paid APIs required
✅ Uses Local AI
✅ Beginner Friendly
✅ Real-world AI project

---

# 🧪 Example Workflow

1. Paste YouTube link
2. Audio downloads
3. Whisper transcribes
4. AI summarizes
5. Summary appears

---

# 🛠 Common Errors & Fixes

### ❌ FFmpeg not found

Install FFmpeg and add to PATH.

---

### ❌ Ollama model not found

Run:

```bash
ollama pull gemma:2b
```

---

### ❌ Port already in use

Run:

```bash
streamlit run app.py --server.port 8502
```

---

# 🌈 Future Improvements

* Add timestamps
* Add summary length options
* Add Telugu language support
* Add download summary as PDF
* Add AI-generated notes
