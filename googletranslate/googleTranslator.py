'''
https://www.youtube.com/watch?v=teum0lI8Efs&t=1266s
'''

from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator
import textblob


root=Tk()
root.title("Google Translator")
root.geometry("1080x400")

# icons
image_icon=PhotoImage(file="Google_Translate_Icon.png")
root.iconphoto(False, image_icon)

language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("English")


root.configure(bg="white")
root.mainloop()
