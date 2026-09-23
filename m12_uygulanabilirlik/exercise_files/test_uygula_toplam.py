from uygula_toplam import toplam_dongu, toplam_gauss


def test_kucuk_n():
    assert toplam_dongu(10) == 55
    assert toplam_gauss(10) == 55


def test_n_bir():
    assert toplam_dongu(1) == 1
    assert toplam_gauss(1) == 1


def test_sifir_ve_negatif():
    # Toplanacak sayı yoksa toplam 0'dır; iki yöntem de aynı cevabı vermeli.
    assert toplam_dongu(0) == 0
    assert toplam_gauss(0) == 0
    assert toplam_dongu(-5) == toplam_gauss(-5) == 0


def test_iki_yontem_ayni_sonucu_verir():
    for n in range(0, 200):
        assert toplam_dongu(n) == toplam_gauss(n)


def test_buyuk_n():
    assert toplam_gauss(1_000_000) == 500_000_500_000
