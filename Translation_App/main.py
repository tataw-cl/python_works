from tkinter import *
#import textblob
from tkinter import ttk, messagebox
root=Tk()
root.title('Tataw translator')
#root.iconbitmap
root.geometry("800x300")
def Translation():
    pass

#text boxes
original_text=Text(root, height=10, width=35)
original_text.grid(row=0, column=0, padx=8, pady=8)

translated_text=Text(root, height=10, width=35)
translated_text.grid(row=0, column=2,padx=8, pady=8)
translate_button=Button(root, text="Translate", font=("Helvetica", 24), command=Translation)
translate_button.grid(row=0, column=1, padx=8)

#ComboBoxes
original_Combobox=ttk.Combobox(root, width=50,)
original_Combobox.current(5)
original_Combobox.grid(row=1, column=0)

translated_Combobox=ttk.Combobox(root, width=50,)
translated_Combobox.current(5)
translated_Combobox.grid(row=2, column=2)

root.mainloop()