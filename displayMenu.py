#time is used to make the program feel more natural
import time
#HelpObject is our local class created for this assignment
import helpObject

def main():
    while True:
        try:
            with open('help.txt', 'r') as helpfile:
                the_help = helpfile.read() #TODO add regex or something to determine where os_help starts and stops
                os_help_inst = helpObject.HelpObject(the_help[0:20], the_help[20:40], the_help[40:60]) 
                sys_help_inst = helpObject.HelpObject(the_help[60:100], the_help[100:140], the_help[140:180])
                user_choice = displayMenu()
                if user_choice == 'os':
                    displaySelection(os_help_inst)
                elif user_choice == 'sys':
                    displaySelection(sys_help_inst)
                else:
                    print("Goodbye")
                break
        except FileNotFoundError:
            print("""There is no help.txt, please delete this package and redownload from the repo:
                     https://github.com/STUPID-AF-CAT/IDF_Python_Project.git""")
            break
    
    


def displayMenu():

    valid_choice = ['os', 'sys']

    print("Welcome to the Python Library Help System, please\nchoose one of the following libraries (q to quit):")
    
    #keep user in while loop until they make a valid selection
    while True:
        try:
            
            #ask user for input at beginning of loop
            user_choice = input("os, sys\n>").lower()
            
            if user_choice in valid_choice:
                print("Taking you to the", user_choice, "help page!")
               
                #using time.sleep gives user time to read validation message
                time.sleep(1)
                return user_choice
            elif user_choice == 'q':
                break
            else:
                continue
        except ValueError:
            print("You entered something weird.")

def displaySelection(hc):
    print(hc.getDesc())
    print(hc.getEx1())
    print(hc.getEx2())

main()