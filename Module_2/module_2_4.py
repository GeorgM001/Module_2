numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:  # 1 пропускаем
        continue
    is_prime = True  # все числа правда
    for j in range(2, i):  # переменная j это чило от 2 до i - 1, потому что не включительно
        if i % j == 0:  # если i делится на j и при этом остаток 0, то flag = не правда, прерывание цикла
            is_prime = False
            break
    if is_prime:
        primes.append(i)  # если flag правда то число добавляется сюда
    else:
        not_primes.append(i)  # если flag не правда то число добавляется сюда
print('Primes: ', primes)
print('Not Primes: ', not_primes)