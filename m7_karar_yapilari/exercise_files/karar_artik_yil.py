"""M7 - İç içe koşullar ve düzleştirme: Gregoryen takvimde artık yıl kontrolü."""


def artik_yil_mi_ic_ice(yil: int) -> bool:
    """Artık yıl kuralını akış şemasındaki gibi iç içe kararlarla uygular."""
    if yil % 4 == 0:
        if yil % 100 == 0:
            if yil % 400 == 0:  # noqa: SIM103 (akış şemasıyla birebir olsun diye bilerek açık yazıldı)
                return True  # 400'e bölünen yüzyıllar artıktır (2000)
            else:
                return False  # 400'e bölünmeyen yüzyıllar artık değildir (1900)
        else:
            return True  # 4'e bölünen, 100'e bölünmeyen yıllar artıktır (2024)
    else:
        return False  # 4'e bölünmeyen yıllar artık değildir (2023)


def artik_yil_mi(yil: int) -> bool:
    """Aynı kuralın mantıksal operatörlerle düzleştirilmiş hâli."""
    return yil % 4 == 0 and (yil % 100 != 0 or yil % 400 == 0)


if __name__ == "__main__":
    girilen = int(input("Yıl: "))
    if artik_yil_mi(girilen):
        print(f"{girilen} artık yıldır (366 gün).")
    else:
        print(f"{girilen} artık yıl değildir (365 gün).")
