def sum_of_multiples(n=0, d=0):
    multiples = int((n-1) / d)
    return int((multiples * (multiples + 1) / 2) * d)


def main():
    t = int(input("How many times to run? "))
    for i in range(0, t):
        n = int(input("The maximum range of numbers? "))
        print(sum_of_multiples(n, 3)+sum_of_multiples(n, 5)-sum_of_multiples(n, 3*5))

if __name__ == '__main__':
    main()
