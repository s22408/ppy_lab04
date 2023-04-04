#Zadanie 2. Napisz funkcję sprawdzającą czy podane liczby
#są liczbami pierwszymi w szybszy sposób niż w
# przykładzie. Do funkcji można przekazać dowolną liczbę
# argumentów (liczby). Liczby 0 i 1 nie są
# liczbami pierwszymi. (10%)

def function2(*arg):

    Argumenty = list(arg)

    for x in Argumenty:
        if x == 1 or x == 0:
            print(str(x)+' NIE jest liczbą pierwszą')
            continue

        i = 2
        while i^2 <= x:
            if x % i == 0:
                print(str(x)+' NIE jest liczbą pierwszą')
                break
            i =+ 1
            print(str(x)+' JEST liczbą pierwszą')
            break

function2(1,2,3,4,5,6,7)

#KONSOLA:
#1 NIE jest liczbą pierwszą
#2 NIE jest liczbą pierwszą
#3 JEST liczbą pierwszą
#4 NIE jest liczbą pierwszą
#5 JEST liczbą pierwszą
#6 NIE jest liczbą pierwszą
#7 JEST liczbą pierwszą