import math
print("Салам алейкум я инженерный калькулятор")
print("Могу делать почти всё что угодно(кроме плова)")

def slojenie(a, b):
    return (a+b)
def vijitanie(a, b):
    return (a-b)
def umnojenie(a, b):
    return (a*b)
def delenie(a, b):
    if b!= 0:
        return (a/b)
    else:
        return "Ты не много попутал и делишь на 0"
def steepen(a, b):
    return a**b
def koren(a):
    if a > 0:
       return math.sqrt(a)
    else:
        return "Ты не много попутал и ввёл отрицательное число"
def factorial(a):
    if a > 0:
        return math.factorial(a)
    else:
        return "Ты не много попутал и число отрицательное"
def sin(a):
    return math.sin(a)
def cos(a):
    return math.cos(a)
def tangens(a):
    return math.tan(a)

def calc():
    print("По брацки выбери какое нибудь действие")
    print("1. Сложи")
    print("2. Вычти")
    print("3. умнож(преувелич)")
    print("4. раздели(преуеньши)")
    print("5. возведи в степень")
    print("6. вычти корень(унизь его)")
    print("7. Найди факториал")
    print("8. тут синус")
    print("9. там косинус")
    print("10 здесь вообще тангенс")
    print("11. Если хочешь можешь выйти жи ес")

while True:
    calc()
    vibor = input("Введи шо хочешь от меня: ")

    if vibor == '11':
        print("Программа закончилась.")
        break

    if vibor not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
        print("Ты жи ест не то выбрал")
        continue
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))

        if vibor == '1':
            print("Результат:", slojenie(a, b))
        elif vibor == '2':
            print("Результат:", vijitanie(a, b))
        elif vibor == '3':
            print("Результат:", umnojenie(a, b))
        elif vibor == '4':
            print("Результат:", delenie (a, b))
        elif vibor == '5':
            print("Результат:", steepen(a, b))
        elif vibor == '6':
            print("Результат:", koren(a))
        elif vibor == '7':
            print("Результат:", factorial(a))
        elif vibor == '8':
            print("Результат:", sin(a))
        elif vibor == '9':
            print("Результат:", cos(a))
        elif vibor == '10':
            print("Результат:", tangens(a))


    except ValueError as e:
        print("Ты жи есть выбрал неправильный формат числа:", str(e))
        continue
