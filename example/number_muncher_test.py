from example.number_muncher import NumberMuncher as nm


def test_increment():
    assert nm.increment(3) == 4


def test_decrement():
    assert nm.decrement(3) == 2
