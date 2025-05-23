"""
This type stub file was generated by pyright.
"""

oid_ecPublicKey = ...
encoded_oid_ecPublicKey = ...

def randrange(order, entropy=...):  # -> int:
    """Return a random integer k such that 1 <= k < order, uniformly
    distributed across that range. For simplicity, this only behaves well if
    'order' is fairly close (but below) a power of 256. The try-try-again
    algorithm we use takes longer and longer time (on average) to complete as
    'order' falls, rising to a maximum of avg=512 loops for the worst-case
    (256**k)+1 . All of the standard curves behave well. There is a cutoff at
    10k loops (which raises RuntimeError) to prevent an infinite loop when
    something is really broken like the entropy function not working.

    Note that this function is not declared to be forwards-compatible: we may
    change the behavior in future releases. The entropy= argument (which
    should get a callable that behaves like os.urandom) can be used to
    achieve stability within a given release (for repeatable unit tests), but
    should not be used as a long-term-compatible key generation algorithm.
    """
    ...

class PRNG:
    def __init__(self, seed) -> None: ...
    def __call__(self, numbytes):  # -> bytes:
        ...
    def block_generator(self, seed):  # -> Generator[int, Any, NoReturn]:
        ...

def randrange_from_seed__overshoot_modulo(seed, order): ...
def lsb_of_ones(numbits): ...
def bits_and_bytes(order):  # -> tuple[int, int, int]:
    ...
def randrange_from_seed__truncate_bytes(seed, order, hashmod=...):  # -> int:
    ...
def randrange_from_seed__truncate_bits(seed, order, hashmod=...):  # -> int:
    ...
def randrange_from_seed__trytryagain(seed, order):  # -> int:
    ...
def number_to_string(num, order):  # -> bytes:
    ...
def number_to_string_crop(num, order):  # -> bytes:
    ...
def string_to_number(string):  # -> int:
    ...
def string_to_number_fixedlen(string, order):  # -> int:
    ...
def sigencode_strings(r, s, order, v=...):  # -> tuple[bytes, bytes, Any | None]:
    ...
def sigencode_string(r, s, order, v=...):  # -> bytes:
    ...
def sigencode_der(r, s, order, v=...):  # -> bytes:
    ...
def sigencode_strings_canonize(
    r, s, order, v=...
):  # -> tuple[bytes, bytes, Any | None]:
    ...
def sigencode_string_canonize(r, s, order, v=...):  # -> bytes:
    ...
def sigencode_der_canonize(r, s, order, v=...):  # -> bytes:
    ...
def sigdecode_string(signature, order):  # -> tuple[int, int]:
    ...
def sigdecode_strings(rs_strings, order):  # -> tuple[int, int]:
    ...
def sigdecode_der(sig_der, order):  # -> tuple[int, int]:
    ...
