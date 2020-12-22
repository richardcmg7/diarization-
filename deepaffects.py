import requests
import base64

url = "https://proxy.api.deepaffects.com/audio/generic/api/v2/async/diarize"

querystring = {"apikey":"hngjVXmpqvsQZ2f7pAn5wKjQJj3eo1fa", "webhook":"https://webhook.site/c6401689-dfa2-4443-a6a4-a4187e2e708f"}

payload = {
    "encoding": "Wave",
    "languageCode": "en-EN",
    "speakerCount": 3,
    "doVad": True,
    # "audioType": "callcenter"
    "audioType": "meeting"
}

# The api accepts data either as a url or as base64 encoded content
# passing payload as url:
# payload["url"] = "https://publicly-facing-url.wav"
# alternatively, passing payload as content:
with open('data/diarizationExample.wav', 'rb') as fin:
    audio_content = fin.read()
payload["content"] = base64.b64encode(audio_content).decode('utf-8')

headers = {
    'Content-Type': "application/json",
}

response = requests.post(url, json=payload, headers=headers, params=querystring)

print(response.text)

# python