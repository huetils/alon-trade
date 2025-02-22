"""
This type stub file was generated by pyright.
"""

class CurveFp:
    """Elliptic Curve over the field of integers modulo a prime."""
    def __init__(self, p, a, b) -> None:
        """The curve of points satisfying y^2 = x^3 + a*x + b (mod p)."""
        ...

    def p(self):  # -> Any:
        ...
    def a(self):  # -> Any:
        ...
    def b(self):  # -> Any:
        ...
    def contains_point(self, x, y):
        """Is the point (x,y) on this curve?"""
        ...

    def __str__(self) -> str: ...

class Point:
    """A point on an elliptic curve. Altering x and y is forbidding,
    but they can be read by the x() and y() methods."""
    def __init__(self, curve, x, y, order=...) -> None:
        """curve, x, y, order; order (optional) is the order of this point."""
        ...

    def __eq__(self, other) -> bool:
        """Return True if the points are identical, False otherwise."""
        ...

    def __add__(self, other):  # -> Self | Point:
        """Add one point to another point."""
        ...

    def __mul__(self, other):  # -> Point | Self:
        """Multiply a point by an integer."""
        ...

    def __rmul__(self, other):
        """Multiply a point by an integer."""
        ...

    def __str__(self) -> str: ...
    def double(self):  # -> Point:
        """Return a new point that is twice the old."""
        ...

    def x(self):  # -> Any:
        ...
    def y(self):  # -> Any:
        ...
    def curve(self):  # -> Any:
        ...
    def order(self):  # -> None:
        ...

INFINITY = ...
