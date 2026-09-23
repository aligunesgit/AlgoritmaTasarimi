from fonk_sicaklik import donusum_tablosu, fahrenheit


def test_bilinen_noktalar():
    assert fahrenheit(0) == 32
    assert fahrenheit(100) == 212


def test_iki_olcegin_kesistigi_nokta():
    # -40 derece iki ölçekte de aynıdır.
    assert fahrenheit(-40) == -40


def test_tablo_varsayilan_adim():
    tablo = donusum_tablosu(0, 30)
    assert tablo == ["0 C = 32.0 F", "10 C = 50.0 F", "20 C = 68.0 F", "30 C = 86.0 F"]


def test_tablo_ozel_adim_ve_tek_satir():
    assert len(donusum_tablosu(0, 100, adim=25)) == 5
    assert donusum_tablosu(5, 5) == ["5 C = 41.0 F"]
