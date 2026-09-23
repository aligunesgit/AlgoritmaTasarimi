from akis_vki import vki_hesapla, vki_kategori


def test_vki_hesapla():
    assert vki_hesapla(70, 1.75) == 22.9
    assert vki_hesapla(50, 1.0) == 50.0


def test_kategoriler():
    assert vki_kategori(17.0) == "Zayıf"
    assert vki_kategori(22.9) == "Normal"
    assert vki_kategori(27.0) == "Fazla kilolu"
    assert vki_kategori(35.0) == "Obez"


def test_sinir_degerleri():
    # Sınır değer bir üst kategoriye aittir: 18.5 Normal, 25 Fazla kilolu, 30 Obez.
    assert vki_kategori(18.5) == "Normal"
    assert vki_kategori(25) == "Fazla kilolu"
    assert vki_kategori(30) == "Obez"
