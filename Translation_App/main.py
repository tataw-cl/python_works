from tkinter import *
import textblob
from tkinter import ttk, messagebox
from googletrans import LANGUAGES
from translate import Translator
root=Tk()
root.title('Tataw translator')
#root.iconbitmap
root.geometry("800x300")
def Translater():
    try:
        #Deleting any previous translated text
        translated_text.delete(1.0, END)
        #One way of getting the from and to languages
        for key,value in LANGUAGES.items():
            if(value==original_Combobox.get()):
                from_key_lang=key
        for key,value in LANGUAGES.items():
            if(value==translated_Combobox.get()):
                to_key_lang=key
        #words=textblob.TextBlob(original_text.get(1.0, END))
        words=original_text.get(1.0, END)

        #Translate the text
        translation=Translator(from_lang=from_key_lang, to_lang=to_key_lang)
        words=translation.translate(words)
        #output translated text to screen
        translated_text.insert(1.0, words)


                #other way of detecting language
        # original_text_word=original_text.get(1.0, END)
        # #create a textblob object
        # text= textblob.TextBlob(original_text_word)
        # #detect language
        # lang= text.detect_language()
        # #get the selected language
        #lang
    except Exception as e:
        print(f'An error occurred: {e}')
        messagebox.showerror("Translator", e)
def clear():
    #clear the screen
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

#grab language list from translator
# Get a list of supported languages
lang_list = list(LANGUAGES.values())
lang_list.sort()
#text boxes
original_text=Text(root, height=10, width=35)
original_text.grid(row=0, column=0, padx=8, pady=8)

translated_text=Text(root, height=10, width=35)
translated_text.grid(row=0, column=2,padx=8, pady=8)
translate_button=Button(root, text="Translate", font=("Helvetica", 24), command=Translater)
translate_button.grid(row=0, column=1, padx=8)

#ComboBoxes
original_Combobox=ttk.Combobox(root, width=40,value=lang_list)
original_Combobox.current(21)
original_Combobox.grid(row=2, column=0, padx=10, pady=15)
translated_Combobox=ttk.Combobox(root, width=40,value=lang_list)
translated_Combobox.current(26)
translated_Combobox.grid(row=2, column=2, padx=10, pady=15)
clear_button=Button(root, text="clear", command=clear, width=10)
clear_button.grid(row=2, column=1)

root.mainloop()