def root(a, b):
    # b제곱근을 반환
    try:
        return a ** (1 / b)
    except TypeError:
        return "Error"
        """
        Error catch
        """