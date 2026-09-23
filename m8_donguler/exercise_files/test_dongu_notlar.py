from dongu_notlar import en_dusuk_not, en_yuksek_not, gecen_sayisi, gecerli_notlarin_ortalamasi, not_ortalamasi

NOTLAR = [70, 85, 40, 55, 90]


def test_ortalama():
    assert not_ortalamasi(NOTLAR) == 68


def test_ortalama_bos_liste():
    assert not_ortalamasi([]) == 0.0


def test_gecen_sayisi_sinir_degeri():
    # 50 geçer, 49 geçmez: sınır değerini ayrıca deniyoruz.
    assert gecen_sayisi([49, 50, 51]) == 2
    assert gecen_sayisi(NOTLAR) == 4


def test_en_yuksek_ve_en_dusuk():
    assert en_yuksek_not(NOTLAR) == 90
    assert en_dusuk_not(NOTLAR) == 40


def test_en_buyuk_ilk_veya_son_elemanda():
    assert en_yuksek_not([100, 20, 30]) == 100
    assert en_yuksek_not([20, 30, 100]) == 100


def test_tek_elemanli_liste():
    assert en_yuksek_not([42]) == 42
    assert en_dusuk_not([42]) == 42


def test_tum_notlar_negatifse_en_buyuk():
    # en_buyuk = 0 ile başlasaydık bu test başarısız olurdu.
    assert en_yuksek_not([-5, -2, -9]) == -2


def test_gecersiz_notlar_atlanir():
    assert gecerli_notlarin_ortalamasi([80, -10, 60, 150]) == 70
    assert gecerli_notlarin_ortalamasi([-1, 101]) == 0.0
