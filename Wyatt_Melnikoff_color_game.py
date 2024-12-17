import random
#define colored text is formatted in code that takes in text and a color name.
def colored_text(text, color_name):
#create a dictionary of "colors"
    colors = {
#insert ansi escape code for black
        'black': "\033[0;30m",
#insert ansi escape code for red 
        'red': "\033[0;31m",
#insert ansi escape code for green 
        'green':"\033[0;32m",
#insert ansi escape code for yellow
        'yellow':"\033[1;33m",
#insert ansi escape code for blue 
        'blue': "\033[0;34m",
#insert ansi escape code for purple
        'purple': "\033[0;35m",
#insert ansi escape code for cyan 
        'cyan' :  "\033[0;36m",
#insert ansi escape code for white
        'white' : "\033[1;37m",
#insert ansi escape code for reset to black 
        'reset' : "\033[0;30m"
    }
#Get the ansi color code for the given color, default back to white if the color is not found. Display message text with the given color, followed by the reset code to ensave no color leaks 
    print(colors[color_name] + text + "\033[0m") 
#set variable name equal to the input of the question what is your name?
name = input("what is your name?")
#Display message hello, name, the goal of this game is to type the color of the text written, not the text itself.
print(f"hello {name}, the goal of this game is to type the color of the text written, not the text itself")
#created a list including black, red, green, yellow, blue, magenta, cyan, and white 
color_list = ["black","red","green","yellow","blue","magenta","cyan","white"]
#set correct correct round to 0.
correct = 0
#set round to 0.
rounds = 0
#forever loop
while True:
#set variable text color equal to random choice in color lists.
    text_color = random.choice(color_list)
#set variable print color equal to random choice in color list.
    print_color = random.choice(color_list)
#use the function above to text the color and display message color.
    colored_text(text_color, print_color)
#set variable user color equal to the input of quick enter the color of the text.
    user_color=input("quick enter the color of the text")
#if variable user color equals to the variable of print color 

    if user_color==print_color:
#display message you got it 
        print ("you got it")
#add one point to correct rounds.
        correct+=1
#else 
    else:
#display message wrong. 
        print ("wrong")
#add one point to rounds. 
    rounds+=1
#set variable play again equal to would you like to play again? Yes or No.

    play_again=input(f"you have {correct} out of {rounds}.. would you like to play again? yes or no")
#if play again is no 

    if play_again=='no':
#display message exit code 
        print ("exit code")
#exit forever loop
        break



