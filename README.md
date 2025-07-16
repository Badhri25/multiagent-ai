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

## 🚀 How to Run

### 🔧 Setup
```bash
pip install -r requirements.txt
```

### ▶️ Run Main File
```bash
python app/main.py
```

> Outputs include printed summaries and a saved audio file named `summary.mp3`.

---

## 🐳 Docker Setup (Optional)

```bash
docker build -t vahan-summarizer .
docker run vahan-summarizer
```

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
README.md
Dockerfile
```

---

## 📝 Notes
- You’ll need an OpenAI API key to run classification and summarization.
- Audio is saved locally as `summary.mp3`.
- Search is done using `arxiv` API.

---

## 📥 Sample Input/Output

**Input:** Topic = "large language models"

**Output:**
- `summary.txt` (summary of each paper)
- `summary.mp3` (spoken version of synthesis)

---

## 🙋 Contact
**Badhri Srinivasan**  