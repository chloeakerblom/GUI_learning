import tkinter
root = tkinter.Tk()

root.title("Hello World!")
root.geometry("600x600")

my_label = tkinter.Label(root)
my_label.config(text="Hello!", fg="teal", bg="gold", font=("Stencil","40"), padx="5", bd="40")
my_label.grid()

my_label = tkinter.Label(root)
my_label.config(text="Hello!", fg="pink", bg="black", font=("Stencil","40"), padx="5", bd="40")
my_label.grid()

my_label = tkinter.Label(root)
my_label.config(text="Hello!", fg="purple", bg="orange", font=("Stencil","40"), padx="5", bd="40")
my_label.grid()

my_label = tkinter.Label(root)
my_label.config(text="Hello!", fg="white", bg="green", font=("Stencil","40"), padx="5", bd="40")
my_label.grid()


root.mainloop()