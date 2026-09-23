from uygula_asal import asal_mi_karekok, asal_mi_tum, deneme_sayisi_karekok, deneme_sayisi_tum

YONTEMLER = [asal_mi_tum, asal_mi_karekok]


def test_kucuk_asallar():
    for yontem in YONTEMLER:
        for p in [2, 3, 5, 7, 11, 13, 97]:
            assert yontem(p) is True


def test_asal_olmayanlar():
    for yontem in YONTEMLER:
        for sayi in [4, 9, 15, 25, 49, 91, 100]:
            assert yontem(sayi) is False


def test_uc_durumlar():
    # 0, 1 ve negatif sayılar asal değildir.
    for yontem in YONTEMLER:
        for sayi in [-7, 0, 1]:
            assert yontem(sayi) is False


def test_iki_yontem_uyumlu():
    for sayi in range(-3, 500):
        assert asal_mi_tum(sayi) == asal_mi_karekok(sayi)


def test_deneme_sayilari():
    # 1_000_003 asaldır: ilk yöntem 1_000_001, ikinci yöntem yalnızca 999 bölen dener.
    assert deneme_sayisi_tum(1_000_003) == 1_000_001
    assert deneme_sayisi_karekok(1_000_003) == 999
