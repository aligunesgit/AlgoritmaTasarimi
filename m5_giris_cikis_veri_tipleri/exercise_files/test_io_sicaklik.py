import pytest
from io_sicaklik import celsiustan_fahrenheita, sicaklik_raporu


def test_donma_noktasi():
    assert celsiustan_fahrenheita(0) == 32


def test_vucut_sicakligi():
    assert celsiustan_fahrenheita(37) == pytest.approx(98.6)


def test_rapor_bicimi():
    assert sicaklik_raporu(100) == "100.0 °C = 212.0 °F"


def test_rapor_tek_ondalik_basamaga_yuvarlar():
    assert sicaklik_raporu(36.66) == "36.7 °C = 98.0 °F"


def test_negatif_sicaklik():
    assert sicaklik_raporu(-40) == "-40.0 °C = -40.0 °F"


def test_metinden_gelen_girdi():
    # input() str döndürür; önce float() ile çevirmek gerekir.
    assert sicaklik_raporu(float("25")) == "25.0 °C = 77.0 °F"
