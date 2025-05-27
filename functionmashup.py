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
def is_integer(number):
    '''
    Takes any parameter and returns a boolean based on if it is an integer
    Args:
        number (any): what we are checking
    Returns:
        boolean: True if the number is an integer
    '''
    try:
        int(number)
        return True
    except ValueError:
        return False
def get_integers():
    '''
     Uses get_integers and prints a random number between the two given integers. 
     Args:
        none 
    Returns:
        random integer
     '''
    while True:
        a = input('Enter your first number: ')
        b = input('Enter your second number: ')
    
        if is_integer(a) and is_integer(b):
            return int(a), int(b)
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
    
def main():
    numbers = [1,2,3,4]
    colors = ['Purple', 'red','white']
    sing() 
    add(4, 12) 
    print_list(numbers)
    print(in_list(colors, '1'))  
    print(in_list(numbers, 1))  
    print(is_integer(5))
    print(is_integer('hello'))
    a, b = get_integers()
    add(a, b)
    get_random()
    sentence = input ('enter the text you would like to check for vowels: ')
    print (count_vowels(sentence))
main()  