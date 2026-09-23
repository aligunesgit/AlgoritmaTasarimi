from gorsel_takas import takas


def test_farkli_degerler():
    assert takas(3, 7) == (7, 3)


def test_esit_degerler():
    assert takas(5, 5) == (5, 5)


def test_sifir_ve_negatif():
    assert takas(0, -4) == (-4, 0)


def test_iki_kez_takas_ilk_duruma_dondurur():
    a, b = takas(1, 2)
    assert takas(a, b) == (1, 2)
