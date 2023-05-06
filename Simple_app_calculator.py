#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 5
#Create a Simple App Calculator 1.  The application will ask the user to choose one of the  four math operations (Addition, Subtraction, Multiplication and Division)
#2.  The application will ask the user for two numbers 3.  Display the result 4. The application will ask if the user wants to try again or not.
#5. If yes, repeat Step 1. 6. If no, Display “Thank you!” and the program will exit 7. Use Python Function and appropriate Exceptions to capture errors during runtime.

#Imports necessary elements
import tkinter as tkinter
from tkinter import messagebox
#Creates Method For Calculator
def calculate():
# Displaying options for operation
    operation_label.config(text="Choose an operation:")
    operation_options.config(text="1-Addition \n2-Subtraction \n3-Multiplication \n4-Division")
    #Gets User Input For Operation
    while True:
        try:
            operation = int(operation_entry.get())
            #If Invalid input, shows error message and prompts user to enter again
            if operation > 4 or operation < 1:
                raise ValueError
            break
        except ValueError:
            return messagebox.showerror("Error on Chosen Operation", "Invalid Input, Please Choose a Number Between 1-4 For the Operation")
    # Asking for the first number
    while True:
        try:
            num1 = float(num1_entry.get())
            #If Invalid input, shows error message and prompts user to enter again
            if not isinstance(num1, float):
                raise ValueError
            break
        except ValueError:
            return messagebox.showerror("Error on First Number Entry", "Invalid Input, Please Enter a Number")
    # Asking for the second number
    while True:
        try:
            num2 = float(num2_entry.get())
            #If Invalid input, shows error message and prompts user to enter again
            if not isinstance(num2, float):
                raise ValueError
            break
        except ValueError:
            return messagebox.showerror("Error on Second Number Entry", "Invalid Input, Please Enter a Number")
     # Performing the addition operation 
    if operation == 1:
        result = num1 + num2
        result_label.config(text="Result: " + str(result))
    # Performing the subtraction operation 
    elif operation == 2:
        result = num1 - num2
        result_label.config(text="Result: " + str(result))
    # Performing the multiplication operation 
    elif operation == 3:
        result = num1 * num2
        result_label.config(text="Result: " + str(result))
    # Performing the division operation 
    elif operation == 4:
            result = num1 / num2
            result_label.config(text="Result: " + str(result))
# Asking user if they want to try again or not
    choice = messagebox.askyesno("Try again?", "Do you want to try again?")
    #Creates a pop-up Thank you message and closes the program
    if not choice:
        messagebox.showinfo("Thank you message", "Thank you!")
        window.destroy()

# Create the GUI