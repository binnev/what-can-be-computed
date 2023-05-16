import pytest

import utils
from exercises.chapter3.count_chars import count_chars
from exercises.chapter3.count_chars_b import count_chars_b


@pytest.mark.parametrize("func", [count_chars, count_chars_b])
@pytest.mark.parametrize(
    "input, solution",
    [
        ("CATTG", 5),
        (utils.rf("exercises/chapter3/count_chars.py"), 58),
        (utils.rf("exercises/chapter3/count_chars_b.py"), 103),
    ],
)
def test_3_2(func, input, solution):
    """
    The two programs give different output when given their own source code as input,
    because their own source code is different lengths, obviously. Both programs give the same
    answer to all the inputs.
    """
    val = func(input)
    assert val == solution
