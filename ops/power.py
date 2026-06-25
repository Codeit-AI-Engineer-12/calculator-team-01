#태윤

def power(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("자연수만 입력할 수 있습니다.")
    if a <= 0 or b <= 0:
        raise ValueError("자연수만 입력할 수 있습니다.")
    return a ** b