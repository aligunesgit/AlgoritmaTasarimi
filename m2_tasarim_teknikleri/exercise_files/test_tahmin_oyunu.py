import pytest
from tahmin_oyunu import kaba_kuvvet_tahmin_sayisi, yariya_bolme_tahmin_sayisi


def test_kaba_kuvvet_ilk_ve_son():
    assert kaba_kuvvet_tahmin_sayisi(1) == 1
    assert kaba_kuvvet_tahmin_sayisi(100) == 100


def test_yariya_bolme_ortadaki_sayi_tek_tahmin():
    assert yariya_bolme_tahmin_sayisi(50) == 1


def test_yariya_bolme_en_kotu_durum_yedi():
    en_kotu = max(yariya_bolme_tahmin_sayisi(s) for s in range(1, 101))
    assert en_kotu == 7


def test_yariya_bolme_bin_sayida_on():
    en_kotu = max(yariya_bolme_tahmin_sayisi(s, 1, 1000) for s in range(1, 1001))
    assert en_kotu == 10


def test_aralik_disi_hata():
    with pytest.raises(ValueError):
        kaba_kuvvet_tahmin_sayisi(0)
    with pytest.raises(ValueError):
        yariya_bolme_tahmin_sayisi(101)
