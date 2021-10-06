# Introduction and directions printed out
print('Welcome to Brian\'s tip calculator!!  You can use this tool to calculate how much each person in your party\
should pay for a restauarnt bill. \n In order to use this calculator correctly, you must enter positive numbers \
for the cost of food and number of people splitting the bill.\n  The percent tip should be greater than or\
equal to 0 as you can choose to give no tip.')
print()

# Getting user input for Cost of Food
food_cost = input('What was the bill for your meal (Not including tax?) ')
print()

# Getting user input for the number of people splitting the bill
number_of_people = int(input('How many people are going to split the bill? '))
print()

# Getting user input for the tip percentage
tip_percentage = input('What percent tip would you like to give? ')
print()

# Function to determine if any of the input is an invalid entry e.g. contains an alphabetic entry. Research was conducted and I found this site that helped me figure this out: https://note.nkmk.me/en/python-str-num-determine/

def is_num(user_input):
    try:
        float(user_input)
    except ValueError:
        return False
    else:
        return True

# Function to convert input into a float
def convert_float(input):
    return float(input)

# Function that runs tip calculator as long as user input is above or equal to 0
def run_calculator():
    if food_cost > 0 and number_of_people > 0 and tip_percentage >= 0:
        # Calculating the cost of the food with a 10% tax
        tax_total = (food_cost * 1.10)
        # Calculate tip
        tip = food_cost * (tip_percentage/100)
        # Calculating the entire bill including user entered tip
        total_bill = (tax_total + tip)
        # Calculating how much the bill should be per person
        bill_per_person = (total_bill / number_of_people)
        # Printing the results of the tip calculation
        print(f'For the cost of your meal ${round(food_cost, 2)} with a 10% tax, your bill before tip is ${round(tax_total, 2)}.')
        print()
        print(f'The total bill including a {round(tip_percentage, 2)}% tip will be ${round(total_bill, 2)}')
        print()
        print(f'For your total bill of ${round(total_bill, 2)}, and splitting your bill {number_of_people} ways, you should each pay ${round(bill_per_person,2)}.')
    #  Else statement saying user under a value which makes no sense for a tip calculator.  Your bill must be a value greater \ than 0, your tip a value greater or equal to 0 and 1 or more people need to be splitting the bill
    else:
        print('You entered a value less than or equal 0 which makes no sense calculating when calculating a bill!')


# Checking to see if all user input are numbers and not letters which can't be used in a tip calculator
if is_num(food_cost) and is_num(number_of_people) and is_num(tip_percentage):
    food_cost = convert_float(food_cost)
    tip_percentage = convert_float(tip_percentage)
    run_calculator()
else:   
    print('You entered an invalid value for one of the questions.')