from arama_tum_konumlar import tum_konumlari_bul


def test_birden_fazla_konum():
    assert tum_konumlari_bul([3, 6, 1, 6, 2, 6, 4], 6) == [1, 3, 5]


def test_hic_yok():
    assert tum_konumlari_bul([1, 2, 3], 9) == []


def test_bos_liste():
    assert tum_konumlari_bul([], 1) == []


def test_girdi_degismez():
    liste = [5, 5, 5]
    assert tum_konumlari_bul(liste, 5) == [0, 1, 2]
    assert liste == [5, 5, 5]
