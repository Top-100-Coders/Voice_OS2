# import required libraries
from openai import OpenAI
from scipy.io.wavfile import write
import sounddevice as sd
import wavio as wv


from openai import OpenAI
client = OpenAI(api_key="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")

#transcription func
def transcrpt(aud):
    audio_file= open(aud, "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="text"
    )

    # print(f"transcript={transcript}")
    return transcript

#answering func
def chat(q):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You provide only shell commands to run in command line.Dont add any other text. Dont add any placeholder text. provide command as it should be typed in cmmand line."},
    {"role": "user", "content": "provide code to complete the following task. say error if task doesnt make sense:"+q}
    ],
    temperature=0.4, 
    max_tokens=256, 
    top_p=1, 
    frequency_penalty=0, 
    presence_penalty=0

    )

    # print(f"response = {response.choices[0].message.content}")
    return response.choices[0].message.content

    
