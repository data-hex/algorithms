#поиск НОД у двух чисел

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return gcd(a % b, b)
    elif b >= a:
        return gcd(a, b % a)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))

main()