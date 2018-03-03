nums = input("Podaj dwie liczby a i b: ").split(' ')

list(nums)

a = int(nums[0])

if len(nums) < 2 :
    print('\nPodałeś jedną liczbę.\n')
    nums.append(input('Teraz podaj drugą liczbę: '))
    
a = int(nums[0])
b = int(nums[1])

M = int(input('Aby zobaczyć wszystkie możliwe operacje wpisz 1 lub jeśli chcesz wykonać jedna operację wciśnij 2: '))

if M == 1:
    print('\nDodawanie: ', a+b,
      '\nOdejmowanie: ', a-b,
      '\nMnożenie: ', a*b,
      '\nDzielenie(a/b): ', a/b,
      '\nDzielenie(b/a): ', b/a,
      '\nPotęgowanie(a^b): ', a**b,
      '\nPotęgowanie(b^a): ', b**a)

elif M == 2:
    O = input('Podaj znak operacji jaką chcesz wykonać: ')

    if O == '+':
        print(a+b)
    elif O == '-':
        print(a-b)
    elif O == '*':
        print(a*b)
    elif O == '/':
        print(a/b)
    elif O == '^':
        print(a**b)

else:
    'Podany znak nie odpowiada żadnemu działaniu program się zakończy swoje działanie'





