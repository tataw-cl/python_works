# from gtts import gTTS
# import tkinter as tk
# from tkinter import filedialog
# root=tk.Tk()
# root.withdraw()
# text_file=filedialog.askopenfilename()
# # text="Hello, how are you doing today?"
# lang='en'
# tts=gTTS(text=text_file,lang=lang, slow=False)
# tts.save("sample.mp3")

#Doesn't work yet
import tkinter as tk
from tkinter import filedialog
from gtts import gTTS
from pdf2image import convert_from_path
import pytesseract

root = tk.Tk()
root.withdraw()

# Open a file dialog and get the file path
pdf_file_path = filedialog.askopenfilename()

# Convert the PDF to images
pages = convert_from_path(pdf_file_path)

# Initialize an empty string for the text
text = ""

# Loop through each page image and extract the text
for page in pages:
    text += pytesseract.image_to_string(page)

lang = 'en'
tts = gTTS(text=text, lang=lang, slow=False)
tts.save("sample.mp3")