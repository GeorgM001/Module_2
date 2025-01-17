def get_matrix(n, m, value):
    # Если размеры матрицы некорректны, возвращаем пустой список
    if n <= 0 or m <= 0:
        return []

    # Создаем пустую матрицу
    matrix = []

    # Внешний цикл: для каждой строки (n раз)
    for _ in range(n):
        row = []  # Создаем пустую строку
        # Внутренний цикл: заполняем строку значениями value (m раз)
        for _ in range(m):
            row.append(value)  # Добавляем элемент в строку
        # После заполнения строки добавляем её в матрицу
        matrix.append(row)

    # Возвращаем готовую матрицу
    return matrix

print(get_matrix(2,6,4))
