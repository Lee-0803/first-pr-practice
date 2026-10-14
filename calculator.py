"""簡單的計算機函式。"""


def add(a, b):
    """回傳 a + b。"""
    return a + b


def subtract(a, b):
    """回傳 a - b。"""
    return a - b


def multiply(a, b):
    """回傳 a * b。"""
    return a * b


def divide(a, b):
    """回傳 a / b。b 為 0 時拋出 ZeroDivisionError。"""
    if b == 0:
        raise ZeroDivisionError("不能除以 0")
    return a / b
