import random

#задание 1
print("\nЗадание 1\n")
rand = random.randint(1,10)
popit = 0

print("Угадайте загаданное число")
while True:
  n = int(input("Число: "))
  if (rand == n):
    print("Вы угадали число за ", popit+1, " попыток")
    break
  else:
    print("Попробуйте еще!")
    popit += 1;
    if (n > rand): print("Нужное число меньше вашего")
    else: print("Нужное число больше вашего")
    
#задание 2
print("\nЗадание 2\n")
mass = input("Буквы: ").lower().split(' ')
result = []
temp = []

for i in range(len(mass)):
    if len(temp) == 0 or mass[i] == temp[0]:
        temp.append(mass[i])  
    else:
        result.append(temp)  
        temp = [mass[i]]

if len(temp) > 0:
    result.append(temp)  

final = []  
seen = []  

for item in mass:
    if item not in seen:  
        seen.append(item)  
        gruppa = []
        for i in mass:
            if i == item:
                gruppa.append(i)
        final.append(gruppa)

print(final)

#задание 3
print("\nЗадание 3\n")
mast = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 2, 'Q': 3, 'K': 4, 'A': 11}
random.shuffle(mast)
ochki = 0

while True:
    answer = input("у - взять карту\nn - завершить игру\n")
    
    if answer == 'n':
        print("У вас", ochki, "очков. Игра завершена")
        break
    elif answer == 'y':
        card = mast.pop()
        ochki += values[card]  
        
        print("Ваша карта:", card)
        print("Ваши очки:", ochki)
        
        if ochki > 21:
            print("Вы проиграли! У вас больше 21 очка.")
            break
        elif ochki == 21:
            print("Мои поздравления, вы выиграли. Игра завершена!")
            break
    else:
        print("Такой команды не найдено.\n")
