from tkinter import *

def button_click():
    print("I got clicked")
    my_label["text"] = input.get()

window = Tk()
window.title("GUI program")
window.minsize(width = 500, height = 300)
window.config(padx=100, pady=200)

#Label


my_label = Label(text = "I Am a Label", font=("Arial",24, "bold"))
my_label.config (text ="New text")
my_label.grid(column=0, row=0)

#Button

button = Button(text="Click me", command = button_click)
button.grid(column = 1, row = 1)

second_button = Button(text="new button")
second_button.grid(column = 2, row = 0)



#Entry

input = Entry(width = 10)
print(input.get())
input.grid(column = 3, row= 2)






window.mainloop()