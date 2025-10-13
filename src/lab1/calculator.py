'''Калькулятор, умеющий вычислять результат операций над двумя числами'''

def calculator():
    """Запрашивает у пользователя числа и операцию, выводит результат."""
    first_value = float(input("Введите первое число: "))
    operation = input("Введите операцию (+, -, *, /): ")
    second_value = float(input("Введите второе число: "))

    if operation == "+":
        result = first_value + second_value
    elif operation == "-":
        result = first_value - second_value
    elif operation == "*":
        result = first_value * second_value
    elif operation == "/":
        if second_value == 0:
            print("Ошибка: деление на ноль")
            return
        result = first_value / second_value
    else:
        print("Ошибка: неизвестная операция")
        return

    print("Результат:", result)


if __name__ == "__main__":
    calculator()
