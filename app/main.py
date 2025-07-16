from agents.search_agent import search_papers
from agents.extract_agent import extract_text_from_pdf
from agents.classify_agent import classify_topic
from agents.summarize_agent import summarize_text
from agents.synthesize_agent import synthesize_topics
from agents.audio_agent import text_to_speech
import os

TOPICS = ["Machine Learning", "NLP", "Computer Vision", "Reinforcement Learning"]

if __name__ == '__main__':
    results = search_papers("large language models")
    summaries = []

    for idx, (title, url) in enumerate(results):
        print(f"\n[+] Downloading and processing: {title}")
        filename = f"paper_{idx}.pdf"
        os.system(f"wget -O {filename} {url}")
        text = extract_text_from_pdf(filename)
        topic = classify_topic(text, TOPICS)
        summary = summarize_text(text)
        print(f"Topic: {topic}\n\nSummary:\n{summary}\n")
        summaries.append(summary)

    synthesis = synthesize_topics(summaries)
    print("\n[Cross-paper Synthesis]\n", synthesis)
    audio_path = text_to_speech(synthesis, output_path="summary.mp3")
    print(f"\n[Audio saved to]: {audio_path}")
