from subprocess import Popen, PIPE # Used for the copying process
import functools # Used for division and subtraction functions
from math import sqrt # Used for the Square_Root function



###################################################
# Calculator program                              #  
# Cody Tapp                                       #
# CIT 432                                         #
# Western Kentucky University                     #
#                                                 #
#CHECK OUT MY PORTFOLIO @ CODYJTAPP.WORDPRESS.COM #
###################################################

def main():
    title_screen() # Just a typical title screen, will only play on initial start of program
    menu_item = menu_selection() # menu_selection ask for user to input an operator symbol. Returned variable is assigned to variable in main function 
    process_menu_item(menu_item) #The next function call processes menu item to determine which mathetmatical calculation will take place
    exit_program() # When exit string is input from while loop in process_menu_item function, exit_program will process and close out the program.

    

def title_screen():
    print("**********************************")
    print("* Cody Tapp's Calculator Program *")
    print("**********************************\n\n")
    

def menu_selection(): # Displays a list of options, a variable is assigned to user input as a string and returned to main to be processed by next function
    print("Select one of the following:\n'+' for addition\n'-' for subtraction\n'*' for multiplication\n'/' for division\n'sqrt' for square root\n'exit' to close\n")
    print("NOTE: If you would like to add and subtract within the same set of calculations type '+'.")
    menu_operator = str(input())
    return menu_operator

def process_menu_item(menu_operation): # Processes the menu item from main and determines what calculations are to be made
    while menu_operation != "exit": # The program will keep running until the user enters exit, where the program will return to main and run the terminating function.            
        if menu_operation in ("+", "-", "*", "/", "sqrt", "Sqrt", "SQRT"): # If operator or sqrt is applied, proper functions are called
            solution = number_list(menu_operation) # Menu operation is sent to number_list function to determine menu display and how calculations are made.
        else: # If operator is not applied, program throws error and plays back from beginning 
            print("*******************************************")
            print("* ERROR! INVALID OPERATION!               *")
            print("*******************************************\n\n\n\n\n")
            main()
            
        print("******************************") # This set of print statements confirms the total that was calculated
        print(solution)
        print("******************************")
        print("\n\n\n\n")
        
        menu_operation = menu_selection() # Replays the initial menu so user can select next operation.
    

def number_list(operator_item): # Creates a list of numbers, after calculation, list is returned to main to be assigned to list_of_numbers variable.
    number_list = []
    counter = 1 # Starts at one to prevent DivideByZero and logic errors with division and multiplication
    if operator_item == "+": # operator_item determines list of calculations to be made
        print("Negative values can be used for subtracting from the sum.\n")
    elif operator_item == "-":
        print("Using negative values will add to the total instead of subtracting")
    elif operator_item == "*":
        print("Negative values can be used for calculating the product")
    elif operator_item == "/":
        print("Negative values can be used for calculating the quotient")
        print("!!!!WARNING: Do not divide by zero!!!!")
            
    else: # Used for square root, warns user that negative values cannot be calculated, if calculated, the square_root function will throw an error.
        print("!!!!Negative values ARE NOT ALLOWED for calculating square root!!!!\n!!!!Imaginary numbers go beyond the scope of the program's capabilities!!!!")
        print("Please enter a positive value")
    print("Press Ctrl+V to use previous solution in calculation. \nEnter starting value and press enter. Enter one value at a time and press enter. Type '=' and enter or double tap enter to return to menu\n")

    
    while number_list != "=": # Calculations are entered until the user types the equal sign, then the answer is returned to main
        try:
            list_value = float(input())
        except ValueError: # Created an exception to break out of the loop. Typing "=" will copy the current total to the clipboard
            sentinel_value = input("Press '=' or 'Enter' again to complete calculation and copy answer to system clipboard.\n\n") 
            if sentinel_value in ("=", ''): # Exception handles "=" to break loop, copys total and returns it to process_menu_item function
                return running_total
            else: # An error is only thrown if any other key is input besides "="
                print("*******************************************")
                print("* ERROR! INVALID OPERATION!               *")
                print("*******************************************\n\n\n\n\n")
                main()                
                
        number_list.append(list_value) # Each number that is input from user will be added to list 
        
        # Menu item determines calculation and output
        if operator_item == "+":
            running_total = addition(number_list) 
            if counter == 1: # 
                print("Starting value:", running_total) # The first number that is entered in a set of calculation is labeled starting value
            else:
                print("Current sum:", running_total) 

        elif operator_item == "-":
            running_total = subtraction(number_list)
            if counter == 1:
                print("Starting value:", running_total)
            else:
                print("Current difference:", running_total)

        elif operator_item == "*":
            running_total = multiplication(number_list)
            copy(running_total)
            if counter == 1:
                print("Starting value:", running_total)
            else:
                running_total = multiplication(number_list)
                print("Current product:", running_total)

        elif operator_item == "/":
            running_total = division(number_list)
            if counter == 1:
                print("Starting value:", running_total)
            else:
                running_total = division(number_list)
                print("Current quotient:", running_total)

        elif operator_item in ("sqrt", "Sqrt", "SQRT"):
            running_total = square_root(number_list)
            copy(running_total)
            print("Square root: ", running_total)
            print("Enter another value if needed")

        counter += 1
         

def addition(number_array): 
    total_sum = sum(number_array)
    copy(total_sum)
    return total_sum

def subtraction(number_array):
    # Created lambda function to subtract previous total from current input. functools.reduce displays the current value of the array (current total)
    total_difference = functools.reduce(lambda current_element, previous_element: current_element - previous_element, number_array)
    copy(total_difference)
    return total_difference

def multiplication(number_array): 
    total_product = 1 # This is not 0 because if it were, every product would come out to 0. 
    for count in range(0, len(number_array)): # Product results are calculating with a for loop
        total_product *= number_array[count]
    return total_product

def division(number_array): # Similar format to subtraction function, except '/' instead of '-'
    
    total_quotient = functools.reduce(lambda current_element, previous_element: current_element / previous_element, number_array)
    copy(total_quotient)
    return total_quotient
    
 
def square_root(number_array): # Similar format to multiplication. If less than 0, imaginary number error is thrown
    for count in range(0, len(number_array)):
        if number_array[count] >= 0:
            total = sqrt(number_array[count])
        else:
            print("*******************************************")
            print("* ERROR! SOLUTION IS AN IMAGINARY NUMBER! *")
            print("*******************************************\n\n\n\n\n")     
            main()
    return total
 
def copy(solution_answer): # Function attaches value in result to system clipboard, prints a confirmation. 
    print("******************************")
    print("*", solution_answer)
    print("******************************")
    Popen(["clip"], stdin=PIPE).communicate(str(solution_answer).encode())
    print("\n\n\n\n", solution_answer,"has been copied to your clipboard") # Used only for confirmation to ensure copy function runs
    
def exit_program(): 
    print("Closing calculator . . .")
    exit()
    
main()
