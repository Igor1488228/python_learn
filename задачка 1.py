print("""Біцан І.А., КМ-82.
Програма для обчислення суми трьох чисел """)


while True:

    try:
        a = float(input("Введіть значення a: "))
        b = float(input("Введіть значення b: "))
        c = float(input("Введіть значення c: "))
        print(a+b+c)  
    
        repit_program=input("Натисніть 1, щоб завершити")

        if repit_program=='1':
            break
    
    except ValueError:
        print('Помилочка')  
