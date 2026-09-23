from karar_kargo import KARGO_UCRETI, kargo_ucreti, odenecek_tutar


def test_esigin_alti_ve_ustu():
    assert kargo_ucreti(499.99) == KARGO_UCRETI
    assert kargo_ucreti(500.01) == 0


def test_tam_esikte_kargo_bedava():
    # Sınır değer: 500 TL "500 ve üzeri" kapsamındadır (bkz. M7 §3, Kendinizi deneyin).
    assert kargo_ucreti(500) == 0


def test_ogrenci_olmayan():
    assert odenecek_tutar(100, False) == 149.9
    assert odenecek_tutar(600, False) == 600


def test_ogrenci_indirimi():
    assert odenecek_tutar(100, True) == 139.9  # 90 + 49.90
    # Eşik indirimden önceki tutara bakar: 500 TL'lik sepet indirimle 450 olur ama kargo yine bedava.
    assert odenecek_tutar(500, True) == 450
