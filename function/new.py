from google.cloud import speech
from google.oauth2 import service_account 

credentials=service_account.Credentials.from_service_account_file('./banded-pager-368009-a62bb17e9932.json')
client = speech.SpeechClient(credentials=credentials)

# 
with open('./audio.mp4', "rb") as audio_file:
    content = audio_file.read()

# import sys
# with open(sys.argv[1], 'r') as f:
#     content = f.read()
# print(content)

audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code="en-US",
    audio_channel_count=2,
    enable_separate_recognition_per_channel=True,
)

response = client.recognize(config=config, audio=audio)

for i, result in enumerate(response.results):
    alternative = result.alternatives[0]
    print("-" * 20)
    print("First alternative of result {}".format(i))
    print(u"Transcript: {}".format(alternative.transcript))
    print(u"Channel Tag: {}".format(result.channel_tag))