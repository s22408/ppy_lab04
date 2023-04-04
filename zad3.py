#Zestaw 3. Napisz funkcję szyfrującą wiadomość szyfrem cezara. Dla ułatwienia należy przekształcić
# wiadomość tak aby zawierała tylko wielkie
# lub małe litery.
#Funkcja przyjmuje: wiadomość
#– tekst do zaszyfrowania, klucz
#– liczbę o ile należy przesunąć litery w alfabecie oraz
#zwraca zaszyfrowaną wiadomość w formie łańcucha znaków -string. (40%)
#Funkcja szyfruje tylko litery – inne znaki wstawia
#do końcowej zaszyfrowanej wiadomości bez zmian(10%)
#Funkcja rozwiązuje problem klucza przesuwającego litery
#poza zakres listy  z alfabetem oraz problem podania klucza
#o dowolnej wielkości(20%).
#Funkcja opcjonalnie przyjmuje dowolny alfabet. Domyślnie używa angielskiego(10%).
#alfabet: 'abcdefghijklmnopqrstuvwxyz'
def function3(text, key):

    wiadomosc = text.lower()
    klucz = key%26              #rozwiazanie problemu duzego klucza
    wynik = ''

    for x in range(len(wiadomosc)):

        if ord(wiadomosc[x])<97 or ord(wiadomosc[x])>122:
            wynik = wynik + wiadomosc[x]
            continue

        nowyZnak = ord(wiadomosc[x])+klucz

        if nowyZnak>122:
            nowyZnak = nowyZnak - 122 + 96 #bo zakres znakow od 97(a) do 122(z)

        wynik = wynik + chr(nowyZnak)

    return wynik

#test
print(function3('zzz aaa !@#$%^& bbbb',27))