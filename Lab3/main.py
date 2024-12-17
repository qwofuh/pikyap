from lab_python_oop.Rectangle import Rectangle 
from lab_python_oop.circle import Circle
from lab_python_oop.Square import Square
from colorama import init
init()
from colorama import Fore

def main():
    r = Rectangle("синий", 4, 5)
    c = Circle("зеленый", 6)
    s = Square("красный", 4)
    print(Fore.RED + str(s))
    print(Fore.GREEN + str(c))
    print(Fore.BLUE + str(r))

if __name__ == "__main__":
    main()
