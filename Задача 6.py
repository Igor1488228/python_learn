print("""Біцан І.А., КМ-82.
Програма для обчислення цілої к-сті парт """)

    
from math import ceil
while True:

    try:
        a = float(input("Введіть значення a: "))
        b = float(input("Введіть значення b: "))
        c = float(input("Введіть значення c: "))
        print(ceil(a/2)+ceil(b/2)+ceil(c/2))

        repit_program=input("Натисніть 1, щоб завершити")

        if repit_program=='1':
            break

    except ValueError:
        print('Помилочка')



  
