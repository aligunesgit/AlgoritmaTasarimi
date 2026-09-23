import random

from siralama_ekleme import ekleme_sirala, ekleme_sirala_sayarak


def test_ornek_liste():
    assert ekleme_sirala([5, 2, 9, 1, 6]) == [1, 2, 5, 6, 9]


def test_bos_ve_tek_elemanli_liste():
    assert ekleme_sirala([]) == []
    assert ekleme_sirala([42]) == [42]


def test_tekrarli_elemanlar():
    assert ekleme_sirala([3, 1, 3, 2, 1, 3]) == [1, 1, 2, 3, 3, 3]


def test_zaten_sirali_ve_ters_sirali():
    assert ekleme_sirala([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert ekleme_sirala([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_negatif_sayilar():
    assert ekleme_sirala([0, -3, 7, -1]) == [-3, -1, 0, 7]


def test_girdi_listesi_degismez():
    liste = [5, 2, 9, 1, 6]
    sonuc = ekleme_sirala(liste)
    assert liste == [5, 2, 9, 1, 6]  # orijinal olduğu gibi kaldı
    assert sonuc is not liste  # yeni bir liste döndü


def test_sayilar_ders_notundaki_tabloyla_ayni():
    sirali, *sayilar = ekleme_sirala_sayarak([5, 2, 9, 1, 6])
    assert sirali == [1, 2, 5, 6, 9]
    assert tuple(sayilar) == (7, 5)
    _, *sayilar = ekleme_sirala_sayarak([1, 2, 5, 6, 9])  # zaten sıralı
    assert tuple(sayilar) == (4, 0)


def test_rastgele_listelerde_sorted_ile_ayni_sonuc():
    rastgele = random.Random(2031)  # sabit tohum: test her çalıştırmada aynı listeleri üretir
    for _ in range(300):
        uzunluk = rastgele.randint(0, 25)
        liste = [rastgele.randint(-50, 50) for _ in range(uzunluk)]
        assert ekleme_sirala(liste) == sorted(liste)
        assert ekleme_sirala_sayarak(liste)[0] == sorted(liste)
