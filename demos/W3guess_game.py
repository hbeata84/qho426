import random

secret_number = random.randint(1,20)
print("welcome to my Guess Game! im thinking abour nr between 1 and 20")

for attempts in range (1,6):
    print(f"attempt nr {attempts}")
    guess = int(input ("take a guess"))
    if guess == secret_number:
        print("Congrats! you guessed correct")
        break
    elif guess > secret_number:
        print ("too high")
    else:
        print("too low")
if guess != secret_number:
    print(f"game over, my number was{secret_number}")