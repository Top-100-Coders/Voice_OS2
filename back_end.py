from openai import OpenAI


# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv


from openai import OpenAI
client = OpenAI(api_key="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")

def transcrpt(aud):
    audio_file= open(aud, "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="text"
    )
    return transcript

def chat(q):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You provide shell commands to run in command line."},
    {"role": "user", "content": "provide code to complete the following task. say error if task doesnt make sense:"+q}
    ]
    )
    return response.choices[0].message.content

    
