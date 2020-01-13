from random import randint

rand_num = randint(1, 100)

def guess():
    print("Zgadnij liczbę od 1 do  100!")
    try:
        num = int(input("Twoja liczba: "))
    except ValueError:
        print("Wprowadź poprawną liczbę")
        guess()
    if num > 100:
        print("Liczba jest większa od 100!")
        guess()
    if num > rand_num:
        print("Za dużo")
        guess()
    elif num < rand_num:
        if num <= 0:
            print("Wprowadź liczbę większą od 0")
        else:
            print("Za mało")
        guess()
    else:
        print("Zgadłeś")

guess()