import sys
import math

def get_kef():
    while True:
        try:
            stroka = input()
            numbers = stroka.split()
            a,b,c = map(int, numbers)
            return a,b,c
        except ValueError:
            print("Некорректный ввод")

def solve(a, b, c):
    if a == 0:
        print("Это не биквадратное уравнение, A не может быть равно 0.")
        return

    D = b**2 - 4 * a * c
    if D < 0:
        print("Действительных корней нет.")
        return

    t1 = (-b + math.sqrt(D)) / (2 * a)
    t2 = (-b - math.sqrt(D)) / (2 * a)

    roots = []
    
    if t1 >= 0:
        roots.append(math.sqrt(t1))
        roots.append(-math.sqrt(t1))
    
    if t2 >= 0:
        roots.append(math.sqrt(t2))
        roots.append(-math.sqrt(t2))
    
    if roots:
        print("Действительные корни:", sorted(set(roots)))
    else:
        print("Действительных корней нет.")


if len(sys.argv) == 4:
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
    except ValueError:
        print("Некорректный ввод, введите коэффициенты снова")
        a,b,c = get_kef()
else:
    a,b,c = get_kef()

solve(a, b, c)
