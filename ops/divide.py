#태윤

def divide(a, b):
    """두 수를 나눈 결과를 반환합니다."""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b