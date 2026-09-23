import pytest
from tip_donusum import tip_adi, yas_hesapla


def test_temel_tip_adlari():
    assert tip_adi(5) == "int"
    assert tip_adi(5.0) == "float"
    assert tip_adi("5") == "str"
    assert tip_adi(True) == "bool"


def test_donusumden_sonra_tip_degisir():
    assert tip_adi(int("42")) == "int"
    assert tip_adi(str(42)) == "str"


def test_yas_hesapla():
    assert yas_hesapla("2006", 2026) == 20


def test_bosluklu_girdi():
    assert yas_hesapla("  2006 \n", 2026) == 20


def test_yazi_ile_yazilmis_sayi_hata_verir():
    with pytest.raises(ValueError):
        yas_hesapla("iki bin alti", 2026)


def test_ondalikli_metin_int_ile_cevrilemez():
    with pytest.raises(ValueError):
        yas_hesapla("2006.5", 2026)


def test_bool_donusumu_tuzagi():
    # Boş olmayan her metin True'dur, "False" metni bile.
    assert bool("False") is True
    assert bool("") is False
