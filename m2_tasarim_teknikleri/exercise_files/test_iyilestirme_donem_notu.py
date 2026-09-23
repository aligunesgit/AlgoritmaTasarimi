from iyilestirme_donem_notu import agirlikli_ortalama


def test_varsayilan_agirlik():
    # 60 * 0.4 + 80 * 0.6 = 24 + 48 = 72
    assert agirlikli_ortalama(60, 80) == 72


def test_esit_notlar():
    assert agirlikli_ortalama(70, 70) == 70


def test_uc_degerler():
    assert agirlikli_ortalama(0, 0) == 0
    assert agirlikli_ortalama(100, 100) == 100


def test_farkli_agirlik_ve_yuvarlama():
    # 55 * 0.3 + 72 * 0.7 = 16.5 + 50.4 = 66.9
    assert agirlikli_ortalama(55, 72, vize_agirlik=0.3) == 66.9
