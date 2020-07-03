# 2.2


def sum_nth_integers(input, n):
    integers = list(map(int, input.split()))
    output = sum(integers[n - 1 :: n])
    return str(output)


def sum_second_integers(input):
    return sum_nth_integers(input, 2)


def sum_third_integers(input):
    return sum_nth_integers(input, 3)


def sum_third_ints_greater_than_sum_second_ints(input):
    third = sum_third_integers(input)
    second = sum_second_integers(input)
    return int(third) > int(second)


assert sum_second_integers("58 41 78 3 25 9") == "53"
assert sum_third_integers("58 41 78 3 25 9") == "87"
assert sum_third_ints_greater_than_sum_second_ints("58 41 78 3 25 9") is True


# 2.3


def count_g(*inputs):
    occurrences = [item.count("g") for item in inputs]
    return "\n".join(map(str, occurrences))


assert count_g("hhg", "ggt") == "1\n2"

# 2.7
