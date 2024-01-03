import os
from pathlib import Path
from openai import OpenAI
import speech_recognition as sr

client = OpenAI()


def convert_voice_to_text(voice_file_path):
    r = sr.Recognizer()
    
    with sr.AudioFile(voice_file_path) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
    
    return text

def convert_live_voice_to_text():
    r = sr.Recognizer()
        
    with sr.Microphone() as source:
        print("Listening...")
        audio_data = r.listen(source)
        print("Processing...")
            
        try:
            text = r.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Unable to recognize speech")
        except sr.RequestError as e:
            print(f"Error: {e}")
        
    return None

text = convert_voice_to_text()

#speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input=text
)

response.stream_to_file("output.mp3")