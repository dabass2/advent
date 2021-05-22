import math

with open('input.txt', 'r') as f:
    x = f.read().splitlines()

def ass(mass):
    mass = int(mass)
    mass = mass / 3
    mass = math.floor(int(mass))
    mass = mass - 2
    if mass > 0:
        return(mass)
    else:
        return(0)

total = 0
# # print(x[0])
for mass in x:
    # print(mass)
    mass = int(mass) / 3
    mass = math.floor(int(mass))
    # print(mass)
    mass = int(mass) - 2
    # print(mass)
    total = total + int(mass)
    while mass > 0:
        mass = ass(mass)
        print(mass)
        total = total + int(mass)  

    # else:
    #     total = total + int(mass)
    # total = total + int(mass)

# mass = 100756
# mass = int(mass) / 3
# mass = math.floor(int(mass))
# # print(mass)
# mass = int(mass) - 2
# # print(mass)
# total = total + int(mass)
# print(total)
# while mass > 0:
#     mass = ass(mass)
#     print(mass)
#     total = total + int(mass)   

print(total)

