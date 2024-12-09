def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result == 1:
            print('Единица. И не простое, и не сложное не пойми какое')
        if result == 2:
            print('Простое')
        for i in range(2, int(result ** 0.5) + 1):
            if result % i == 0:
                print('Составное')
                break
            else:
                print('Простое')
                break
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(4, 5, 7)
print(result)
