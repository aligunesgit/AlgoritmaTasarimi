import calendar

from karar_artik_yil import artik_yil_mi, artik_yil_mi_ic_ice


def test_dorde_bolunmeyen():
    assert artik_yil_mi(2023) is False
    assert artik_yil_mi(2019) is False


def test_dorde_bolunen():
    assert artik_yil_mi(2024) is True
    assert artik_yil_mi(1996) is True


def test_yuze_bolunen_ama_dort_yuze_bolunmeyen():
    assert artik_yil_mi(1900) is False
    assert artik_yil_mi(2100) is False


def test_dort_yuze_bolunen():
    assert artik_yil_mi(2000) is True
    assert artik_yil_mi(1600) is True


def test_iki_surum_ayni():
    # Düzleştirme davranışı değiştirmemeli; Python'un hazır fonksiyonu da "ikinci görüş" verir.
    for yil in range(1583, 2401):  # döngüleri M8'de göreceğiz
        assert artik_yil_mi(yil) == artik_yil_mi_ic_ice(yil) == calendar.isleap(yil)
