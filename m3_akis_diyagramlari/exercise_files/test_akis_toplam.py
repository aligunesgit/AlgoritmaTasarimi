from akis_toplam import ilk_n_toplam


def test_iz_tablosu_ornegi():
    assert ilk_n_toplam(4) == 10


def test_bir():
    assert ilk_n_toplam(1) == 1


def test_sifir_ve_negatif():
    # Döngü koşulu ilk kontrolde yanlış olur, gövde hiç çalışmaz.
    assert ilk_n_toplam(0) == 0
    assert ilk_n_toplam(-3) == 0


def test_gauss_formulu_ile_ayni():
    for n in range(1, 50):
        assert ilk_n_toplam(n) == n * (n + 1) // 2
