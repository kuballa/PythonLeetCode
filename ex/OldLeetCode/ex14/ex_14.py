import sys

def CommonPrefix(strs: str) -> str:
    for i in range(len(strs[0])):
        for s in strs[1:]:
            if len(s) <= i or s[i] != strs[0][i]:
                return s[:i]
    return s[0]

def main() -> int:
    s1 = ["flower", "flow", "flight"]
    s2 = ["dog", "racecar","car"]

    print(CommonPrefix(s1))
    print(CommonPrefix(s2))

    return 0

if __name__ == '__main__':
    sys.exit(main())