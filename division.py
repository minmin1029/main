def division(a, b):
    """a를 b로 나눕니다. b가 0이면 에러를 냅니다."""
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return a / b
