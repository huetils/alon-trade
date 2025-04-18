"""
This type stub file was generated by pyright.
"""

"""keccakf1600.py

Keccak is a family of hash functions based on the sponge construction. It was
chosen by NIST to become the SHA-3 standard. This code implements the
Keccak-f[1600] permutation. Detailed information about this function can be
found on the official site [1]. Original implementation [2] by the Keccak Team.

Some caveats about the implementation:
    * width `b` of permutation is fixed as 1600 (5 * 5 * 64), which means
    the number of rounds is 24 (12 + 2ℓ, ℓ = log_2(b / 25))
    * ρ step could have its offsets pre-computed as the array `r`.
    * ι step could have its round constants pre-computed as the array `RC`.

[1] http://keccak.noekeon.org/
[2] https://git.io/vKfkb
"""

def keccak_f_1600(state):
    """The inner permutation for the Keccak sponge function.

    The Keccak-f permutation is an iterated construction consisting of a
    sequence of almost identical rounds. It operates on a state array with
    each of the twenty-four rounds performing five steps, described below
    with detail.

    The loops above and below the core of the permutation are used to save and
    restore the state array to a stream of bytes, used outside the permutation.
    The original state array has three dimensions, whereas this characteristic
    can be cleverly optimized to a 5x5 matrix with 64-bit words. As such, this
    implementation makes use of this trick and stores an entire lane (a z-axis
    set of bits within the state) as a single word.

    The θ step diffuses the bits alongside the state array by calculating the
    parity of nearby columns relative to a lane.

    The ρ and π steps are merged; together, they move more bits around
    according to two alike recurrence relations.

    The χ step is similar to an S-box permutation; it makes the whole round
    non-linear with a few logic operations on bits inside a line.

    The ι step is a simple LFSR that breaks the symmetry of the rounds. It
    generates constants by doing computations according to the round number
    and its previous output, modulo polynomials over GF(2)[x].

    Args:
        state:  square matrix of order 5 that holds the input bytes.

    Returns:
        state:  bytes permuted by Keccak-f[1600].
    """
    ...

def Keccak(r, c, _input, suffix, output_len):  # -> bytearray:
    """
    The general sponge function, consisting of the inner permutation and a
    padding rule (`pad10*1`). It consists of three main parts.
        * absorbing, where the input will be permuted repeatedly every time
            it is divided into a block of size `r + c`.
        * padding, where an oddly sized last block will be filled with bits
            until it can be fed into the permutation.
        * squeezing, where the output's blocks will be permuted more times
            until they are concatenated to the desired size.

    Args:
        r:          rate, or the number of input bits processed or output bits
                    generated per invocation of the underlying function
        c:          capacity, or the width of the underlying function minus
                    the rate
        _input:     list of bytes containing the desired object to be hashed
        suffix:     distinguishes the inputs arising from SHA-3/SHAKE functions
        output_len: length of hash output.

    Returns:
        Hash of the input bytes.
    """
    ...

def SHA3(_input):  # -> bytearray:
    """
    FIPS 202 generalized instance of the SHA-3 hash function.

    Args:
        size:   instance of desired SHA3 algorithm.
        _input: list of bytes to compute a hash from.

    Returns:
        Instance of the Keccak permutation that calculates the hash.
    """
    ...
