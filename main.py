def task1(number: int, degree: int) -> float:
    if degree < 0:
        result = number * number
        return 1 / result
    if degree == 0:
        return 1
    if degree == 1:
        return number
    if degree >= 1:
        return number * task1(number, degree - 1)


print(task1(number=5, degree=2))

n = int(input('Enter value: '))


def stars(n):
    if n <= 0:
        return

    print('*', end='')

    return stars(n - 1)


print(stars(n))

# print(task2(stars=user))

num1 = int(input('Enter first value: '))
num2 = int(input('Enter last value: '))


def sum_range(a, b):
    if a > b:
        return 0

    return a + sum_range(a + 1, b)


print(sum_range(a=num1, b=num2))
