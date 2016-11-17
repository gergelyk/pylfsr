Database
========

Database of precalculated values to be used with LFSR.

max_len_lfsr_min_taps
---------------------

Polynomials with minimal number of taps for maximum-length LFSR counters.

Source:
https://www.xilinx.com/support/documentation/application_notes/xapp210.pdf


max_len_lfsr_2_taps
-------------------

Polynomials with 2-taps for maximum-length LFSR counters.

Source:
http://courses.cse.tamu.edu/csce680/walker/lfsr_table.pdf


max_len_lfsr_4_taps
-------------------

Polynomials with 4-taps for maximum-length LFSR counters.

Source:
http://courses.cse.tamu.edu/csce680/walker/lfsr_table.pdf


Notes
-----

* Maximum-length LFSR counter - the one period of which equals 2**n-1 where n is width (number of bits) of the counter.
* Initial value of maximum-length LFSR counter can be anything except for 0.
* List of alternative maximal-length polynomials can be found here: http://www.ece.cmu.edu/~koopman/lfsr/index.html
