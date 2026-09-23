from uygula_tekrar import tekrar_var_ic_ice, tekrar_var_kume, tekrar_var_sirali

YONTEMLER = [tekrar_var_ic_ice, tekrar_var_sirali, tekrar_var_kume]


def test_tekrar_var():
    for yontem in YONTEMLER:
        assert yontem([3, 8, 1, 8, 5]) is True


def test_tekrar_yok():
    for yontem in YONTEMLER:
        assert yontem([3, 8, 1, 5]) is False


def test_bos_ve_tek_elemanli_liste():
    for yontem in YONTEMLER:
        assert yontem([]) is False
        assert yontem([7]) is False


def test_tekrar_basta_ve_sonda():
    for yontem in YONTEMLER:
        assert yontem([4, 1, 2, 3, 4]) is True


def test_orijinal_liste_degismez():
    liste = [5, 3, 9, 1]
    tekrar_var_sirali(liste)
    assert liste == [5, 3, 9, 1]
