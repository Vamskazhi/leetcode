import pytest
from two_sum import Solution


@pytest.mark.parametrize(
    'params', [
        [[2, 7, 11, 15], 9, [0, 1]],
        [[3, 2, 4], 6, [1, 2]],
        [[3, 3], 6, [0, 1]]
    ]
)
def test_two_sum(params):
    assert Solution().two_sum(params[0], params[1]) == params[2]

