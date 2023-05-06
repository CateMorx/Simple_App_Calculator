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
#If Invalid input, shows error message and prompts user to enter again
# Asking for the second number
# Performing the calculations
# Asking user if they want to try again or not
#Prints Thank you and closes the program 
# Create the GUI