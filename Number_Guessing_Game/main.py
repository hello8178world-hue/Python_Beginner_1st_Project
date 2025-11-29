import random

def Guessing_Game():

    Computer = random.randint(1,100) # Generate Random Number 1 to 100

    print("🎉 Welcome to the Number Guessing Game!")
    print("🔢 I'm thinking of a number between 1 and 100. Can you guess it?")

    # Initialize counter for number Guesses
    Guesses = 0 

    while True:

        # try is handle error like somone input string
        try :

            # User take inpute
            User = int(input("Enter a number: "))
            Guesses += 1 # If user not guess correct. They guessing time increase...

            # Condition
            if (User > Computer):
                print("📉 Too high! Try a smaller number.")
            elif (User < Computer):
                print("📈 Too low! Try a bigger number.")
            else:
                print("✅ Congratulations!! 🎉")
                print(f"Guesses number is {User}. You are Guessing time is {Guesses}")
                break

        except ValueError :
            print("❌ Please enter a valid integer (e.g., 42).")

Guessing_Game()


# Ask Play_Again.....

def Again():
    
    while True:

        # Guessing_Again
        print("Let's Guessing Again...")
        print("If you play again press '1' ")
        print("If you will exit press '2' ")

        choice = int(input("Choose_Option: "))

        if choice == 1:
            Guessing_Game()
        else:
            print("😊😊Thank you for playing with me...")
            break
        
Again()