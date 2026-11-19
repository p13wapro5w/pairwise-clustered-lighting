import pytest
from render import clustered_lighting as mod

CASES = [
    ("grid", 'm.cluster_grid(1920, 16) == 120'),
    ("depth", 'm.depth_slice(10, 0.1, 1000, 16) == 8'),
    ("cone", 'm.cone_extent(1.0, 0.5) == approx(2.0)'),
    ("overflow", 'm.overflow_policy(5, 3) == "keep_nearest"'),
    ("transparent", 'm.transparent_cluster(4) == 4'),
    ("barrier", 'm.barrier_ok(True) is True'),
    ("camera", 'm.camera_buffer(1, 2) == "1:2"'),
    ("light", 'm.light_key(3, 1) == "3:1"'),
    ("nan", 'm.sanitize_attenuation(float("nan")) == 0.0'),
    ("lag", 'm.buffer_lag(5, 3) == 2'),
    ("att0", 'm.attenuation(0.0, 5.0) == approx(1.0)'),
    ("att1", 'm.attenuation(5.0, 5.0) == approx(0.0)'),
    ("budget", 'm.cluster_budget(32, 32, 16, 2) == 8'),
    ("froxel", 'm.froxel_index(1, 2, 3, 4, 5) == 69'),
    ("keep", 'm.overflow_keep([5, 1, 3], 2) == [1, 3]')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
