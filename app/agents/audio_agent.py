from gtts import gTTS
import os

def text_to_speech(summary_text, output_path="output_audio.mp3"):
    tts = gTTS(summary_text)
    tts.save(output_path)
    print(f"✅ MP3 saved as: {output_path}")
