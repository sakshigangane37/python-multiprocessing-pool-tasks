from multiprocessing import Pool
import os

def Factorial(No):
    Fact = 1

    for i in range(1, No + 1):
        Fact = Fact * i

    return os.getpid(), No, Fact

def main():
    Data = [10, 15, 20, 25]

    with Pool() as p:
        result = p.map(Factorial, Data)

    for ProcessID, Number, Fact in result:
        print("Process ID :", ProcessID)
        print("Input Number :", Number)
        print("Factorial :", Fact)
        print()

if __name__ == "__main__":
    main()