#Zadanie 2. Napisz funkcję sprawdzającą czy podane liczby
#są liczbami pierwszymi w szybszy sposób niż w
# przykładzie. Do funkcji można przekazać dowolną liczbę
# argumentów (liczby). Liczby 0 i 1 nie są
# liczbami pierwszymi. (10%)

def function2(*arg):

    Argumenty = list(arg)

    for x in Argumenty:
        print(x)
        if x == 1 or x == 0:
            print(str(x)+' NIE jest liczbą pierwszą')

        i = 2
        while i^2 <= x:
            if x % i == 0:
                print(str(x)+' NIE jest liczbą pierwszą')
            i =+ 1
            print(str(x)+' JEST liczbą pierwszą')

function2(1,2)