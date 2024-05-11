from gtts import gTTS
text="Hello, how are you doing today?"
lang='en'
tts=gTTS(text=text,lang=lang, slow=False)
tts.save("sample.mp3")