from io_fatura import KDV_ORANI, fatura_metni, kdv_tutari


def test_kdv_tutari():
    assert kdv_tutari(100, 0.20) == 20.0


def test_kdv_iki_basamaga_yuvarlanir():
    assert kdv_tutari(33.33, 0.20) == 6.67


def test_sifir_tutar():
    assert kdv_tutari(0, KDV_ORANI) == 0


def test_fatura_metni():
    beklenen = (
        "Ürün               Defter\nAra toplam      150.00 TL\nKDV (%20)        30.00 TL\nToplam          180.00 TL"
    )
    assert fatura_metni("Defter", 3, 50, 0.20) == beklenen


def test_fatura_farkli_oran():
    satirlar = fatura_metni("Ekmek", 2, 10, 0.01).split("\n")
    assert satirlar[2] == "KDV (%1)          0.20 TL"
    assert satirlar[3] == "Toplam           20.20 TL"
