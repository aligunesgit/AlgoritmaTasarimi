from akis_en_buyuk import en_buyuk_uc


def test_her_konumda_en_buyuk():
    assert en_buyuk_uc(9, 2, 5) == 9
    assert en_buyuk_uc(2, 9, 5) == 9
    assert en_buyuk_uc(2, 5, 9) == 9


def test_esit_sayilar():
    assert en_buyuk_uc(4, 4, 4) == 4
    assert en_buyuk_uc(7, 7, 1) == 7


def test_negatif_ve_ondalik():
    assert en_buyuk_uc(-5, -1, -3) == -1
    assert en_buyuk_uc(2.5, 2.4, 2.49) == 2.5
