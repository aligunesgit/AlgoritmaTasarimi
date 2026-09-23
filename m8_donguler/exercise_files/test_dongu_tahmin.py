from dongu_tahmin import deneme_sayisi, tahmin_degerlendir


def test_ipuclari():
    assert tahmin_degerlendir(30, 42) == "Daha büyük bir sayı deneyin."
    assert tahmin_degerlendir(60, 42) == "Daha küçük bir sayı deneyin."
    assert tahmin_degerlendir(42, 42) == "Doğru!"


def test_ilk_denemede_bulma():
    assert deneme_sayisi(7, [7, 3, 9]) == 1


def test_break_sonrasi_tahminler_sayilmaz():
    # Hedef 3. denemede bulunur; sonraki iki tahmin sayılmamalı.
    assert deneme_sayisi(42, [50, 25, 42, 42, 10]) == 3


def test_hic_bulunamazsa():
    assert deneme_sayisi(42, [1, 2, 3]) == -1
    assert deneme_sayisi(42, []) == -1
