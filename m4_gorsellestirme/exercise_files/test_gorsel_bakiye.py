import pytest
from gorsel_bakiye import son_bakiye


def test_tipik_kullanim():
    assert son_bakiye(40, 100, 17.5) == 122.5


def test_hicbir_islem_yok():
    assert son_bakiye(50, 0, 0) == 50


def test_bakiye_sifirlanir():
    assert son_bakiye(20, 30, 50) == 0


def test_ondalikli_tutarlar():
    # 0.1 + 0.2 bilgisayarda tam olarak 0.3 etmez (M6); approx küçük farkı tolere eder.
    assert son_bakiye(0.1, 0.2, 0) == pytest.approx(0.3)
