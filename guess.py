import random
#grah = random.randint(1,10)
#replace all instances of bot with grah
pool = [1,2,3,4,5,6,7,8,9,10]
b1 = min(pool)
b2 = max(pool)
history = [] 
bot = int(random.choice(pool))
print(f" I'm thinking of a number between {b1} and {b2}, what is it?:")
choice = 0
while bot != choice:
    choice = int(input("guess?:"))
    print("try again:")
    if choice < bot:
        history.append(choice)
        print(f"{choice} is less than the number")
    elif choice > bot:
        history.append(choice)
        print(f"{choice} is greater than the number")
    if choice == bot:
        history.append(choice)
        tah = len(history)
        print(f"{choice} is correct. Only took you {tah} attempts")
        print(history)


""" #challenge 1 
x = 10
while x != 1:
    print(x)
    x = x - 1 
    if x == 1:
        print(x) """

#challenge 2 
""" 
color = 0
list = []
while color != "stop":
    color = input("what are your favorite colors? type 'stop' to stop:")
    if color != "stop":
        list.append(color)
    elif color == "stop":
        list = (set(list))
        print(f"your favorite colors are {list}")
     """
