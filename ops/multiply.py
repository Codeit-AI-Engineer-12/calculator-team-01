def multiply(a, b):

    if not isinstance(a, int) or a <= 0:
        raise ValueError("자연수만 계산할 수 있습니다.")

    if not isinstance(b, int) or b <= 0:
        raise ValueError("자연수만 계산할 수 있습니다.")

    return a * b
