import sys

def palindromeNumber(number: int) -> bool:
    reverseNum = 0
    tempOriginal = number

    while (tempOriginal > 0):
        lastDigit = tempOriginal % 10
        reverseNum = reverseNum * 10 + lastDigit
        tempOriginal = tempOriginal // 10 # // is needed because without that we experience numerical error

    if (number == reverseNum):
        return True
    else:
        return False

def main() -> int:
    k_1 = 1234321
    k_2 = 1236321
    k_3 = 12343821
    k_4 = 12343921
    k_5 = 123141321
    k_6 = 12534321
    k_7 = 12343021
    k_8 = 12343321

    print(palindromeNumber(k_1))
    print(palindromeNumber(k_2))
    print(palindromeNumber(k_3))
    print(palindromeNumber(k_4))
    print(palindromeNumber(k_5))
    print(palindromeNumber(k_6))
    print(palindromeNumber(k_7))
    print(palindromeNumber(k_8))
    return 0

if __name__ == '__main__':
    sys.exit(main())