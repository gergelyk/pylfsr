Linear Feedback Shift Register Toolkit
======================================

**lfsr_if** `(poly, init=1)`

Linear Feedback Shift Register with internal feedback.

Example (visualization):

::

    poly = 0x0D (x**3+x**2+1)
    init = 0x01

::

    +----<-----+-------<-------+
    |          |               |
    +-----[0]-XOR-[0]-----[1]--+-->-- out

    x**3     x**2    x**1    x**0

::

    cycle state 
      0    001
      1    110
      2    011
      3    111
      4    101
      5    100
      6    010
  
Example (code):

>>> n = 3
>>> taps = max_len_lfsr_min_taps[n]
>>> poly = taps_to_poly(taps)
>>> prng = lfsr_if(poly)
>>> for i in range(10):
...     print(i, next(prng))
0 1
1 6
2 3
3 7
4 5
5 4
6 2
7 1
8 6
9 3
  
Reference: http://www.eng.auburn.edu/~strouce/class/elec6250/LFSRs.pdf


**lfsr_ef** `(poly, init=1)`

Linear Feedback Shift Register with external feedback.

Implements LFSR counter for many use cases. For instance for certain polynomial and init, LSB of the output can be considered as pseudo-random sequence.

Example (visualization):

::

    poly = 0x0D (x**3+x**2+1)
    init = 0x01

::

    +----<----XOR------<-------+
    |          |               |
    +-----[0]--+--[0]-----[1]--+-->-- out

    x**3     x**2    x**1    x**0

::

    cycle state 
      0    001
      1    100
      2    110
      3    111
      4    011
      5    101
      6    010

Example (code):

>>> n = 3
>>> taps = max_len_lfsr_min_taps[n]
>>> poly = taps_to_poly(taps)
>>> prng = lfsr_ef(poly)
>>> for i in range(10):
...     print(i, next(prng))
0 1
1 4
2 6
3 7
4 3
5 5
6 2
7 1
8 4
9 6

Reference: http://www.eng.auburn.edu/~strouce/class/elec6250/LFSRs.pdf


**taps_to_poly** `(taps, append0=True)`

Converts vector of taps to corresponding polynomial.

Note that tap #0 defaults to 1, unles `append0` is ``False``.

Example:

Vector of taps ``[4,3,0]`` correspond to polynomial ``x**4+x**3+1`` which is represented as ``0x19``.

**measure_period** `(cntr)`

Measures how many cycles it takes for the counter overflow.


References
----------

* `<http://www.eng.auburn.edu/~strouce/class/elec6250/LFSRs.pdf>`_
* `<https://www.xilinx.com/support/documentation/application_notes/xapp210.pdf>`_
* `<https://users.ece.cmu.edu/~koopman/lfsr/>`_
* `<https://en.wikipedia.org/wiki/Linear-feedback_shift_register>`_

