import math
import pytest
from latexexpr_efficalc import Operation, Variable, SUM, MAX, MIN, SQRT, SIN, COS, TAN, SINH, COSH, TANH, EXP, LOG, LN, \
    LOG10, RBRACKETS, BRACKETS, SBRACKETS, CBRACKETS, ABRACKETS


def test_variable_add():
    a = Variable("a", 5)
    c = a + a
    assert c.result() == 10


def test_variable_add_right():
    a = Variable("a", 5)
    c = 2 + a
    assert c.result() == 7


def test_variable_add_left():
    a = Variable("a", 5)
    c = a + 2
    assert c.result() == 7


def test_variable_subtract():
    a = Variable("a", 5)
    c = a - a
    assert c.result() == 0


def test_variable_subtract_right():
    a = Variable("a", 5)
    c = 7 - a
    assert c.result() == 2


def test_variable_subtract_left():
    a = Variable("a", 5)
    c = a - 7
    assert c.result() == -2


def test_variable_multiply():
    a = Variable("a", 5)
    c = a * a
    assert c.result() == 25


def test_variable_multiply_right():
    a = Variable("a", 5)
    c = 2 * a
    assert c.result() == 10


def test_variable_multiply_left():
    a = Variable("a", 5)
    c = a * 2
    assert c.result() == 10


def test_variable_power():
    a = Variable("a", 5)
    b = Variable("b", 3)
    c = a ** b
    assert c.result() == 125


def test_variable_power_right():
    a = Variable("a", 5)
    c = 2 ** a
    assert c.result() == 32


def test_variable_power_left():
    a = Variable("a", 5)
    c = a ** 2
    assert c.result() == 25


def test_variable_divide():
    a = Variable("a", 5)
    c = a / a
    assert c.result() == 1


def test_variable_divide_right():
    a = Variable("a", 5)
    c = 10 / a
    assert c.result() == 2


def test_variable_divide_left():
    a = Variable("a", 5)
    c = a / 2
    assert c.result() == 2.5


# TODO: Render floor div in LaTex and implement floor div operation
# def test_variable_floor_div():
#     a = Variable("a", 5)
#     b = Variable("b", 2)
#     c = a // b
#     assert c.result() == 2


def test_variable_neg():
    a = Variable("a", 5)
    assert (-a).result() == -5


def test_variable_abs():
    a = Variable("a", -5)
    assert abs(a).result() == 5


def test_variable_sum():
    a = Variable("a", 5)
    b = Variable("b", 15)
    c = Variable("c", 2)
    assert SUM(a, b, c).result() == 22


def test_variable_max():
    a = Variable("a", 5)
    b = Variable("b", 15)
    c = Variable("c", 2)
    assert MAX(a, b, c).result() == 15


def test_variable_min():
    a = Variable("a", 5)
    b = Variable("b", 15)
    c = Variable("c", 2)
    assert MIN(a, b, c).result() == 2


def test_variable_sqrt():
    a = Variable("a", 25)
    assert SQRT(a).result() == 5


def test_variable_sin():
    a = Variable("a", math.pi / 2)
    assert SIN(a).result() == pytest.approx(1, abs=0.001)


def test_variable_cos():
    a = Variable("a", math.pi / 2)
    assert COS(a).result() == pytest.approx(0, abs=0.001)


def test_variable_tan():
    a = Variable("a", math.pi / 3)
    assert TAN(a).result() == pytest.approx(1.732050, abs=0.001)


def test_variable_sinh():
    a = Variable("a", -2)
    assert SINH(a).result() == pytest.approx(-3.62686, abs=0.001)


def test_variable_cosh():
    a = Variable("a", -2)
    assert COSH(a).result() == pytest.approx(3.762196, abs=0.001)


def test_variable_tanh():
    a = Variable("a", -2)
    assert TANH(a).result() == pytest.approx(-0.96403, abs=0.001)


def test_variable_exp():
    a = Variable("a", 2)
    assert EXP(a).result() == pytest.approx(math.e ** 2, abs=0.001)


def test_variable_log():
    a = Variable("a", 2)
    b = Variable("b", 64)
    assert LOG(a, b).result() == 6


def test_variable_ln():
    a = Variable("a", 2)
    assert LN(a).result() == pytest.approx(0.693147, abs=0.001)


def test_variable_log10():
    a = Variable("a", 10000)
    assert LOG10(a).result() == 4


def test_variable_r_brackets():
    a = Variable("a", 2)
    b = Variable("b", 3, "in")
    c = b * RBRACKETS(a + b)
    assert c.result() == 15
    assert c.strSubstituted() == " 3 \\ \\mathrm{in} \\cdot \\left(  2 \\ \\mathrm{} +  3 \\ \\mathrm{in} \\right)"


def test_variable_brackets():
    a = Variable("a", 2)
    b = Variable("b", 3, "in")
    c = b * BRACKETS(a + b)
    assert c.result() == 15
    assert c.strSubstituted() == " 3 \\ \\mathrm{in} \\cdot \\left(  2 \\ \\mathrm{} +  3 \\ \\mathrm{in} \\right)"


def test_variable_s_brackets():
    a = Variable("a", 2)
    b = Variable("b", 3, "in")
    c = b * SBRACKETS(a + b)
    assert c.result() == 15
    assert c.strSubstituted() == " 3 \\ \\mathrm{in} \\cdot \\left[  2 \\ \\mathrm{} +  3 \\ \\mathrm{in} \\right]"


def test_variable_c_brackets():
    a = Variable("a", 2)
    b = Variable("b", 3, "in")
    c = b * CBRACKETS(a + b)
    assert c.result() == 15
    assert c.strSubstituted() == " 3 \\ \\mathrm{in} \\cdot \\left\\{  2 \\ \\mathrm{} +  3 \\ \\mathrm{in} \\right\\}"


def test_variable_a_brackets():
    a = Variable("a", 2)
    b = Variable("b", 3, "in")
    c = b * ABRACKETS(a + b)
    assert c.result() == 15
    assert c.strSubstituted() == " 3 \\ \\mathrm{in} \\cdot \\left\\langle  2 \\ \\mathrm{} +  3 \\ \\mathrm{in} \\right\\rangle"