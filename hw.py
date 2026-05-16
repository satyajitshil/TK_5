from tkinter import *

tk = Tk()
tk.geometry("800x800")
tk.title("Denomination Calculator")
tk.configure(bg= "light blue")

label1 = Label(tk, text="Enter a password", bg = "light blue")
entry = Entry()

def msg():
    mseg = entry.get()
    length = len(str(mseg))
    if length >= 8:
        message = "Strong Password\n"
    else:
        message = "Weak Password\n"
    
    text_box.insert(END, message)

text_box = Text(bg="#1d75f5",fg="#ffffff",height=10,width=50)
btn = Button(text="Calculate",command=msg, bg="#1d75f5",fg="#000000" )


label1.place(x=20,y=20)
entry.place(x=150,y=20)
btn.place(x=150,y=200)
text_box.place(x=20,y=240)


mainloop()
