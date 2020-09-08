def convert_to_decimal(number, base):
    mul = 1
    result = 0

    while number > 0:
        result += number % 10 * mul
        mul += base
        number = number // 10

    return result


def test_convert_to_decimal():
    number, base = 1001, 2
    result = convert_to_decimal(number, base)
    print(result)
    print('finish')

if __name__ == '__main__':
    test_convert_to_decimal()