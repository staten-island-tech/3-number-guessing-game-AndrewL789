import random

pool = [1,2,3,4,5,6,7,8,9,10]
b1 = min(pool)
b2 = max(pool)
x = 1
bot = int(random.choice(pool))
print(f" I'm thinking of a number between {b1} and {b2}, what is it?:")
choice = int(input("What am I thinking of?:"))
if choice == bot:
    print("that is right")
while bot != choice:
    
    
    choice = int(input("try again:"))
    x = x + 1
    print(f" this is attempt x{x}")
    
    
    if choice == bot:
        print(f"that is right, only took you {x + 1} attempts")

