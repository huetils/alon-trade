"""
This type stub file was generated by pyright.
"""

PYPY = ...
__all__ = (
    "identity",
    "apply",
    "thread_first",
    "thread_last",
    "memoize",
    "compose",
    "compose_left",
    "pipe",
    "complement",
    "juxt",
    "do",
    "curry",
    "flip",
    "excepts",
)
PYPY = ...

def identity(x):
    """Identity function. Return x

    >>> identity(3)
    3
    """
    ...

def apply(*func_and_args, **kwargs):
    """Applies a function and returns the results

    >>> def double(x): return 2*x
    >>> def inc(x):    return x + 1
    >>> apply(double, 5)
    10

    >>> tuple(map(apply, [double, inc, double], [10, 500, 8000]))
    (20, 501, 16000)
    """
    ...

def thread_first(val, *forms):  # -> object | None:
    """Thread value through a sequence of functions/forms

    >>> def double(x): return 2*x
    >>> def inc(x):    return x + 1
    >>> thread_first(1, inc, double)
    4

    If the function expects more than one input you can specify those inputs
    in a tuple.  The value is used as the first input.

    >>> def add(x, y): return x + y
    >>> def pow(x, y): return x**y
    >>> thread_first(1, (add, 4), (pow, 2))  # pow(add(1, 4), 2)
    25

    So in general
        thread_first(x, f, (g, y, z))
    expands to
        g(f(x), y, z)

    See Also:
        thread_last
    """
    ...

def thread_last(val, *forms):  # -> object | None:
    """Thread value through a sequence of functions/forms

    >>> def double(x): return 2*x
    >>> def inc(x):    return x + 1
    >>> thread_last(1, inc, double)
    4

    If the function expects more than one input you can specify those inputs
    in a tuple.  The value is used as the last input.

    >>> def add(x, y): return x + y
    >>> def pow(x, y): return x**y
    >>> thread_last(1, (add, 4), (pow, 2))  # pow(2, add(4, 1))
    32

    So in general
        thread_last(x, f, (g, y, z))
    expands to
        g(y, z, f(x))

    >>> def iseven(x):
    ...     return x % 2 == 0
    >>> list(thread_last([1, 2, 3], (map, inc), (filter, iseven)))
    [2, 4]

    See Also:
        thread_first
    """
    ...

def instanceproperty(
    fget=..., fset=..., fdel=..., doc=..., classval=...
):  # -> partial[Any] | InstanceProperty:
    """Like @property, but returns ``classval`` when used as a class attribute

    >>> class MyClass(object):
    ...     '''The class docstring'''
    ...     @instanceproperty(classval=__doc__)
    ...     def __doc__(self):
    ...         return 'An object docstring'
    ...     @instanceproperty
    ...     def val(self):
    ...         return 42
    ...
    >>> MyClass.__doc__
    'The class docstring'
    >>> MyClass.val is None
    True
    >>> obj = MyClass()
    >>> obj.__doc__
    'An object docstring'
    >>> obj.val
    42
    """
    ...

class InstanceProperty(property):
    """Like @property, but returns ``classval`` when used as a class attribute

    Should not be used directly.  Use ``instanceproperty`` instead.
    """
    def __init__(self, fget=..., fset=..., fdel=..., doc=..., classval=...) -> None: ...
    def __get__(self, obj, type=...):  # -> Any | None:
        ...
    def __reduce__(
        self,
    ):  # -> tuple[type[InstanceProperty], tuple[Callable[[Any], Any] | None, Callable[[Any, Any], None] | None, Callable[[Any], None] | None, str | None, Any | None]]:
        ...

class curry:
    """Curry a callable function

    Enables partial application of arguments through calling a function with an
    incomplete set of arguments.

    >>> def mul(x, y):
    ...     return x * y
    >>> mul = curry(mul)

    >>> double = mul(2)
    >>> double(10)
    20

    Also supports keyword arguments

    >>> @curry                  # Can use curry as a decorator
    ... def f(x, y, a=10):
    ...     return a * (x + y)

    >>> add = f(a=1)
    >>> add(2, 3)
    5

    See Also:
        toolz.curried - namespace of curried functions
                        https://toolz.readthedocs.io/en/latest/curry.html
    """
    def __init__(self, *args, **kwargs) -> None: ...
    @instanceproperty
    def func(self):  # -> Callable[..., object]:
        ...
    @instanceproperty
    def __signature__(self):  # -> Signature:
        ...
    @instanceproperty
    def args(self):  # -> tuple[Any, ...]:
        ...
    @instanceproperty
    def keywords(self):  # -> dict[str, Any]:
        ...
    @instanceproperty
    def func_name(self):  # -> Any | str:
        ...
    def __str__(self) -> str: ...
    def __repr__(self):  # -> str:
        ...
    def __hash__(self) -> int: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __call__(self, *args, **kwargs):  # -> object | Self:
        ...
    def bind(self, *args, **kwargs):  # -> Self:
        ...
    def call(self, *args, **kwargs):  # -> object:
        ...
    def __get__(self, instance, owner):  # -> Self | curry:
        ...
    def __reduce__(
        self,
    ):  # -> tuple[Callable[..., ModuleType | Any], tuple[type[Self], LiteralString | Callable[[], Callable[..., object]], Callable[[], tuple[Any, ...]], Callable[[], dict[str, Any]], tuple[tuple[str, Any], ...], bool | None]]:
        ...

@curry
def memoize(func, cache=..., key=...):  # -> Callable[..., Any]:
    """Cache a function's result for speedy future evaluation

    Considerations:
        Trades memory for speed.
        Only use on pure functions.

    >>> def add(x, y):  return x + y
    >>> add = memoize(add)

    Or use as a decorator

    >>> @memoize
    ... def add(x, y):
    ...     return x + y

    Use the ``cache`` keyword to provide a dict-like object as an initial cache

    >>> @memoize(cache={(1, 2): 3})
    ... def add(x, y):
    ...     return x + y

    Note that the above works as a decorator because ``memoize`` is curried.

    It is also possible to provide a ``key(args, kwargs)`` function that
    calculates keys used for the cache, which receives an ``args`` tuple and
    ``kwargs`` dict as input, and must return a hashable value.  However,
    the default key function should be sufficient most of the time.

    >>> # Use key function that ignores extraneous keyword arguments
    >>> @memoize(key=lambda args, kwargs: args)
    ... def add(x, y, verbose=False):
    ...     if verbose:
    ...         print('Calculating %s + %s' % (x, y))
    ...     return x + y
    """
    ...

class Compose:
    """A composition of functions

    See Also:
        compose
    """

    __slots__ = ...
    def __init__(self, funcs) -> None: ...
    def __call__(self, *args, **kwargs): ...
    def __getstate__(self):  # -> tuple[Any, tuple[Any, ...] | Any]:
        ...
    def __setstate__(self, state):  # -> None:
        ...
    @instanceproperty(classval=__doc__)
    def __doc__(self):  # -> str:
        ...
    @property
    def __name__(self):  # -> LiteralString | property:
        ...
    def __repr__(self):  # -> str:
        ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __get__(self, obj, objtype=...):  # -> Self | MethodType:
        ...
    @instanceproperty
    def __signature__(self):  # -> Signature:
        ...

    __wrapped__ = ...

def compose(*funcs):  # -> Callable[..., Any] | Compose:
    """Compose functions to operate in series.

    Returns a function that applies other functions in sequence.

    Functions are applied from right to left so that
    ``compose(f, g, h)(x, y)`` is the same as ``f(g(h(x, y)))``.

    If no arguments are provided, the identity function (f(x) = x) is returned.

    >>> inc = lambda i: i + 1
    >>> compose(str, inc)(3)
    '4'

    See Also:
        compose_left
        pipe
    """
    ...

def compose_left(*funcs):  # -> Callable[..., Any] | Compose:
    """Compose functions to operate in series.

    Returns a function that applies other functions in sequence.

    Functions are applied from left to right so that
    ``compose_left(f, g, h)(x, y)`` is the same as ``h(g(f(x, y)))``.

    If no arguments are provided, the identity function (f(x) = x) is returned.

    >>> inc = lambda i: i + 1
    >>> compose_left(inc, str)(3)
    '4'

    See Also:
        compose
        pipe
    """
    ...

def pipe(data, *funcs):
    """Pipe a value through a sequence of functions

    I.e. ``pipe(data, f, g, h)`` is equivalent to ``h(g(f(data)))``

    We think of the value as progressing through a pipe of several
    transformations, much like pipes in UNIX

    ``$ cat data | f | g | h``

    >>> double = lambda i: 2 * i
    >>> pipe(3, double, str)
    '6'

    See Also:
        compose
        compose_left
        thread_first
        thread_last
    """
    ...

def complement(func):  # -> Callable[..., Any] | Compose:
    """Convert a predicate function to its logical complement.

    In other words, return a function that, for inputs that normally
    yield True, yields False, and vice-versa.

    >>> def iseven(n): return n % 2 == 0
    >>> isodd = complement(iseven)
    >>> iseven(2)
    True
    >>> isodd(2)
    False
    """
    ...

class juxt:
    """Creates a function that calls several functions with the same arguments

    Takes several functions and returns a function that applies its arguments
    to each of those functions then returns a tuple of the results.

    Name comes from juxtaposition: the fact of two things being seen or placed
    close together with contrasting effect.

    >>> inc = lambda x: x + 1
    >>> double = lambda x: x * 2
    >>> juxt(inc, double)(10)
    (11, 20)
    >>> juxt([inc, double])(10)
    (11, 20)
    """

    __slots__ = ...
    def __init__(self, *funcs) -> None: ...
    def __call__(self, *args, **kwargs):  # -> tuple[Any, ...]:
        ...
    def __getstate__(self):  # -> tuple[Any, ...]:
        ...
    def __setstate__(self, state):  # -> None:
        ...

def do(func, x):
    """Runs ``func`` on ``x``, returns ``x``

    Because the results of ``func`` are not returned, only the side
    effects of ``func`` are relevant.

    Logging functions can be made by composing ``do`` with a storage function
    like ``list.append`` or ``file.write``

    >>> from toolz import compose
    >>> from toolz.curried import do

    >>> log = []
    >>> inc = lambda x: x + 1
    >>> inc = compose(inc, do(log.append))
    >>> inc(1)
    2
    >>> inc(11)
    12
    >>> log
    [1, 11]
    """
    ...

@curry
def flip(func, a, b):
    """Call the function call with the arguments flipped

    This function is curried.

    >>> def div(a, b):
    ...     return a // b
    ...
    >>> flip(div, 2, 6)
    3
    >>> div_by_two = flip(div, 2)
    >>> div_by_two(4)
    2

    This is particularly useful for built in functions and functions defined
    in C extensions that accept positional only arguments. For example:
    isinstance, issubclass.

    >>> data = [1, 'a', 'b', 2, 1.5, object(), 3]
    >>> only_ints = list(filter(flip(isinstance, int), data))
    >>> only_ints
    [1, 2, 3]
    """
    ...

def return_none(exc):  # -> None:
    """Returns None."""
    ...

class excepts:
    """A wrapper around a function to catch exceptions and
    dispatch to a handler.

    This is like a functional try/except block, in the same way that
    ifexprs are functional if/else blocks.

    Examples
    --------
    >>> excepting = excepts(
    ...     ValueError,
    ...     lambda a: [1, 2].index(a),
    ...     lambda _: -1,
    ... )
    >>> excepting(1)
    0
    >>> excepting(3)
    -1

    Multiple exceptions and default except clause.

    >>> excepting = excepts((IndexError, KeyError), lambda a: a[0])
    >>> excepting([])
    >>> excepting([1])
    1
    >>> excepting({})
    >>> excepting({0: 1})
    1
    """
    def __init__(self, exc, func, handler=...) -> None: ...
    def __call__(self, *args, **kwargs): ...
    @instanceproperty(classval=__doc__)
    def __doc__(
        self,
    ):  # -> str | Callable[..., str | Callable[..., str | Callable[..., str | Callable[..., str | Callable[..., str | Callable[..., str | Callable[..., str | Callable[..., str | Callable[..., str | Callable[..., Any]]]]]]]]]]:
        ...
    @property
    def __name__(self):  # -> LiteralString | Literal['excepting']:
        ...

if PYPY:
    _check_sigspec_orig = ...

def num_required_args(func, sigspec=...):  # -> int | Literal[False] | None:
    ...
def has_varargs(func, sigspec=...):  # -> bool | None:
    ...
def has_keywords(func, sigspec=...):  # -> bool | None:
    ...
def is_valid_args(func, args, kwargs, sigspec=...):  # -> bool | None:
    ...
def is_partial_args(func, args, kwargs, sigspec=...):  # -> bool | None:
    ...
def is_arity(n, func, sigspec=...):  # -> bool | None:
    """Does a function have only n positional arguments?

    This function relies on introspection and does not call the function.
    Returns None if validity can't be determined.

    >>> def f(x):
    ...     return x
    >>> is_arity(1, f)
    True
    >>> def g(x, y=1):
    ...     return x + y
    >>> is_arity(1, g)
    False
    """
    ...
