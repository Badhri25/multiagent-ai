# Vahan AI Internship Assignment

## 📌 Multi-Agent System for Research Paper Summarization

This project is a multi-agent AI system that automatically discovers, analyzes, summarizes, and generates audio podcasts from research papers using OpenAI and Python.

---

## ⚙️ Features

✅ Search research papers using `arxiv` API  
✅ Accept URLs and PDFs for extraction using `PyMuPDF`  
✅ Classify topic based on user-defined list using GPT-3.5  
✅ Summarize each paper individually using OpenAI LLMs  
✅ Synthesize summaries across papers  
✅ Generate audio podcast (.mp3) for summaries using `gTTS`  
✅ Fully dockerized 2-command setup

---

## 🧠 Agents Breakdown

| Agent Name         | Role                                                  |
|-------------------|--------------------------------------------------------|
| `search_agent`    | Finds papers from arXiv based on query                |
| `extract_agent`   | Extracts full text from PDFs                          |
| `classify_agent`  | Classifies paper into topic using GPT                 |
| `summarize_agent` | Summarizes the content using OpenAI                   |
| `synthesize_agent`| Combines multiple summaries into one                  |
| `audio_agent`     | Converts text to audio podcast using gTTS             |

---

## 🚀 Setup Instructions

### 🔧 Local Setup
```bash
pip install -r requirements.txt
python app/main.py
```
> Outputs include printed summaries and a saved audio file named `summary.mp3`.

### 🐳 Docker Setup (Optional)
```bash
docker build -t vahan-summarizer .
docker run vahan-summarizer
```

---

## 🏗️ System Architecture

This system follows a modular multi-agent architecture:
- Each core function (search, extract, classify, etc.) is implemented as an independent agent module.
- The `main.py` orchestrates the workflow from search to audio generation.
- Agents communicate through function calls and shared data (not message queues).

```
User Query → Search Agent → Extract Agent → Classify Agent → Summarize Agent → Synthesize Agent → Audio Agent
```

---

## 🤖 Multi-Agent Design & Coordination

Each agent:
- Is a Python module with a clearly defined class/function.
- Operates independently, allowing easy debugging, testing, and scaling.
- Is called in sequence from `main.py`, passing results from one to the next.

This modular design ensures:
- Separation of concerns
- Easier maintenance and extensibility

---

## 📄 Paper Processing Methodology

1. **Search Agent** pulls top N relevant papers using the arXiv API.
2. **Extract Agent** downloads and extracts raw text from each PDF.
3. **Classify Agent** uses GPT-3.5 to tag each paper with a relevant topic from a pre-defined list.
4. **Summarize Agent** sends paper content to GPT and receives summaries.
5. **Synthesize Agent** combines summaries into a coherent single overview.
6. **Audio Agent** converts the final summary into audio (podcast-style).

---

## 🔊 Audio Generation Implementation

The final summary is converted into a `.mp3` file using `gTTS`:
```python
from gtts import gTTS
text = "Final summary text"
tts = gTTS(text)
tts.save("summary.mp3")
```
- Requires internet connection
- Produces high-quality TTS from Google

---

## ⚠️ Limitations & Future Improvements

### Current Limitations:
- Relies on OpenAI and gTTS — needs API keys and internet
- Token limits in GPT may truncate large papers
- No GUI or web interface

### Future Enhancements:
- Add a Streamlit frontend for ease of use
- Replace gTTS with offline TTS option
- Handle long PDFs with chunked summarization
- Add retry + logging to improve reliability
- Support for additional paper sources (Semantic Scholar, DOI input)

---

## 🗂️ Folder Structure
```
app/
├── agents/
│   ├── search_agent.py
│   ├── extract_agent.py
│   ├── classify_agent.py
│   ├── summarize_agent.py
│   ├── synthesize_agent.py
│   └── audio_agent.py
├── main.py
samples/
├── sample_input.txt
├── sample_summary.txt
├── output_audio.mp3
README.md
Dockerfile
```

---

## 📥 Sample Input/Output

**Input:** Topic = "large language models"

**Output:**
- `sample_summary.txt` (GPT-generated summary)
- `summary.mp3` (spoken version of synthesis)

---

## 🙋 Contact
**Badhri Srinivasan**  


