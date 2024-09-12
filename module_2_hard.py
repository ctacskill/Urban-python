import random

first_num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , 14, 15, 16, 17, 18, 19, 20]

def password():
    password_ = []
    result = ''
    n = random.choice(first_num)
    print(n)
    for i in range(1, n):
        for k in range(1,n):
            if i > k:
                continue
            else:
                sum = i + k
            if n % sum == 0:
                password_.append(i)
                password_.append(k)
                result= result + str(i) + str(k)

    print(password_)
    print(result)

password()