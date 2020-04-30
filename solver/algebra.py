from solver.helpers import display_float, Stf, Subtract
from solver.exercise import Exercise, latex, OpExercise, StfExercise
from sympy import (
    Add,
    expand as Expand,
    factor,
    Mul,
    powdenest,
    simplify as Simplify,
    solve,
    sqrt,
    symbols,
    sympify,
    UnevaluatedExpr,
)


def expand(expression):
    """Expand an algebraic expression

    Parameters
    ----------
    expression : str
        Mathematical expression to be expanded

    Examples
    --------
    >>> expand('(x - 2) * (x - 3)')
    ('(x - 2) (x - 3)', 'x^{2} - 5 x + 6')
    """
    return Exercise(latex, Expand)(expression)


def factorise(expression):
    """Factorise an algebraic expression

    Parameters
    ----------
    expression : str
        Mathematical expression to be factorised

    Examples
    --------
    >>> factorise('x^2 - 5 * x + 6')
    ('x^{2} - 5 x + 6', '(x - 2) (x - 3)')
    """
    return Exercise(latex, factor)(expression)


def simplify(expression):
    r"""Simplify an algebraic expression

    Parameters
    ----------
    expression : str
        Mathematical expression to be simplified

    Examples
    --------
    >>> symplify('x^2/x')
    ('\\frac{x^2}{x}', 'x')
    """
    return Exercise(latex, Simplify)(expression)


def add(*terms):
    r"""Add terms

    Parameters
    ----------
    terms : list
        List of strings which correspond to the mathematical expressions to add.

    Examples
    --------
    >>> add('3/4', '1/2')
    ('\\frac{3}{4} + \\frac{1}{2}', '\\frac{5}{4}')
    """
    return OpExercise(Add)(*terms)


def div(dividend, divisor):
    r"""Divide terms (with \div)

    Parameters
    ----------
    dividend : string
        Mathematical expression to divide.
    divisor : string
        What the dividend will be divided by.

    Examples
    --------
    >>> div('3/4', '2/3')
    ('\\frac{3}{4} \\div \\frac{2}{3}', '\\frac{9}{8}')
    """
    return OpExercise("div")(dividend, divisor)


def frac(numerator, denominator):
    r"""Divide terms (in fraction form)

    Parameters
    ----------
    numerator : string
        Mathematical expression to divide (numerator).
    denominator : string
        What the dividend will be divided by (denominator).

    Examples
    --------
    >>> frac('3/4', '2/3')
    ('\\frac{\\frac{3}{4}}{\\frac{2}{3}}', '\\frac{9}{8}')
    """
    return OpExercise("frac")(numerator, denominator)


def mult(*terms):
    r"""Multiply terms

    Parameters
    ----------
    terms : list
        List of strings which correspond to the mathematical expressions to multiply.

    Examples
    --------
    >>> mult('3/4', '1/2')
    ('\\frac{3}{4} \\times \\frac{1}{2}', '\\frac{3}{8}')
    """
    return OpExercise(Mul)(*terms)


def subtract(term1, term2):
    r"""Add terms

    Parameters
    ----------
    term1 : string
        Mathematical expression from which we want to subtract
    term2 : string
        Mathematical expression to subtract from 'term1'

    Examples
    --------
    >>> add('3/4', '1/2')
    ('\\frac{3}{4} + \\frac{1}{2}', '\\frac{5}{4}')
    """
    return OpExercise(Subtract)(term1, term2)


stf = Exercise(display_float, Stf)
stf2dec = Exercise(lambda t: latex(Stf(t)), display_float)
stfadd = StfExercise(Add)
stfdiv = StfExercise("div")
stffrac = StfExercise("frac")
stfmult = StfExercise(Mul)
stfsub = StfExercise(Subtract)

expindex = Exercise(
    lambda base, power: f"{{{base}}}^{{{power}}}",
    lambda base, power: r" \times ".join([str(base)] * power),
)


def power(expr, power, **substitutions):
    substitutions = [
        (symbols(t), UnevaluatedExpr(v)) for (t, v) in substitutions.items()
    ]
    exercise = f"\\br{{{latex(sympify(expr).subs(substitutions))}}}^{{{power}}}"
    expr = f"({expr})^({power})"
    solution = latex(powdenest(expr, force=True).subs(substitutions))
    return (exercise, solution)


def equation(lhs, rhs="0"):
    if isinstance(lhs, str) and "=" in lhs:
        lhs, rhs = lhs.split("=")
    lhs, rhs = sympify(lhs), sympify(rhs)
    exercise = f"{latex(lhs)} = {latex(rhs)}"
    solution = ", ".join([latex(sol) for sol in solve(lhs - rhs)])
    return (exercise, solution)


def complete_square(expr):
    alpha, h, k, x = symbols("alpha h k x")
    solution = alpha * (x + h) ** 2 + k
    sols = [y for y in solve(solution - sympify(expr), [alpha, h, k])[0]]
    exercise = latex(expr)
    solution = latex(solution.subs(dict(zip([alpha, h, k], sols))))
    return (exercise, solution)


def circle_equation(info, lhs, rhs=0):
    if isinstance(lhs, str) and "=" in lhs:
        lhs, rhs = lhs.split("=")
    lhs, rhs = sympify(lhs), sympify(rhs)
    eq = Expand(lhs - rhs)
    exercise = f"{latex(lhs)} = {latex(rhs)}"

    # alpha [ (x - v)^2 + (y - w)^2 - r^2 ] = 0
    x, y = symbols("x y")
    alpha = eq.coeff(x, 2)
    v = -eq.coeff(x, 1) / (2 * alpha)
    w = -eq.coeff(y, 1) / (2 * alpha)
    r = sqrt(v ** 2 + w ** 2 - eq.subs([(x, 0), (y, 0)]) / alpha)

    if info == "radius":
        solution = latex(r)
    else:
        solution = f"\\br{{{latex(v)}, {latex(w)}}}"
    return (exercise, solution)
