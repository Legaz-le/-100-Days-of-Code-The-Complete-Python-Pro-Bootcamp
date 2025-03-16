from tkinter import *

window = Tk()
window.title("Mile to Km Convertor")
window.minsize(width= 150, height= 100)
def calculater ():
    miles = float(convertor.get())
    km = miles * 1.609
    number.config(text=f"{km}")


convertor = Entry(width= 10)
convertor.grid(column=1, row= 0)

label = Label(text="Miles")
label.grid(column=2, row= 0)
label.config(padx=10,pady=10)
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0,row=1)
is_equal_to.config(padx=5,pady=0)
number = Label(text= "0")
number.grid(column=1,row=1)
km = Label(text="Km")
km.grid(column=2,row=1)

button =Button(text="Calculate", command=calculater)
button.grid(column=1,row=2)












window.mainloop()