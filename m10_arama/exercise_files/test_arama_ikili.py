import random
from bisect import bisect_left

from arama_ikili import ikili_ara, ikili_ara_sayarak


def test_bulunan_eleman():
    liste = [3, 8, 12, 17, 23, 31, 42, 56, 64, 77, 85]
    assert ikili_ara(liste, 64) == 8


def test_bulunmayan_eleman():
    liste = [3, 8, 12, 17, 23, 31, 42, 56, 64, 77, 85]
    assert ikili_ara(liste, 20) == -1
    assert ikili_ara(liste, 1) == -1  # en küçükten küçük
    assert ikili_ara(liste, 100) == -1  # en büyükten büyük


def test_bos_ve_tek_elemanli_liste():
    assert ikili_ara([], 5) == -1
    assert ikili_ara([5], 5) == 0
    assert ikili_ara([5], 4) == -1


def test_ilk_ve_son_eleman():
    liste = [2, 4, 6, 8, 10, 12]
    assert ikili_ara(liste, 2) == 0
    assert ikili_ara(liste, 12) == 5


def test_iz_tablosundaki_adim_sayilari():
    liste = [3, 8, 12, 17, 23, 31, 42, 56, 64, 77, 85]
    assert ikili_ara_sayarak(liste, 23) == (4, 4)  # README §4.3, birinci iz tablosu
    assert ikili_ara_sayarak(liste, 20) == (-1, 4)  # README §4.3, ikinci iz tablosu


def test_bin_elemanda_en_fazla_on_karsilastirma():
    liste = list(range(1, 1001))
    for hedef in range(0, 1002):  # listedeki her değer ve iki kenardaki eksik değerler
        _, adim = ikili_ara_sayarak(liste, hedef)
        assert adim <= 10


def test_tekrarli_elemanlar():
    liste = [1, 3, 3, 3, 5, 7]
    indeks = ikili_ara(liste, 3)
    assert liste[indeks] == 3  # eşit elemanlardan herhangi biri olabilir


def test_bisect_ile_ayni_sonuc():
    rastgele = random.Random(2031)  # sabit tohum
    for _ in range(300):
        liste = sorted(rastgele.sample(range(100), rastgele.randint(0, 30)))  # tekrarsız, sıralı
        hedef = rastgele.randint(-5, 105)
        i = bisect_left(liste, hedef)
        beklenen = i if i < len(liste) and liste[i] == hedef else -1
        assert ikili_ara(liste, hedef) == beklenen
