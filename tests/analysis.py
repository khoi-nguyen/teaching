from solver.analysis import (
    diff,
    gradient,
    line_equation,
    maximum,
    minimum,
    plot,
    stationary,
    taylor,
)

tests = [
    # Plots
    (
        plot("x"),
        r"\plotfunction[darkblue]{-9:9}{(\x)}",
        r"Check x is replaced by \x in \plot",
    ),
    (
        plot("x**2"),
        r"\plotfunction[darkblue]{-9:9}{(\x)^2}",
        r"Check ** is replaced by ^ in \plot",
    ),
    (
        plot("x", "darkred"),
        r"\plotfunction[darkred]{-9:9}{(\x)}",
        "Changing plot color",
    ),
    (
        plot("x", "darkred", "3:4"),
        r"\plotfunction[darkred]{3:4}{(\x)}",
        "Changing plot domain",
    ),
    (
        plot("sin(x)"),
        r"\plotfunction[darkblue]{-9:9}{sin(((\x))r)}",
        "Force use of radians for plots",
    ),
    (
        plot("sin(cos(x))"),
        r"\plotfunction[darkblue]{-9:9}{sin((cos(((\x))r))r)}",
        "Radians in nested trig functions for plots",
    ),
    (gradient(0, 0, 1, 2)[1], "2", "Gradient from two points",),
    (
        line_equation(3, 1, 2)[1],
        "y = 3 x - 1",
        "Find the line equation with gradient and point",
    ),
    (
        line_equation(0, 1, 1, 3)[1],
        "y = 2 x + 1",
        "Find the line equation with two points",
    ),
    # Differentiation
    (
        diff("x^n"),
        r"\frac{d}{d x} x^{n}",
        "n x^{n - 1}",
        "Treat other variables as constant when differentiating",
    ),
    (
        diff("x*y", "x", partial=True)[0],
        r"\frac{\partial}{\partial x} x y",
        "Partial differentiation",
    ),
    (
        diff("sin(x)^2")[1],
        r"2 \sin{\left(x \right)} \cos{\left(x \right)}",
        "Don't factorise trig functions",
    ),
    # Taylor
    (str(taylor("exp(x)", 0, 3)), "x**3/6 + x**2/2 + x + 1", "Taylor development",),
    # Stationary points
    (
        stationary("x^2 - 6*x + 4"),
        "x^{2} - 6 x + 4",
        r"\left\{3\right\}",
        "Stationary points",
    ),
    # Minimum
    (minimum("x^2 + 4*x + 6"), "x^{2} + 4 x + 6", "-2", "Single minimum function",),
    (
        minimum("(x-2)^2 * (x-3)^2"),
        r"\left(x - 3\right)^{2} \left(x - 2\right)^{2}",
        "2, 3",
        "Double minimum function",
    ),
    # Maximum
    (
        maximum("-(x - 2)^2 * (x + 3)^2"),
        r"\left(x - 2\right)^{2} \left(x + 3\right)^{2}",
        "-3, 2",
        "Find function max",
    ),
]