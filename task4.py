import random
print("Выберите дверь: ")
print("1 2 3")
answer = int(input())
PC = random.randint(1, 3)
print("Игрок выбрал: ", PC)
chance = random.randint(1, 3)
while True:
    if (chance != answer) and (chance != PC):
        print("За дверью", chance, "нету ничего")
        break
    elif (chance == answer) or (chance == PC):
        chance = random.randint(1, 3)