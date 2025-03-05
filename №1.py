def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


while True:
    try:
        start = int(input("Введите начало диапазона (целое число): "))
        end = int(input("Введите конец диапазона (целое число): "))
        if start > end:
            print("Начало диапазона должно быть меньше конца. Попробуйте снова.")
            continue
        prime_number = [num for num in range(start, end + 1) if is_prime(num)]
        print(prime_number)
        break
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целые числа.")