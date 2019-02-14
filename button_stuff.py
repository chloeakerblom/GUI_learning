import tkinter
root = tkinter.Tk()

def print_bonjour():
    print("Bonjour")

button1 = tkinter.Button(root)
button1.config(text="Bonjour.", fg="black", bg="pink", font=("Stencil", "50"), command=print_bonjour)
button1.grid()

root.mainloop()