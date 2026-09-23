from operator_zaman import saat_dakika_saniye


def test_sifir():
    assert saat_dakika_saniye(0) == "0 sa 0 dk 0 sn"


def test_bir_dakikadan_az():
    assert saat_dakika_saniye(59) == "0 sa 0 dk 59 sn"


def test_tam_dakika_siniri():
    assert saat_dakika_saniye(60) == "0 sa 1 dk 0 sn"


def test_karisik():
    assert saat_dakika_saniye(3725) == "1 sa 2 dk 5 sn"


def test_bir_gun():
    # Gün birimi yok; 24 saat olarak gösterilir.
    assert saat_dakika_saniye(86400) == "24 sa 0 dk 0 sn"
