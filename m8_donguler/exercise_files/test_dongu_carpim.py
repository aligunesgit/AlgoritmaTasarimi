from dongu_carpim import carpim_sayisi, carpim_tablosu


def test_bir_boyutlu_tablo():
    assert carpim_tablosu(1) == "1 x 1 = 1\n"


def test_uc_boyutlu_tablo():
    tablo = carpim_tablosu(3)
    satirlar = tablo.splitlines()
    assert len(satirlar) == 9
    assert satirlar[0] == "1 x 1 = 1"
    assert "2 x 3 = 6" in satirlar
    assert satirlar[-1] == "3 x 3 = 9"


def test_sifir_boyut_bos_metin():
    assert carpim_tablosu(0) == ""


def test_ic_ice_dongu_n_kare_kez_calisir():
    assert carpim_sayisi(10) == 100
    assert carpim_sayisi(0) == 0
