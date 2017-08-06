from lib.number_multiples.number_multiples import NumberMultiples


def main():
    try:
        n = int(input("The maximum range of numbers? "))
    except ValueError:
        print("This is not a positive number")

    m = NumberMultiples(n=n)

    print(m.count_multiples_of(3))
    print(m.list_multiples_of('3'))
    print(m.sum_multiples_of('a', 5))

if __name__ == '__main__':
    main()
