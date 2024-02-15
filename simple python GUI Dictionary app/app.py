from nltk.corpus import wordnet
from tkinter import *
from tkinter import scrolledtext
# import nltk
# nltk.download('wordnet')
def define():
    userinput=userbox.get()
    word=wordnet.synsets(userinput)
    finalmeaning=[wd.definition() for wd in word]
    if finalmeaning==[]:
        output.delete('1.0', END)
        output.insert(END,"NOT FOUND, TRY ANOTHER WORD" )
    else:
        output.delete('1.0', END)
        output.insert(END,finalmeaning)

mw= Tk()
mw.title('Dictionary')
mw.geometry('700x500')
# mw.iconbitmap('images/icon.ico')

userbox=Entry(mw, width=35)  # create a widget
userbox.grid(row=1,column=1,pady=6)   # attach to screen

btn=Button(mw, text='search', relief='groove', width=14, font=('arial',10), command=define)
btn.grid(row=1, column=2, pady=6)

output= scrolledtext.ScrolledText(mw)
output.grid(row=2,column=1, columnspan=2, pady=6, padx=10)
mw.mainloop()

