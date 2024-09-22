from pytube import YouTube

def ytvd(url_s):
    YTObj = YouTube(url_s)
    YTObj = YTObj.streams.get_highest_resolution()
    try:
        YTObj.download()
    except:
        print("There was an error while downloading")
    print("Download is completed successfully")


url_s = "https://www.youtube.com/watch?v=Y8Tko2YC5hA"
ytvd(url_s)

from moviepy.editor import *
from moviepy.editor import VideoFileClip
video_name = "What is Python Why Python is So Popular"
vid = VideoFileClip(f"{video_name}.mp4")
vid.audio.write_audiofile(f"{video_name}.mp3")

import openai
import json

aud_name = "What is Python Why Python is So Popular.mp3"
aud_file= open(aud_name, "rb")

# Reading keys
api_info_path = "key.json"
with open(api_info_path, "r") as f:
    keys = json.load(f)
whisp_key = keys["key"]
org_id = keys["organization_id"]

# Settings keys to the API module
openai.organization = org_id
openai.api_key = whisp_key

print("Be Patient ... Converting your audio to text")
tp = openai.Audio.transcribe("whisper-1", aud_file)
txt = tp["text"]
print(txt)

print("Be Patient ... ChatGPT is summarizing your text")
response = openai.ChatCompletion.create(
model="gpt-3.5-turbo",
messages=[
        {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible."},
        {"role": "user", "content": f"Summarize the following text: {text}"}
    ]
)

print(response['choices'][0]['message']['content'])