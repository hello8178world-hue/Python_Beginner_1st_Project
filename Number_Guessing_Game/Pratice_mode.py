import random

def Guess():

    print("Welcome Guessing Game")
    print("Choose Guessing Number 1 to 100")

    com = random.randint(1,100)
    
    guess = 0



    while True:

        try:

            user = int(input("Enter_Guess_Number: "))
            guess += 1

            if user < com:
                print("Too Low")

            elif user > com:
                print("Too High")

            else:
                print("Congratulation!! You Guesses Finished")
                print(f"Computer_Guess: {com} | Your_Guess: {user} | Time-Consume: {guess}")
                break

        
        except:
            print("Invalid_Value")
            print("You Can Choose 1 to 100 Range Number")
            
Guess()



def again():

    while True:

        print("If you can play again type: 1")
        print("If you can exit game type: 0")

        choice = int(input("Choose number for exit or Play-Again: "))

        if choice == 1:
            Guess()
        elif choice == 0:
            break


again()