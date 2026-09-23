import random

from arama_dogrusal import dogrusal_ara, dogrusal_ara_sayarak


def test_bulunan_eleman():
    assert dogrusal_ara([72, 45, 90, 38], 90) == 2


def test_bulunmayan_eleman():
    assert dogrusal_ara([72, 45, 90, 38], 100) == -1


def test_bos_liste():
    assert dogrusal_ara([], 5) == -1


def test_tekrarli_elemanda_ilk_indeks():
    assert dogrusal_ara([4, 7, 4, 7], 7) == 1


def test_karsilastirma_en_iyi_ve_en_kotu_durum():
    liste = [10, 20, 30, 40, 50]
    assert dogrusal_ara_sayarak(liste, 10) == (0, 1)  # en iyi durum: ilk eleman
    assert dogrusal_ara_sayarak(liste, 50) == (4, 5)  # son eleman: n karşılaştırma
    assert dogrusal_ara_sayarak(liste, 99) == (-1, 5)  # yok: yine n karşılaştırma


def test_list_index_ile_ayni_sonuc():
    rastgele = random.Random(2031)  # sabit tohum: test her çalıştırmada aynı listeleri üretir
    for _ in range(200):
        liste = [rastgele.randint(0, 20) for _ in range(rastgele.randint(0, 15))]
        hedef = rastgele.randint(0, 20)
        beklenen = liste.index(hedef) if hedef in liste else -1
        assert dogrusal_ara(liste, hedef) == beklenen
