def binary_game():
    print("Загадайте число от 0 до 1000, а я попробую его угадать!")

    low = 0
    hig = 1000
    att = 0

    while low <= hig:
        mid = (low + hig) // 2
        att += 1

        res = input(f"Твое число больше {mid}? (да/нет): ").strip().lower()

        if res == 'да':
            low = mid + 1
        elif res == 'нет':
            hig = mid - 1
        else:
            print("Пожалуйста, отвечайте только 'да' или 'нет'.")

    print(f"Я угадал! Твое число - {low}! Угадал за {att} попыток.")


binary_game()
