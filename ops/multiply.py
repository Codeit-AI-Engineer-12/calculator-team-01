def multiply(a, b):
    """두 수를 곱하여 결과를 반환한다.
    Args:
        a (int): 첫번째 자연수
        b (int): 두번째 자연수

    Raises:
        ValueError: 입력값이 자연수가 아닐 경우 발생

    Returns:
        int: 두 자연수를 곱한 값
    """

    if not isinstance(a, int) or a <= 0:
        raise ValueError("자연수만 계산할 수 있습니다.")

    if not isinstance(b, int) or b <= 0:
        raise ValueError("자연수만 계산할 수 있습니다.")

    return a * b
