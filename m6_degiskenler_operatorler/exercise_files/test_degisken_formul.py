import math

from degisken_formul import daire_alani, fahrenhayta_cevir, kdvli_fiyat


def test_suyun_donma_ve_kaynama_noktasi():
    assert fahrenhayta_cevir(0) == 32
    assert fahrenhayta_cevir(100) == 212


def test_eksi_kirk_iki_olcekte_ayni():
    assert fahrenhayta_cevir(-40) == -40


def test_daire_alani():
    assert daire_alani(0) == 0
    # float karşılaştırması: == yerine math.isclose (bkz. M6 §3.2)
    assert math.isclose(daire_alani(1), math.pi)
    assert math.isclose(daire_alani(2), 4 * math.pi)


def test_kdvli_fiyat():
    assert kdvli_fiyat(100) == 120
    assert kdvli_fiyat(0) == 0
    assert kdvli_fiyat(9.99) == 11.99
