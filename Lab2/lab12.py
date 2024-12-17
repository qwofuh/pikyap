import math
import sys

class equation:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def show(self):
        print(self.a,self.b,self.c)

    def solve(self):

        if self.a == 0:
            print("Это не биквадратное уравнение, A не может быть равно 0.")
            return
        
        D = self.b**2 - 4*self.a*self.c

        if D < 0:
            print("Действительных корней нет.")
            return
        
        t1 = (-self.b + math.sqrt(D)) / (2 * self.a)
        t2 = (-self.b - math.sqrt(D)) / (2 * self.a)

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

def get_kef(name):
        while True:
            try:
                value = float(input(f"Введите коэффициент {name}: "))
                return value
            except ValueError:
                print(f"Коэффициент {name} должен быть числом. Попробуйте снова.")

if len(sys.argv) == 4:
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
    except ValueError:
        print("Один или несколько параметров командной строки некорректны.")
        a = get_kef('A')
        b = get_kef('B')
        c = get_kef('C')
else:
    a = get_kef('A')
    b = get_kef('B')
    c = get_kef('C')

eq = equation(a,b,c).solve()