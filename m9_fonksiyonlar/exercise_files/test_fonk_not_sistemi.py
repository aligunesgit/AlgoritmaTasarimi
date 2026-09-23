import pytest
from fonk_not_sistemi import harf_notu, ortalama_hesapla, rapor_yaz


def test_ortalama():
    assert ortalama_hesapla([70, 80, 90]) == 80


def test_ortalama_ondalikli():
    # Ondalıklı sayılarda küçük yuvarlama farkları olabilir; approx bunu tolere eder.
    assert ortalama_hesapla([0.1, 0.2]) == pytest.approx(0.15)


def test_ortalama_bos_liste():
    assert ortalama_hesapla([]) == 0.0


def test_harf_notu_sinir_degerleri():
    # Her aralığın tam alt sınırını ve hemen altını deniyoruz.
    assert harf_notu(90) == "AA"
    assert harf_notu(89.99) == "BA"
    assert harf_notu(50) == "DD"
    assert harf_notu(49.99) == "FF"


def test_harf_notu_uc_degerler():
    assert harf_notu(100) == "AA"
    assert harf_notu(0) == "FF"


def test_rapor():
    assert rapor_yaz("Ayşe", [80, 90]) == "Ayşe: ortalama 85.00, harf notu BA"


def test_rapor_bos_not_listesi():
    assert rapor_yaz("Can", []) == "Can: ortalama 0.00, harf notu FF"
