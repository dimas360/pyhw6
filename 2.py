def print_operation_table(operation):
    cols = int(input("Введите количество столбцов: "))
    for i in range(1, int(input("Введите количество строк: ")) + 1):
        answer = []
        for j in range(1, cols + 1):
            answer.append(str(operation(i, j)))
        print('\t'.join(answer))
print_operation_table(lambda x, y: x * y)

