from multiprocessing import Pool
import os

def SumOdd(No):
    Sum = 0

    for i in range(1, No + 1, 2):
        Sum = Sum + i

    return os.getpid(), No, Sum

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    with Pool() as p:
        result = p.map(SumOdd, Data)

    for ProcessID, Number, Sum in result:
        print("Process ID :", ProcessID)
        print("Input Number :", Number)
        print("Sum of Odd Numbers :", Sum)
        print()

if __name__ == "__main__":
    main()