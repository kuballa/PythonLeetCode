from itertools import pairwise
import sys

def RomanToInteger(s: str) -> int:
    d = {"I": 1,
         "V": 5,
         "X": 10,
         "L": 50,
         "C": 100,
         "D": 500,
         "M": 1000}

    return (sum(
            (-1 if d[a] < d[b] else 1) * d[a] 
            for a,b in pairwise(s)
            ) + d[s[-1]])

def main() -> int:
    s1 = "III"
    s2 = "LVIII"
    s3 = "MCMXCIV"

    print(RomanToInteger(s1))
    print(RomanToInteger(s2))
    print(RomanToInteger(s3))

if __name__ == '__main__':
    sys.exit(main())