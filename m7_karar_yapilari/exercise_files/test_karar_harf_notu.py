from karar_harf_notu import harf_notu

# Her dal ve her eşiğin iki yanı için bir test (bkz. M7 §6, sınır değer testi).


def test_gecersiz_puanlar():
    assert harf_notu(-1) == "Geçersiz"
    assert harf_notu(101) == "Geçersiz"


def test_uc_noktalar_gecerli():
    assert harf_notu(0) == "FF"
    assert harf_notu(100) == "AA"


def test_ff_dd_siniri():
    assert harf_notu(49) == "FF"
    assert harf_notu(50) == "DD"


def test_dd_cc_siniri():
    assert harf_notu(59) == "DD"
    assert harf_notu(60) == "CC"


def test_cc_bb_siniri():
    assert harf_notu(74) == "CC"
    assert harf_notu(75) == "BB"


def test_bb_aa_siniri():
    assert harf_notu(89) == "BB"
    assert harf_notu(90) == "AA"


def test_ondalikli_puan():
    assert harf_notu(89.5) == "BB"
    assert harf_notu(49.99) == "FF"
