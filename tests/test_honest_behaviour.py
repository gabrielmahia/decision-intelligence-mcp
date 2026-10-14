from classical_strategy_mcp import main as server

_fn = lambda name: (getattr(server, name).fn if hasattr(getattr(server, name), "fn") else getattr(server, name))


def test_an_unknown_lens_says_the_competition_lens_was_applied():
    assert _fn("apply_strategy")("p", "astrology", "all")["lens_applied"] == "competition"
    assert _fn("apply_strategy")("p", "leadership", "all")["lens_applied"] == "leadership"
