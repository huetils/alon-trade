"""
This type stub file was generated by pyright.
"""

from typing import Tuple as tTuple
from typing import Type

"""
PythonMPQ: Rational number type based on Python integers.

This class is intended as a pure Python fallback for when gmpy2 is not
installed. If gmpy2 is installed then its mpq type will be used instead. The
mpq type is around 20x faster. We could just use the stdlib Fraction class
here but that is slower:

    from fractions import Fraction
    from sympy.external.pythonmpq import PythonMPQ
    nums = range(1000)
    dens = range(5, 1005)
    rats = [Fraction(n, d) for n, d in zip(nums, dens)]
    sum(rats) # <--- 24 milliseconds
    rats = [PythonMPQ(n, d) for n, d in zip(nums, dens)]
    sum(rats) # <---  7 milliseconds

Both mpq and Fraction have some awkward features like the behaviour of
division with // and %:

    >>> from fractions import Fraction
    >>> Fraction(2, 3) % Fraction(1, 4)
    1/6

For the QQ domain we do not want this behaviour because there should be no
remainder when dividing rational numbers. SymPy does not make use of this
aspect of mpq when gmpy2 is installed. Since this class is a fallback for that
case we do not bother implementing e.g. __mod__ so that we can be sure we
are not using it when gmpy2 is installed either.
"""
_PyHASH_MODULUS = ...
_PyHASH_INF = ...

class PythonMPQ:
    """Rational number implementation that is intended to be compatible with
    gmpy2's mpq.

    Also slightly faster than fractions.Fraction.

    PythonMPQ should be treated as immutable although no effort is made to
    prevent mutation (since that might slow down calculations).
    """

    __slots__ = ...
    def __new__(cls, numerator, denominator=...):  # -> Self:
        """Construct PythonMPQ with gcd computation and checks"""
        ...

    def __int__(self) -> int:
        """Convert to int (truncates towards zero)"""
        ...

    def __float__(self):
        """Convert to float (approximately)"""
        ...

    def __bool__(self):  # -> bool:
        """True/False if nonzero/zero"""
        ...

    def __eq__(self, other) -> bool:
        """Compare equal with PythonMPQ, int, float, Decimal or Fraction"""
        ...

    def __hash__(self) -> int:
        """hash - same as mpq/Fraction"""
        ...

    def __reduce__(self):  # -> tuple[type[Self], tuple[Any, Any]]:
        """Deconstruct for pickling"""
        ...

    def __str__(self) -> str:
        """Convert to string"""
        ...

    def __repr__(self):  # -> str:
        """Convert to string"""
        ...

    def __lt__(self, other) -> bool:
        """self < other"""
        ...

    def __le__(self, other) -> bool:
        """self <= other"""
        ...

    def __gt__(self, other) -> bool:
        """self > other"""
        ...

    def __ge__(self, other) -> bool:
        """self >= other"""
        ...

    def __abs__(self):  # -> Self:
        """abs(q)"""
        ...

    def __pos__(self):  # -> Self:
        """+q"""
        ...

    def __neg__(self):  # -> Self:
        """-q"""
        ...

    def __add__(self, other):  # -> _NotImplementedType | Self:
        """q1 + q2"""
        ...

    def __radd__(self, other):  # -> Self | _NotImplementedType:
        """z1 + q2"""
        ...

    def __sub__(self, other):  # -> _NotImplementedType | Self:
        """q1 - q2"""
        ...

    def __rsub__(self, other):  # -> Self | _NotImplementedType:
        """z1 - q2"""
        ...

    def __mul__(self, other):  # -> _NotImplementedType | Self:
        """q1 * q2"""
        ...

    def __rmul__(self, other):  # -> Self | _NotImplementedType:
        """z1 * q2"""
        ...

    def __pow__(self, exp):  # -> Self:
        """q ** z"""
        ...

    def __truediv__(self, other):  # -> _NotImplementedType | Self:
        """q1 / q2"""
        ...

    def __rtruediv__(self, other):  # -> Self | _NotImplementedType:
        """z / q"""
        ...

    _compatible_types: tTuple[Type, ...] = ...
