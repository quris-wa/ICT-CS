"""Калькулятор, умеющий вычислять результат операций над двумя числами"""


def calculator(first_value: float, operation: str, second_value: float):
    """Выводит результат операции над двумя числами"""
    if operation == "+":
        result = first_value + second_value
    elif operation == "-":
        result = first_value - second_value
    elif operation == "*":
        result = first_value * second_value
    elif operation == "/":
        if second_value == 0:
            print("Ошибка. Деление на 0")
            raise ValueError("Деление на 0")
        result = first_value / second_value
    else:
        print("Ошибка. Неизвестная операция")
        raise ValueError("Неизвестная операция")

    print("Результат:", result)
    return result


if __name__ == "__main__":

    a = float(input("Введите первое число: "))
    o = input("Введите операцию (+, -, *, /): ")
    b = float(input("Введите второе число: "))

    calculator(a, o, b)
