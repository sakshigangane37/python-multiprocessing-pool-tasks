from multiprocessing import Pool
import os

def CountEven(No):
    Count = 0

    for i in range(1, No + 1):
        if i % 2 == 0:
            Count = Count + 1

    return os.getpid(), No, Count

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    with Pool() as p:
        result = p.map(CountEven, Data)

    for ProcessID, Number, Count in result:
        print("Process ID :", ProcessID)
        print("Input Number :", Number)
        print("Even Number Count :", Count)
        print()

if __name__ == "__main__":
    main()