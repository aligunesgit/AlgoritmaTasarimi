from uygula_arama import dogrusal_adim, dogrusal_ara, ikili_adim, ikili_ara


def test_dogrusal_bulur_ve_bulamaz():
    liste = [42, 7, 19, 3]
    assert dogrusal_ara(liste, 19) == 2
    assert dogrusal_ara(liste, 100) == -1


def test_ikili_bulur_ve_bulamaz():
    sirali = [3, 7, 19, 42, 58]
    assert ikili_ara(sirali, 3) == 0
    assert ikili_ara(sirali, 58) == 4
    assert ikili_ara(sirali, 20) == -1


def test_bos_liste():
    assert dogrusal_ara([], 5) == -1
    assert ikili_ara([], 5) == -1


def test_iki_yontem_ayni_indeksi_verir():
    sirali = list(range(0, 100, 3))
    for hedef in range(-2, 105):
        assert dogrusal_ara(sirali, hedef) == ikili_ara(sirali, hedef)


def test_adim_sayilari_en_kotu_durum():
    sayilar = list(range(1_000))
    assert dogrusal_adim(sayilar, -1) == 1_000
    assert ikili_adim(sayilar, -1) <= 10  # 2 üzeri 10 = 1024 ≥ 1000
