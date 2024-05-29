#!/usr/bin/env python
# coding: utf-8

# In[12]:


import time
from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def Translate():
    try:
        # Translation function
        start_time = time.time()  # Start time for performance evaluation
        translator = Translator()
        translated = translator.translate(text=Input_text.get(), dest=dest_lang.get())
        output_text.delete(1.0, END)
        output_text.insert(END, translated.text)
        
        end_time = time.time()  # End time for performance evaluation
        translation_time = end_time - start_time
        translation_time_label.config(text=f"Translation Time: {translation_time:.2f} seconds")
        
        lang = translator.detect(Input_text.get())
        lang_print.config(text=f"language detected: {lang}")
    except Exception as e:
        # Error handling
        print("Error occurred during translation:")
        print(traceback.format_exc())
        output_text.delete(1.0, END)
        output_text.insert(END, "Error occurred. Please try again later.")

# GUI setup
root = Tk()
root.geometry("1100x350")
root.resizable(0, 0)
root['bg'] = 'skyblue'
root.title("Language Translator by DS75")

Label(root, text=" Language Translator ", font="Arial 20 bold", foreground="red").place(relx=0.5, rely=0.1, anchor=CENTER)

Label(root, text=" Enter Text ", font="Arial 14 bold", bg='white smoke').place(x=150, y=60)
Input_text = Entry(root, width=60)
Input_text.place(x=50, y=100)

Label(root, text=" Output ", font="Arial 14 bold", bg='white smoke').place(x=780, y=60)
output_text = Text(root, font='Arial 12', height=4, wrap=WORD, padx=5, pady=5, width=40)
output_text.place(x=650, y=100)

languages = list(LANGUAGES.values())
dest_lang = ttk.Combobox(root, values=languages, width=30)
dest_lang.place(x=130, y=130)
dest_lang.set("Choose language")

trans_btn = Button(root, text='Translate', font='Arial 12 bold', pady=6, command=Translate, bg='orange', activebackground='green')
trans_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

lang_print = Label(root, text="language detected: ", font="Arial 12 bold", bg='skyblue')
lang_print.place(relx=0.5, rely=0.8, anchor=CENTER)

translation_time_label = Label(root, text="Translation Time: ", font="Arial 12 bold", bg='skyblue')
translation_time_label.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()


# In[ ]:




