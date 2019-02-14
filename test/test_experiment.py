from experiment import Experiment

from pytest import approx


def test_probability_of_a_head():
    # heads are 1
    e = Experiment()
    p = e.flip_coin_x_times(10000)
    assert p == approx(0.5, rel=0.01)


def test_probability_of_hh():
    # heads are 1
    e = Experiment()
    p = e.flip_coin_2x_ntimes(10000)
    assert p == approx(0.25, rel=0.01)


def test_probability_of_ththh():
    # heads are 1
    e = Experiment()
    p = e.flip_coin_with_pattern_n_time([0, 1, 0, 1, 1], 100_000, 5)
    assert p == approx((0.5)**5, rel=0.01)
