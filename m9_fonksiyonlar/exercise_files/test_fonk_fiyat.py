from fonk_fiyat import indirimli_fiyat, kdvli_fiyat, sepet_toplami


def test_varsayilan_oran():
    assert kdvli_fiyat(100) == 120.0


def test_oran_verilince_varsayilan_ezilir():
    assert kdvli_fiyat(100, 0.10) == 110.0
    assert kdvli_fiyat(100, oran=0) == 100.0


def test_anahtar_kelimeli_argumanlarda_sira_onemsiz():
    assert kdvli_fiyat(oran=0.01, fiyat=100) == kdvli_fiyat(100, 0.01)


def test_indirim():
    assert indirimli_fiyat(200) == 180.0
    assert indirimli_fiyat(200, yuzde=50) == 100.0
    assert indirimli_fiyat(200, yuzde=0) == 200.0


def test_sepet():
    assert sepet_toplami([40, 60]) == 120.0
    assert sepet_toplami([40, 60], indirim_yuzdesi=20) == 96.0
    assert sepet_toplami([40, 60], kdv_orani=0) == 100.0


def test_bos_sepet():
    assert sepet_toplami([]) == 0.0
