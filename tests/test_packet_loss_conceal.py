import pytest
from audio import packet_loss_conceal as mod

CASES = [
    ("pitch", 'm.pitch_period(100, 48000) == 480'),
    ("frame", 'm.frame_len(48000, 20) == 960'),
    ("delay", 'm.plc_delay(5, 3) == 8'),
    ("fec", 'm.fec_cover(2, 4) == approx(0.5)'),
    ("noise", 'm.comfort_noise(2.0, 0.5) == approx(1.0)'),
    ("reset", 'm.reset_state(True, 5) is None'),
    ("transient", 'm.transient_guard(True, 2) is False'),
    ("fade", 'm.fade_gain(0, 4) == approx(1.0)'),
    ("drift", 'm.clock_drift(48000, 47999) == 1'),
    ("device", 'm.device_delay(20, 30) == 10'),
    ("stereo", 'm.stereo_sync(1, 3) == 2'),
    ("max", 'm.max_conceal(10, 4) == 4'),
    ("recover", 'm.recover_fade(2, 4) == approx(0.5)'),
    ("energy", 'm.plc_energy(2.0, 0.5) == approx(1.0)'),
    ("align", 'm.frame_align(5, 4) == 1')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
