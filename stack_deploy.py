
import re

stack = []
num = 0

def push(list, item):
   list.append(item)
   
def pop(list):
    if list:
        return list.pop()
    else:
        print("Stack is empty!")
     
        
def print_menu():
    print("1. Insert to TOP!")
    print("2. Get from TOP!")
    print("q/Q for Quit!")
    
def get_choice():
    return ("please provide a choice: ")

def main():
    choice, num, out_num = 0
    
    
    
    while True:
        print_menu()
        choice = get_choice()
        
        if not choice:
            continue
                
        if choice == "q" or choice == "Q":
            break
        
        pattern = r'^\d$'
        match = re.match(pattern, choice)
        
        if not match:
            print("Error in choice!")
            continue
        
            choice = int(choice)
            match choice:
                case 1:
                    num = input("Please insert a number: ")
                    pattern = r'^\d$'
                    match = re.match(pattern, num)
                    
                    if not match:
                        print("Error in number.")
                        continue
                        
                    num = int(num)
                    push(stack, num)
                    print("Inserted in stack at the top.")
                case 2:
                    out_num = pop(stack)
                    print("You got out of the stack the item: ", out_num)
                case _:
                    print("Μη εγκυρη επιλογη")
                    

