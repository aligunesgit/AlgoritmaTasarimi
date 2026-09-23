from dongu_toplam import rakamlar_toplami, toplam_1den_n


def test_toplam_kucuk_n():
    assert toplam_1den_n(4) == 10


def test_toplam_gauss_formulu_ile_ayni():
    # Gauss formülü: n * (n + 1) / 2
    for n in range(1, 50):
        assert toplam_1den_n(n) == n * (n + 1) // 2


def test_toplam_sifir_ve_negatif():
    # Döngü hiç çalışmaz, toplayıcı başlangıç değerinde kalır.
    assert toplam_1den_n(0) == 0
    assert toplam_1den_n(-5) == 0


def test_rakamlar_toplami():
    assert rakamlar_toplami(472) == 13


def test_rakamlar_tek_basamak_ve_sifir():
    assert rakamlar_toplami(7) == 7
    assert rakamlar_toplami(0) == 0


def test_rakamlar_icinde_sifir_olan_sayi():
    assert rakamlar_toplami(1005) == 6
