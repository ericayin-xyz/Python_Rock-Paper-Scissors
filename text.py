# import random
# from re import X
# from turtle import position


# random_integer = random.randint(1,10)

# print(random_integer)
 
# random_float = random.random[0,5).

# print(random_float)

row1 = ["😂","😂","😂"]
row2 = ["😂","😂","😂"]
row3 = ["😂","😂","😂"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")
position = input("Where do you want to put the tresure? ")
horizonal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizonal - 1] = "🤣"


print(f"{row1}\n{row2}\n{row3}\n")

