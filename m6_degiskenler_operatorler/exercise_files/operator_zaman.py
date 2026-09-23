"""M6 - Saniyeyi saat, dakika ve saniyeye çevirir (// ve % operatörleri)."""

SANIYE_PER_DAKIKA = 60
SANIYE_PER_SAAT = 60 * SANIYE_PER_DAKIKA


def saat_dakika_saniye(toplam_saniye: int) -> str:
    """Toplam saniyeyi "S sa D dk N sn" biçiminde bir metne çevirir.

    Örnek: 3725 saniye -> "1 sa 2 dk 5 sn".
    """
    saat = toplam_saniye // SANIYE_PER_SAAT  # kaç tam saat sığar?
    kalan = toplam_saniye % SANIYE_PER_SAAT  # saatlerden artan saniye
    dakika = kalan // SANIYE_PER_DAKIKA  # artandan kaç tam dakika çıkar?
    saniye = kalan % SANIYE_PER_DAKIKA  # en son artan saniye
    return f"{saat} sa {dakika} dk {saniye} sn"


if __name__ == "__main__":
    girilen = int(input("Toplam süre (saniye): "))
    print(saat_dakika_saniye(girilen))
