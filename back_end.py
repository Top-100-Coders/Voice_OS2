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

    # print(f"transcript={transcript}")
    return transcript

def chat(q):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You provide only shell commands to run in command line.Dont add any other text. Dont add any placeholder text. provide command as it should be typed in cmmand line."},
    {"role": "user", "content": "provide code to complete the following task. say error if task doesnt make sense:"+q}
    ],
    temperature=0.85, 
    max_tokens=256, 
    top_p=1, 
    frequency_penalty=0, 
    presence_penalty=0

    )

    # print(f"response = {response.choices[0].message.content}")
    return response.choices[0].message.content

    
