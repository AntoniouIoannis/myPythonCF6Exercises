import re

queue = []  
num = 0

def in_queue(queue, item):
    queue.append(item)

def out_queue(queue):
    if queue:
        return queue.pop(0)  # Αφαιρεί το πρώτο στοιχείο
    else:
        print("Queue is empty!")
        return None

def print_queue_menu():
    print("1. Insert to END of Queue!")
    print("2. Get from FRONT of Queue!")
    print("q/Q for Quit!")

def get_choice():
    return input("Please provide a choice: ")

def main():
    while True:
        print_menu()
        choice = get_choice()

        if not choice:
            continue

        if choice == "q" or choice == "Q":   #  ή if choice.lower() == "q": 
            break

        pattern = r'^\d$'
        match = re.match(pattern, choice)

        if not match:
            print("Error in choice!")
            continue

        choice = int(choice)
        if choice == 1:
            num = input("Please insert a number: ")
            pattern = r'^\d+$'  
            match = re.match(pattern, num)

            if not match:
                print("Error in number.")
                continue

            num = int(num)
            in_queue(queue, num)
            print("Inserted in queue at the end: ", num)
        elif choice == 2:
            out_num = out_queue(queue)
            if out_num is not None:
                print("You got from the front of the queue the item: ",  out_num)
        else:
            print("Μη εγκυρη επιλογη!")

