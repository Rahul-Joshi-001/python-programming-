import random
num = random.randint(1,100)


print("YOU HAVE TO GUESS A RANDOM NO BETWEEN 1 TO 100")

chances  =0

while(True):
    guess_num = input("guess your no or press Q to quit :- ")
    if(guess_num =='Q'):
        break

    guess_num = int(guess_num)
    if(guess_num==num):
        chances += 1
        print("you guessed it in",chances,"chances hurray !")
        break;
    elif(guess_num>num):
        print("the no is too big")
        chances += 1

    else:
        print("the no is too small"); 
        chances += 1
        
print("-------GAME OVER--------")