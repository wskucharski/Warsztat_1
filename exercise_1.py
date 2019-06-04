def  guessing_game():

    import random

    print("Witaj w grze w zgadywanie liczb!")

    guessed = False
    guessed_number = random.randint(0, 100)
    print(guessed_number)
    while not guessed:
        try:
            number = int(input("Zgadnij liczbę z zakresu 0-100: "))
            number = int(number)
            if number > guessed_number:
                print("Za dużo!")
            elif number < guessed_number:
                print("Za mało!")
            else:
                print("Zgadłeś!")
                guessed = True
                restart = input("Czy chcesz zagrać jeszcze raz? tak/nie")
                if restart == 'tak':
                    guessing_game()
                else:
                    exit()




        except ValueError:
            print("To nie jest liczba!")

    print(f"Liczba {number} jest poprawna!")

guessing_game()