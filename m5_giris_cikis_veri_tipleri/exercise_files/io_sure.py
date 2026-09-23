"""M5 - Toplam saniyeyi SS:DD:ss (saat:dakika:saniye) biçiminde gösterme."""


def sure_bicimle(toplam_saniye: int) -> str:
    """Toplam saniyeyi iki basamaklı saat:dakika:saniye metnine çevirir.

    // (tam bölme) ve % (kalan) operatörlerini M6'da ayrıntılı göreceğiz.
    Burada bilmeniz gereken: 3725 // 3600 = 1 (kaç tam saat), 3725 % 3600 = 125 (artan saniye).
    """
    saat = toplam_saniye // 3600
    kalan = toplam_saniye % 3600
    dakika = kalan // 60
    saniye = kalan % 60
    return f"{saat:02d}:{dakika:02d}:{saniye:02d}"


if __name__ == "__main__":
    girdi = int(input("Toplam saniye: "))
    print("Süre:", sure_bicimle(girdi))
