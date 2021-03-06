from solver.geometry import arclength, cosine_law, convert, DEG, pythagoras

tests = [
    (convert(90), "90", r"\frac{\pi}{2}", "Convert an angle from degrees to radians",),
    (convert("pi", "deg"), r"\pi", r"180", "Convert an angle from radians to degrees",),
    (arclength(1, "pi", "L")[1], r"L = \pi"),
    (
        cosine_law(3, 4, 5, "gamma")[1],
        r"\gamma = 90",
        "Law of cosines to check right triangle has an angle of 90 degrees",
    ),
    (
        cosine_law(8, 10, "x", 60 * DEG)[1],
        r"x = 2 \sqrt{21}",
        "Law of cosines to find length",
    ),
    (
        cosine_law("sqrt(2)", 5, "sqrt(17)", "alpha", radians=True)[1],
        r"\alpha = \frac{\pi}{4}",
        "Law of cosines to find angle in radians",
    ),
    (pythagoras("a", 8, 10)[1], "a = 6", "Get missing length by Pythagoras's Theorem",),
    (pythagoras(3, 4, 5)[1], "Right triangle", "Check if right triangle",),
    (pythagoras(4, 4, 5)[1], "Not a right triangle", "Check if right triangle",),
]
