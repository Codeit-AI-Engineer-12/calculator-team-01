#태윤
#x에 대한 다항식 미분

def derivative(expression, _=None):
    """x에 대한 단순 다항식 미분 결과를 문자열로 반환합니다."""
    expression = expression.replace(" ", "")
    expression = expression.replace("-", "+-")
    terms = expression.split("+")

    result = []

    for term in terms:
        if not term:
            continue

        if "x" not in term:
            continue

        coef_part = term.split("x")[0]
        power_part = term.split("x")[1]

        if coef_part in ("", "+"):
            coef = 1
        elif coef_part == "-":
            coef = -1
        else:
            coef = int(coef_part)

        if power_part.startswith("^"):
            power = int(power_part[1:])
        else:
            power = 1

        new_coef = coef * power
        new_power = power - 1

        if new_power == 0:
            result.append(str(new_coef))
        elif new_power == 1:
            result.append(f"{new_coef}x")
        else:
            result.append(f"{new_coef}x^{new_power}")

    if not result:
        return "0"

    return " + ".join(result).replace("+ -", "- ")