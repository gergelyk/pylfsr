from lfsr import *
from lfsr.db import *

def test_max_len_lfsr_if():
    for n in range(2,10):
        init = 1
        taps = max_len_lfsr_min_taps[n]
        poly = taps_to_poly(taps)
        prng = lfsr_if(poly, init)
        period = measure_period(prng)
        assert(period == 2**n-1)

def test_max_len_lfsr_ef():
    for n in range(2,10):
        init = 1
        taps = max_len_lfsr_min_taps[n]
        poly = taps_to_poly(taps)
        prng = lfsr_ef(poly, init)
        period = measure_period(prng)
        assert(period == 2**n-1)


