from ortalama import ortalama


def test_tam_sayilar():
    assert ortalama(4, 6) == 5


def test_ondalikli_sonuc():
    # Tam sayı bölmesi (//) kullanılsaydı sonuç 3 olurdu (bkz. M1 §2, "Geriye bak").
    assert ortalama(3, 4) == 3.5


def test_negatif_sayilar():
    assert ortalama(-2, 2) == 0
