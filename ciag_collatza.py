liczba = int(input('Podaj liczbę od 1 do 100: '))
dlugosc_ciagu = 0

while liczba < 1 or liczba > 100: 
    print('Liczba wykracza poza zakres 1-100, podaj liczbę jeszcze raz: ')
    liczba = int(input())
dlugosc_ciagu += 1
pierwsza_liczba = liczba
while liczba != 1:
    if liczba % 2 == 0:
        liczba = liczba / 2
        dlugosc_ciagu += 1
    else:
        liczba = 3 * liczba + 1
        dlugosc_ciagu += 1
print(f'Długość ciągu Collatza dla {pierwsza_liczba}: {dlugosc_ciagu}')
    