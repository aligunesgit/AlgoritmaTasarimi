from operator_cift_tek import cift_mi, kati_mi


def test_cift_ve_tek():
    assert cift_mi(4) is True
    assert cift_mi(7) is False


def test_sifir_cifttir():
    assert cift_mi(0) is True


def test_negatif_sayilar():
    # Python'da -7 % 2 == 1 olduğu için negatiflerde de doğru çalışır (bkz. M6 §3.1).
    assert cift_mi(-4) is True
    assert cift_mi(-7) is False


def test_kati_mi():
    assert kati_mi(15, 5) is True
    assert kati_mi(16, 5) is False
    assert kati_mi(0, 3) is True
