import random
n = random.randint(1,100)
a = -1
guesses = 0
while(a != n):
    guesses +=1
    a = int(input("guess any number"))
    if (a>n):
        print("lower number please")
    else:
        print("higher number please")
        
print(f"you have gussed the number in {guesses} attempt")