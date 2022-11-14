from app.routes import compute_item


def test_compute_item():
    assert compute_item(2) == 6