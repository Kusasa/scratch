import random

print ('Goodday fellow homo sapien. What name do others call you?')
name = raw_input()

print('Nice to meet you there '+ name.title() +', you sexy thang. Come let\'s play a guessing game. I\'m thinking of a number between 1-20. I\'ll give you six chances to guess it right.') #Present the Game

actualNumber = random.randint(1,20)

while guesses < 7:
    print('Guess a number:')
    gn = int(input())
    if gn != actualNumber and gn < 21:
        print('Wrong!!! I\'m not thinking of '+ str(gn) + '.')
    if gn != actualNumber and gn > 20:
        print('HAYBO!!! The number you guess must be between 1 and 20. Hhhayi lento oyibhalayo lana.')
    if gn == actualNumber:
        break
    guesses = guesses + 1


if gn != actualNumber:
    print('Oops. ' + name.title() + ' unfortunately you failed to guess the number I was thinking of within the six chances I gave you. I was thinking of ' + str(actualNumber) + '. Better luck next time.')
else:
    print ('WELDONE!!! I was indeed thinking of ' + str(actualNumber) + '. It took you ' + str(guesses) + ' tries to make the right guess. ' + name.title() + ', you have so much luck ey.')
