def add_numbers(a: float, b: float) -> float:
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

print(divide(10, 0))