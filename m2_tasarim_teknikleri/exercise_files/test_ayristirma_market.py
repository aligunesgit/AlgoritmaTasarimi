from ayristirma_market import ara_toplam, fis_toplami, indirim_uygula, kdv_ekle
from pytest import approx


def test_ara_toplam():
    assert ara_toplam(15.0, 2) == 30.0
    assert ara_toplam(99.9, 0) == 0


def test_indirim_ve_vergi():
    assert indirim_uygula(200, 0.10) == approx(180)
    assert indirim_uygula(200, 0) == 200
    assert kdv_ekle(100) == approx(120)


def test_fis_toplami():
    # (30 + 42.5 + 90) = 162.5 → %10 indirim 146.25 → %20 vergi 175.5
    assert fis_toplami(30, 42.5, 90, 0.10) == 175.5


def test_bos_fis():
    assert fis_toplami(0, 0, 0, 0.5) == 0
