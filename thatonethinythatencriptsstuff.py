from tkinter import *

root=Tk()

root.title("Encripter")
root.geometry("400x400")
root.configure(background = 'snow')

entered_word = Entry(root)
entered_word.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label = Label(root, text = "ASCII number: ", bg = 'light yellow', fg = 'black')
label2 = Label(root, text = "Encripted Name: ", bg = 'light yellow', fg = 'black')

def turnintoascii():
    label["text"] = "ASCII number: "
    label2["text"] = "Encripted Name: "
    
    iw = entered_word.get()
    
    for letter in iw :
        label["text"] += str(ord(letter)) + " "
        asciii=int(ord(letter))
        enc = asciii-1
        label2["text"] += str(chr(enc))
btn = Button(root, text = 'Display as Encripted Name', command=turnintoascii, bg='gold', fg = 'black')
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

label.place(relx = 0.5, rely = 0.6, anchor = CENTER)
label2.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()