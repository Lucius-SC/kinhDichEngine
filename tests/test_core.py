from core.logic import rut_que

def test_rut_que():
    que = rut_que()
    assert "name" in que
    assert "meaning" in que
