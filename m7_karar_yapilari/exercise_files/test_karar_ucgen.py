from karar_ucgen import ucgen_turu


def test_eskenar():
    assert ucgen_turu(3, 3, 3) == "Eşkenar"


def test_ikizkenar_her_konumda():
    # Eşit kenar çifti hangi konumda olursa olsun yakalanmalı.
    assert ucgen_turu(5, 5, 3) == "İkizkenar"
    assert ucgen_turu(5, 3, 5) == "İkizkenar"
    assert ucgen_turu(3, 5, 5) == "İkizkenar"


def test_cesitkenar():
    assert ucgen_turu(3, 4, 5) == "Çeşitkenar"


def test_sifir_ve_negatif_kenar():
    assert ucgen_turu(0, 4, 5) == "Geçersiz"
    assert ucgen_turu(3, -4, 5) == "Geçersiz"


def test_ucgen_esitsizligi_siniri():
    # 1 + 2 = 3: kenarlar düz bir çizgi oluşturur, üçgen değildir (sınır değer).
    assert ucgen_turu(1, 2, 3) == "Geçersiz"
    assert ucgen_turu(1, 2, 2.5) == "Çeşitkenar"
    assert ucgen_turu(10, 1, 1) == "Geçersiz"
