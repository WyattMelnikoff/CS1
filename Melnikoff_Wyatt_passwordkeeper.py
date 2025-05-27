'''
Author: Wyatt Melnikoff
Sources. Mrs. Marciano
Description: Lets a user store data for websites and can be stored in a CSV.
Challenges: Allow the user to retroactively add more usernames and passwords, Allow the user to change usernames and passwords,
Store the list of websites with usernames and passwords in an excel spreadsheet, Require a password to enter the password keeper,
Generate a secure password for the user, and Check how complex/secure the passwords are.
Bugs: none.
'''
import random
import os
import time
import csv

def add_entry(websites, usernames, passwords):
    '''
    Allows the user to store websites with its assigned username and passowrd
    Args:
        wesbites (list)
        usernames (list)
        passwords (list)
    Returns:
        information into list
    '''
    website = input("what website would you like? ")
    username = input("what username would you like to use for your website? ")
    password = input("what password would you like for your website? Enter 'g' to generate ")

    if password.lower() == "g":
        password = generate_password()
    websites.append(website)
    usernames.append(username)
    passwords.append(password)

def print_entry(website, username, password):
    '''
    Allows to the user to print out their website, username, and passwords in the form of a f-string
    Args:
        Website (str)
        username (str)
        passwords (str)
    Return:
        print: website, username, password:
    '''
    print(f"Website: {website}, Username: {username}, Password: {password}")
def get_index(websites):
    '''
  takes in websites as a list and element and returns the index of website within a list
  Args:
    websites (list)
  Returns:
    Website (index)
    print (that is not a website in your list)
    '''
    while True:
        website = input("enter the website:") 
        
        if website in websites:
            return websites.index(website)
        else:
            print("that is not a website in your list")
def change_password(websites, usernames, passwords):
    '''
    Manages passwords across diffrent websites presented by the user
    Args:
        websites (index)
    Returns:
        true if the passowrd is correct or false if it is not
    '''
    index = get_index(websites)
    websites[index] = input("what website would you like? ")
    usernames[index] = input("what username would you like to use for your website? ")
    passwords[index] = input("what password would you like for your website? ")
def enter_password(secret_code, tries):
    '''
    Allows the user to create a password so only them can access their websites, usernames, passwords
    Args:
        secret code
    Returns:
         print('Correct! You are in!') 
         print (f"incorrect password! You have {tries-i-1} tries remaining")
        
        
    '''
    for i in range(tries):                                                          #for I in ranfe tries
        pwd_check = input("type in your password:")                                 #pwd_check equals to the input of type in your password
        
        if pwd_check == secret_code:                                                #display message Correc! you are in!
            print('Correct! You are in!') 
            break                                                                   #exit forveer loop
        else:                                                                       #else
            print (f"incorrect password! You have {tries-i-1} tries remaining")     #display message inccorect! you have number of tries remianing.
    print('Too many tries. You have been banned!')                                  # display message too many tries. You have been banned.
    exit()                                                                          # exit forever loop

def export_entries(filename, headers, *arrays):
    """
    Exports parallel arrays to a CSV file.

    Args:
        filename (str): The name of the CSV file to create.
        headers (list): A list of header names for each column.
        *arrays: Variable number of array arguments (lists or tuples).
               All arrays must have the same length.
    """
    if not arrays:                                                    # if not arrays are provided, raise an error
        raise ValueError("At least one array must be provided.")      #function recieves a arguement for a correct data type and gives the requiremnt at least one array must be provided 
    
    num_rows = len(arrays[0])                                         # num_rows equals to the length of the first array

    for arr in arrays:                                                # for arrays in arrays
        if len(arr) != num_rows:                                      #if len of array equals the num_rows 
            raise ValueError("All arrays must have the same length.") #functon recives the correct data type but gives the requirment all arrays must have the same length.
    
    with open(filename, 'w', newline='') as csvfile:                  #Open a filename and newline for a csv.
        csvwriter = csv.writer(csvfile)                               #Create a CSV writer file.
        csvwriter.writerow(headers)                                   #In the CSV file create headers and rows 

        for i in range(num_rows):                                     # Write each lines of data for the CSV file 
            row = [arr[i] for arr in arrays]                          #collect each infomration in the array and turn it into a row
            csvwriter.writerow(row)                                   #write many rows in the CSV file 
def clear_screen(delay):
    '''
    This clears the code on the console screen
    Args:
        Delay 
    Returns:
        a blank console screen for the user to see
    '''
    time.sleep(delay)
    os.system('cls')

def get_length():
    '''
    when the object is a string it returns the number of character in it
    Args:
        none
    Returns:
        print ("not an integer")
    '''
    try:
        length = int(input('Enter Length:'))
        return ("length")
    except ValueError:
        print ("not an integer")
    

def generate_password():
    '''
    Generates a secure password for the user to use using all the letrer, numbers, and special characters
    Args:
        none 
    Returns
        secure password for the user 
    '''
    length = get_length()
    return ''.join(random.sample(list('abcdefghijklmnopqrstuvwuxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'), length))

def check_security (password, length, display):
    '''
    Checks how secure the users passwords by taking in a number of considerations 
    Args:
        password, length, display 
    Returns:
        print ("is not secure")
        print ("Passwrod is secure")
    '''
    if len(password) < length or password.lower() == password or password.upper() == password or not any(char.isdigit() for char in password) or not any(char in password for char in list('abcdefghijklmnopqrstuvwuxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(')):
        if display:
            print(f'{password} is not secure')
        return False
    else:
        if display:
            print(f'{password} is secure')
        return True

def main():
    websites = []
    usernames = []
    passwords = []

    secret_code = input("Enter your secret code: ")
    clear_screen(1)  
    add_entry(websites, usernames, passwords)
    clear_screen(1)
    enter_password(secret_code)
    clear_screen(1)

    while True:
        option = input('''Which option would you like? Enter 'q' to quit
1. Add an entry
2. Print a specific entry
3. Print all entries
4. Change an entry
5. Export 
6. Generate a secure password
7. Check how secure your password is
        ''')

        if option == "q":
            break 
        elif option == "1":
            add_entry (websites, usernames, passwords)
        elif option == "2":
            index = get_index(websites)
            print_entry(websites[index], usernames[index], passwords[index])
        elif option == "3":
            for index in range(len(websites)):
                print_entry(websites[index], usernames[index], passwords[index])
        elif option == "4":
            change_password (websites, usernames, passwords)
        elif option == "5":
            filename = input('Enter your filename: ')
            export_entries(filename+".csv", ["Websites", "Usernames", "Passwords"], websites, usernames, passwords)
            print(f"Export successful! Your data has been stored in {filename}.csv")
        elif option == "6":
            print(f'Your generated password is {generate_password()}')
        elif option == "7":
            (check_security)
main ()
        

    
            
                

		



	
	
	
	
	
	


	
