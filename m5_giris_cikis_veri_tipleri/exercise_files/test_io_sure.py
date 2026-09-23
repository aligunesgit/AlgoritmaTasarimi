from io_sure import sure_bicimle


def test_sifir():
    assert sure_bicimle(0) == "00:00:00"


def test_tipik_deger():
    assert sure_bicimle(3725) == "01:02:05"


def test_bir_gunden_bir_saniye_eksik():
    assert sure_bicimle(86399) == "23:59:59"


def test_tam_bir_dakika():
    assert sure_bicimle(60) == "00:01:00"


def test_24_saatten_uzun():
    # Gün hesabı yapmıyoruz; saat 24'ü geçebilir.
    assert sure_bicimle(90000) == "25:00:00"
