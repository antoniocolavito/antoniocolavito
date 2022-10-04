import random
x = 0
y = 0
i = 0
while i < 100:
    S = random.randint(1,10)
    dir = random.randint(1,4) #1 = Nord, 2 = Sud, 3 = Est, 4 = Ovest
    if dir == 1:
        y = y + S
    elif dir == 2:
        Y = y - S
    elif dir == 3:
        x = x + S
    elif dir == 4:
        x = x - S
    i = i + 1
print('La posizione è finale:' ,x,y)
