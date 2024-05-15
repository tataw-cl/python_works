from gtts import gTTS
import tkinter as tk
from tkinter import filedialog
root=tk.Tk()
root.withdraw()
text_file=filedialog.askopenfilename()
# text="Hello, how are you doing today?"
lang='en'
tts=gTTS(text=text_file,lang=lang, slow=False)
tts.save("sample.mp3")