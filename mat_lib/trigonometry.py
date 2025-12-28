from factorial import factorial as fct


def sin(x):
    # Ряд Тейлора для sin(x) до x^11 (6 членов)
    term1 = x
    term2 = (x ** 3) / fct(3)
    term3 = (x ** 5) / fct(5)
    term4 = (x ** 7) / fct(7)
    term5 = (x ** 9) / fct(9)
    term6 = (x ** 11) / fct(11)

    result = term1 - term2 + term3 - term4 + term5 - term6
    return round(result, 5)