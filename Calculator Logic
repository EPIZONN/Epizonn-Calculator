class Calculator:
    #A class is used so that we do not have to use a global statement in each function

    calculation = ""

    @classmethod
    def update(self):
        #Update the display of the calculator
        
        Display.configure(text=self.calculation)

    @classmethod
    def add_character(self, character, empty=None):
        
        self.calculation += character
        self.update()

    @classmethod
    def brackets(self, empty=None):
        #Add brackets. This is optional
        
        if self.calculation.count("(") == self.calculation.count(")") + 1:
            self.calculation += ")"
        else:
            self.calculation += "("
        self.update()

    @classmethod
    def backspace(self, empty=None):
        #Remove the characters one at a time
        
        self.calculation = self.calculation[:-1]
        self.update()

    @classmethod
    def clear(self, empty=None):
        #Clear all the characters displayed in the calculator
        
        self.calculation = ""
        self.update()

    @classmethod
    def equal(self, empty=None):
        #Evaluate the answer to the calculation.
        #If the answer is larger than 57 digits, it is saved to a results file
        #Any trailing .0 is removed from simple divisions
        
        try:
            if self.calculation == "":
                return
            self.calculation = str(eval(self.calculation))
            
            if self.calculation.endswith(".0"):
                self.calculation = self.calculation[:-2]
                
            if len(self.calculation) > 57:
                saved = open("memory.txt", "a+")
                saved.write(self.calculation + "\n \n")
                self.clear()
                messagebox.showinfo("Saved Result!", "The result was saved in 'memory.txt' and the"
                                                    " calculator display was cleared.")
                                                    
                saved.close()
            self.update()
            
        except ZeroDivisionError:
            messagebox.showerror("Zero Division Error", "Undefined.")
        except SyntaxError:
            messagebox.showerror("Error", "You're input was wrong.")
        except OverflowError:
            messagebox.showerror("Overflow Error", "That value was too small.")
        except TypeError:
            messagebox.showerror("Type Error", "We don't do algebra here.")

    @classmethod
    def decimal(self, empty=None):
        #Add a decimal point.
        
        if self.calculation[:-1] != ".":
            self.calculation += "."
            self.update()

    @classmethod
    def c(self, empty=None):
        #Copy the current value to the clipboard.
        copy(self.calculation)

    @classmethod
    def v(self, empty=None):
        #Paste the clipboard to the display.
        
        for digit in paste():
            if digit not in ["1", "2", "3", "4", "5", "6", "7", "8",
                           "9", "0", "/", "(", ")", "*", ".", "-", "+"]:
                messagebox.showerror("Error",
                                     "The clipboard does not only contain numbers.")
                return
        self.calculation += paste()
        self.update()
