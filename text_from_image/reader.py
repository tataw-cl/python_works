import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog
root=tk.Tk()
root.withdraw()
img=filedialog.askopenfilename()

# Correct the path to the Tesseract executable on my local machine
#link it to the correct install location of the tesseract.exe file if path is incorrect
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe" 

#img = Image.open("text.png") if you wanna use a fixed image
text = pytesseract.image_to_string(img)  # converting to string
print(text)
