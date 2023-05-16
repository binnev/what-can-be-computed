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


def test_3_5():
    # We can write a notional function no_on_string as follows:
    def no_on_string(p, i):
        if p(i) == "no":
            return "yes"
        else:
            return "no"

    # If this function can exist, we can also write no_on_self:
    def no_on_self(p):
        return no_on_string(p, p)

    """
    But this function produces a contradiction when called on itself. 
    Let's substitute in the source code for no_on_string into no_on_self, so it goes from 
    
        def no_on_self(p):
            return no_on_string(p, p)
    
    to 
    
        def no_on_self(p):
            if p(p) == "no":
                return "yes"
            else:
                return "no"

    Now let's call no_on_self(no_on_self), so substituting in p = no_on_self: 
    
        def no_on_self(no_on_self):
            if no_on_self(no_on_self) == "no":
                return "yes"
            else:
                return "no"

    There's the contradiction: 
    no_on_self(no_on_self) returns "yes" if no_on_self(no_on_self) returns "no".
    
    If we try to call no_on_self(no_on_self) in practice, the contradiction manifests itself as 
    an infinite recursion error.
    """
    with pytest.raises(RecursionError) as e:
        no_on_self(no_on_self)
    assert str(e.value) == "maximum recursion depth exceeded"
