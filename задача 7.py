print("""Біцан І.А., КМ-82.
Програма для обчислення годин та хвилин """)

from math import floor,fmod
while True:

    try:
        N = float(input("Введіть значення N: "))
        print("Годин:",floor(N/60)-floor(N/1440)*24)
        print("Хвилин:",fmod(N,60))

        repit_program=input("Натисніть 1, щоб завершити")

        if repit_program=='1':
            break
    except ValueError:
        print('Помилочка')


    
