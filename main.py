from random import randint

#Menu
while True:
    difficultyLevel = input("What difficulty level do you want? \n- Easy (1-10) \n- Medium(1-30) \n- Hard(1-100)\n")
    difficultyLevel = difficultyLevel.capitalize()
    if not difficultyLevel in ["Easy", "Medium", "Hard"]:
        print("You have to type 'Easy', 'Medium' or 'Hard' to continue.\n")
    elif difficultyLevel == "Easy":
        maxNumber = 10
        break
    elif difficultyLevel == "Medium":
        maxNumber = 30
        break
    else:
        maxNumber = 100
        break

#Actual game
while True:
    randomNumber = randint(1, maxNumber)
    howManyTries = 0
    while True:
        howManyTries += 1
        userNumber = int(input(f"Choose a number from 1 to {maxNumber}: "))

        if userNumber == randomNumber:
            print(f"Congratulations! The number was {randomNumber}. You guessed it in {howManyTries} attempt/attempts\n")
            break
        elif userNumber < randomNumber:
            print("Your number is too small! Try something bigger.\n")
        elif userNumber > randomNumber:
            print("Your number is too big! Try something smaller.\n")