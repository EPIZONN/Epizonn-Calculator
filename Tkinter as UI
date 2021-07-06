ui = Tk()

ui.geometry("300x400")
ui.title("Epizónn Calculator")
ui.resizable(False, False)
ui.configure(bg="black")


Button_Frame = Frame(ui)

# The following buttons can be held down
Num1 = Button(Button_Frame, text="1", font = ("Helvetica", "14"), command=partial(Calculator.add_character, "1"), fg="white",
              bg="gray", width=4, height=2, repeatdelay=150, repeatinterval=150)
              
Num2 = Button(Button_Frame, text="2", font = ("Helvetica", "14"), command=partial(Calculator.add_character, "2"), fg="white",
              bg="gray", width=4, height=2, repeatdelay=150, repeatinterval=150)
              
Num3 = Button(Button_Frame, text="3", font = ("Helvetica", "14"),command=partial(Calculator.add_character, "3"), fg="white",
              bg="gray", width=4, height=2, repeatdelay=150, repeatinterval=150)
              
Num4 = Button(Button_Frame, text="4", font = ("Helvetica", "14"), command=partial(Calculator.add_character, "4"), fg="white",
              bg="gray", width=4, height=2, repeatdelay=150, repeatinterval=150)
              
Num5 = Button(Button_Frame, text="5", font = ("Helvetica", "14"), command=partial(Calculator.add_character, "5"), fg="white",
              bg="gray", width=4, height=2, repeatdelay=150, repeatinterval=150)
              
Num6 = Button(Button_Frame, text="6", font = ("Helvetica", "14"), command=partial(Calculator.add_character, "6"), fg="white",
              bg="gray", width=4, height=2, repeatdelay=150, repeatinterval=150)
              
Num7 = Button(Button_Frame, text="7", font = ("Helvetica", "14"), command=partial(Calculator.add_character, "7"), fg="white",
              bg="gray", width=4, height=2, repeatdelay=150, repeatinterval=150)
              
Num8 = Button(Button_Frame, text="8", font = ("Helvetica", "14"), command=partial(Calculator.add_character, "8"), fg="white",
              bg="gray", width=4, height=2, repeatdelay=150, repeatinterval=150)
              
Num9 = Button(Button_Frame, text="9", font = ("Helvetica", "14"), command=partial(Calculator.add_character, "9"), fg="white",
              bg="gray", width=4, height=2, repeatdelay=150, repeatinterval=150)
              
Num0 = Button(Button_Frame, text="0", font = ("Helvetica", "14"), command=partial(Calculator.add_character, "0"), fg="white",
              bg="gray", width=4, height=2, repeatdelay=150, repeatinterval=150)
              
BACK = Button(Button_Frame, text="Del", font = ("Helvetica", "14"), command=Calculator.backspace, fg="black", bg="gold",
              width=4, height=2, repeatdelay=200, repeatinterval=200)

addition = Button(Button_Frame, text="+", font = ("Helvetica", "14"), command=partial(Calculator.add_character, "+"), fg="white",
              bg="black", width=4, height=2)
              
subtraction = Button(Button_Frame, text="-", font = ("Helvetica", "14"), command=partial(Calculator.add_character, "-"), fg="white",
              bg="black", width=4, height=2)

multiplication = Button(Button_Frame, text="×", font = ("Helvetica", "14"), command=partial(Calculator.add_character, "*"), fg="white",
              bg="black", width=4, height=2)
                         
division = Button(Button_Frame, text="÷", font = ("Helvetica", "14"), command=partial(Calculator.add_character, "/"), fg="white",
              bg="black", width=4, height=2)
              
equals = Button(Button_Frame, text=" = ", font=("Helvetica", "14"), fg="black", bg="red", command=Calculator.equal,
                width=10, height=2)

parenthesis = Button(Button_Frame, text="()", font=("Helvetica", "14"), command=Calculator.brackets,
                         width=4, height=2, fg="white", bg="black")
                         
decimal_button = Button(Button_Frame, text=".", font=("Helvetica", "14"), command=Calculator.decimal, fg="white", bg="gray",
                    width=4, height=2)
                    
all_clear = Button(Button_Frame, text="AC", font=("Helvetica", "14"), command=Calculator.clear, fg="black", bg="gold",
                      width=4, height=2)

all_clear.grid(row=1, column=5)
BACK.grid(row=1, column=4)
parenthesis.grid(row=4, column=3)
Num7.grid(row=1, column=1)
Num8.grid(row=1, column=2)
Num9.grid(row=1, column=3)
Num4.grid(row=2, column=1)
Num5.grid(row=2, column=2)
Num6.grid(row=2, column=3)
Num1.grid(row=3, column=1)
Num2.grid(row=3, column=2)
Num3.grid(row=3, column=3)
Num0.grid(row=4, column=1)
decimal_button.grid(row=4, column=2)
division.grid(row=2, column=5)
multiplication.grid(row=2, column=4)
addition.grid(row=3, column=4)
subtraction.grid(row=3, column=5)
equals.grid(row=4, column=4, columnspan=2)

Display.pack()
Button_Frame.pack()

ui.mainloop()
