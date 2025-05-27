'''
Assignmentn name: Function Matchup
Authors Name: Wyatt Melnikoff
Date of Creation: 5/5/25
Discription: Describing Many diffrent functions that you can pick from that do diffrent tasks.
Bugs: none
Challenges: Improve the efficiency of funtions 5 and 6, Make my own function, and Make a random name generator function.
Sources: None 
'''

import random

def chorus ():
    '''
    Prints the chorus of a song
    Args:
        None 
    Returns:
        print: Chorus 
    '''
    print('''Let it be let it be let it be let it be
whispher words of wisdom let it be
    ''')
def sing ():
    '''
    Uses the previous function to sing a song
    Args:
        None 
    Returns:
        print: entire song 
    '''
    
    print('''
When I find myself in times of trouble, Mother Mary comes to me
Speaking words of wisdom, let it be
And in my hour of darkness she is standing right in front of me
Speaking words of wisdom, let it be
          ''')
    chorus()
    print('''
And when the broken hearted people living in the world agree
There will be an answer, let it be
For though they may be parted, there is still a chance that they will see
There will be an answer, let it be

Let it be, let it be, let it be, let it be
There will be an answer, let it be
          ''')
    chorus()
    chorus()
    print('''
And when the night is cloudy there is still a light that shines on me
Shinin' until tomorrow, let it be
I wake up to the sound of music, Mother Mary comes to me
Speaking words of wisdom, let it be
          ''')
    chorus()
    chorus()
def add(x, y):
    '''
    Takes two numbers and prints their sum
    Args:
        x (int): first number
        y (int): second number
    Returns:
        print: sum of the two numbers
    '''
    print(x + y)
def print_list(array):
    '''
    Takes a list and prints every element in that list individually (vertically)
    Args:
        array (list):
    Returns:
        print each element in the list vertically
    '''
    for element in array:
        print(element)
def in_list(array,element):
    '''
    Takes a list and element and returns a boolean based on if the element is in the list
    Args:
        array, element
    Returns:
        element in array 
    '''
    return element in array
def get_integer():
    '''
    Uses user input to get an integer
    Args:
        None
    Returns:
        int: num given by user
    '''
    while True:
        try:
            num = int(input("enter your first number:"))
            return num
        except ValueError:
            print("Invalid response, Please enter number")
def get_integers():
    '''
     Uses user input to get two integers
     Args:
        none 
    Returns:
        random integer
     '''
    a = get_integer()
    b = get_integer()
    return a, b
def get_random ():
    '''
     Asks the user for two numbers, uses is_integer to check input, returns the two integers
     Args:
        none 
    Returns:
        two integers
     '''
    a, b = get_integers()
    print(random.randint(a, b))
def count_vowels(sentence):
    '''
      Takes a string and returns the number of vowels in it 
     Args:
        none 
    Returns:
        the number of vowels in a sentence 
     '''
    num_vowels = 0

    for character in sentence: 
        if character in ['a', 'e','i','o','u']:
            num_vowels +=1
    return num_vowels
def name_generator():
    '''
    name generator that randomly picks names out of a list 
    Arg:
      none 
    Returns:
      random first name and last name from the list 
    '''
    return random.choice(["Wyatt","Jack","Miles","Charlie","Deven"]) + ' ' + random.choice(["Brown","Stern","Darwin","Stud"])
def get_initials(name):
    words = name.split ()
    initials = ""
    for words in words:
        return initials 
def subtract(x,y):
    '''
    subtracts two integers together
    Args:
        x (int): first number
        y (int): second number
    Returns:
        print: difference of the two numbers
    '''
    print (x-y)

def multiply (x,y):
    '''
    multiplies two integers together 
    Args:
        none
    Returns:
        the total number from the multiplication problem 
    '''
    print(x*y)
def divide (x,y):
    '''
    divides two integers together 
    Args:
        x: 
    Returns:
        the total number from the divide problem 
    '''
    print (x/y)
def main():
    numbers = [1,2,3,4]
    colors = ['Purple', 'red','white']
    
    while True:
        option = input ('what would you like to do? 1. Sing a song, 2. Enter calculator, 3. Takes two numbers and prints their sum, 4. Takes a list and element and returns a boolean, 5. Uses user input to get an integer, 6. Uses user input to get two integers, 7. Asks the user for two numbers and returns two integers, 8. Takes a string and returns the number of vowels in it, 9. name generator that randomly picks names out of a list     ')
        
        if option == "1":
            sing() 
        elif option == "2":
            add(4, 12) 
        elif option == "3":
            a, b = get_integers()

            operation = input('What would you like to do? +, -, *, or / ')
            
            if operation == '+':
                add(a, b)
            elif operation == '-':
                subtract(a, b)
            elif operation == '*':
                multiply(a,b)
            elif operation == '/':
                divide(a,b)
        elif option == "4":
            print(in_list(colors, '1'))  
            print(in_list(numbers, 1))  
        elif option == "5":
            print_list(numbers)
        elif option == "6":
            get_random()
        elif option == "7":
            sentence = input ('enter the text you would like to check for vowels: ')
            print (count_vowels(sentence))
        elif option == "8":
            print(name_generator())
main()  