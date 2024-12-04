import random

# Επιλογές του παιχνιδιού
options = ["rock", "paper", "scissors"]

# Ζητάμε την επιλογή του χρήστη
pl_input = input("Make Your choice (rock, paper, scissors): ").lower()

# Η επιλογή του υπολογιστή
pc_input = random.choice(options)

# Εμφανίζουμε τις επιλογές
print("Your choice: ", pl_input)
print("Computer choice: ", pc_input)

# Έλεγχος αποτελέσματος
if pl_input == pc_input:
    print("Είστε Ισοπαλία!")  # Ισοπαλία
elif (pl_input == "rock" and pc_input == "scissors"): # Ο χρήστης κερδίζει
    print("Κέρδισες! Η πέτρα σπάει το ψαλίδι.") 
elif (pl_input == "scissors" and pc_input == "paper"): # Ο χρήστης κερδίζει
    print("Κέρδισες! Το ψαλίδι κόβει το χαρτί.") 
elif (pl_input == "paper" and pc_input == "rock"): # Ο χρήστης κερδίζει
    print("Κέρδισες! Η πέτρα τυλίγει το χαρτί.")  
elif (pc_input == "rock" and pl_input == "scissors"): 
    print("Έχασες! Η πέτρα σπάει το ψαλίδι.")  # Ο υπολογιστής κερδίζει
elif (pc_input == "scissors" and pl_input == "paper"):
    print("Έχασες! Το ψαλίδι κόβει το χαρτί.")  # Ο υπολογιστής κερδίζει
elif (pc_input == "paper" and pl_input == "rock"):
    print("Έχασες! Το ψαλίδι κόβει το χαρτί.")  # Ο υπολογιστής κερδίζει
else:
    print("Έδωσες μη αποδεκτή επιλογή\nΠαρακαλώ επέλεξε ξανά (rock, paper, scissors)...")  # Λάθος είσοδος

