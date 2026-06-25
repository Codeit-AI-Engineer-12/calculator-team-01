def floor_divide(a, b):
    """
    두 자연수를 정수 나눗셈하여 반환합니다. 소수점 이하는 버립니다.
    """

    if not isinstance(a, int) or a < 0:
        raise ValueError("자연수만 계산할 수 있습니다.")

    if not isinstance(b, int) or b < 0:
        raise ValueError("자연수만 계산할 수 있습니다.")

    return a // b
