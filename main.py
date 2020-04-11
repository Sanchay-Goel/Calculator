import tkinter
from tkinter import *

window = Tk()

window.title("Calculator")
window.geometry("312x324")
window.resizable(0, 0)

expression = ""
input_text = StringVar()

input_frame = Frame(window, width=312, height=50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable = input_text, width = 50, bg = "#eee", bd = 0, justify = RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady = 10)

#creating frame for the buttons
btns_frame = Frame(width=312, height=250, bg="grey")
btns_frame.pack()

#creating first row
clear = Button(btns_frame, text="C", fg="black", width=32, height=3, bg="#eee", cursor="hand2")
clear.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bg="#eee", cursor="hand2")
divide.grid(row=0, column=3, padx=1, pady=1)

#creating second row
seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bg="#eee", cursor="hand2").grid(row=1, column=0, padx=1, pady=1)
eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bg="#eee", cursor="hand2").grid(row=1, column=1, padx=1, pady=1)
nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bg="#eee", cursor="hand2").grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btns_frame, text="x", fg="black", width=10, height=3, bg="#eee", cursor="hand2").grid(row=1, column=3, padx=1, pady=1)

#creating third row
four = Button(btns_frame, text="4", fg="black", width=10, height=3, bg="#eee", cursor="hand2").grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text="5", fg="black", width=10, height=3, bg="#eee", cursor="hand2").grid(row=2, column=1, padx=1, pady=1)
six = Button(btns_frame, text="6", fg="black", width=10, height=3, bg="#eee", cursor="hand2").grid(row=2, column=2, padx=1, pady=1)
minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bg="#eee", cursor="hand2").grid(row=2, column=3, padx=1, pady=1)

#creating fourth row
one = Button(btns_frame, text="1", fg="black", width=10, height=3, bg="#eee", cursor="hand2").grid(row=3, column=0, padx=1, pady=1)
two = Button(btns_frame, text="2", fg="black", width=10, height=3, bg="#eee", cursor="hand2").grid(row=3, column=1, padx=1, pady=1)
three = Button(btns_frame, text="3", fg="black", width=10, height=3, bg="#eee", cursor="hand2").grid(row=3, column=2, padx=1, pady=1)
plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bg="#eee", cursor="hand2").grid(row=3, column=3, padx=1, pady=1)

#creating fifth row
zero = Button(btns_frame, text="0", fg="black", width=10, height=3, bg="#eee", cursor="hand2").grid(row=4, column=0, padx=1, pady=1)
dot = Button(btns_frame, text=".", fg="black", width=10, height=3, bg="#eee", cursor="hand2").grid(row=4, column=1, padx=1, pady=1)
equal = Button(btns_frame, text="=", fg="black", width=20, height=3, bg="#eee", cursor="hand2").grid(row=4, columnspan=2, column=2, padx=1, pady=1)






