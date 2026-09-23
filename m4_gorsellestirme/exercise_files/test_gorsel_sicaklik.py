import pytest
from gorsel_sicaklik import fahrenheita_cevir


def test_suyun_donma_noktasi():
    assert fahrenheita_cevir(0) == 32


def test_suyun_kaynama_noktasi():
    assert fahrenheita_cevir(100) == 212


def test_iki_olcegin_kesistigi_nokta():
    # -40 derece, iki ölçekte de aynı sayıyla gösterilir.
    assert fahrenheita_cevir(-40) == -40


def test_ondalikli_girdi():
    # Ondalıklı sayılarda küçük yuvarlama farkları olabilir; approx bunu tolere eder.
    assert fahrenheita_cevir(36.6) == pytest.approx(97.88)
