import pytest

from containsGAGA import containsGAGA
from exercises.chapter3.contains_ga_ga import containsGA_GA
from exercises.chapter3.count_chars import count_chars
from exercises.chapter3.count_chars_b import count_chars_b
from notYesOnSelfApprox import notYesOnSelfApprox
from utils import rf
from yesOnSelfApprox import yesOnSelfApprox
from yesOnStringApprox import yesOnStringApprox


@pytest.mark.parametrize("func", [count_chars, count_chars_b])
@pytest.mark.parametrize(
    "input, solution",
    [
        ("CATTG", 5),
        (rf("exercises/chapter3/count_chars.py"), 58),
        (rf("exercises/chapter3/count_chars_b.py"), 103),
    ],
)
def test_3_2(func, input, solution):
    """
    The two programs give different output when given their own source code as input,
    because their own source code is different lengths, obviously. Both programs give the same
    answer to all the inputs.
    """
    assert func(input) == solution


@pytest.mark.parametrize("func", [containsGAGA, containsGA_GA])
@pytest.mark.parametrize(
    "input, solution",
    [
        ("CATTG", "no"),
        ("GAGA", "yes"),
        ("GA_GA", "no"),
        (rf("exercises/chapter3/contains_ga_ga.py"), "no"),
    ],
)
def test_3_3(func, input, solution):
    assert func(input) == solution


@pytest.mark.parametrize(
    "output, expected",
    [
        (yesOnStringApprox(rf("longerThan1K.py"), rf("longerThan1K.py")), "no"),
        (yesOnStringApprox(rf("maybeLoop.py"), rf("maybeLoop.py")), "yes"),
        (yesOnSelfApprox(rf("longerThan1K.py")), "no"),
        (notYesOnSelfApprox(rf("containsGAGA.py")), "no"),
    ],
)
def test_3_4(output, expected):
    assert output == expected
