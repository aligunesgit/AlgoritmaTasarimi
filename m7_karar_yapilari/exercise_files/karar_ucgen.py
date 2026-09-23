"""M7 - İç içe kararlar: kenar uzunluklarına göre üçgen türü."""


def ucgen_turu(a: float, b: float, c: float) -> str:
    """Üçgenin türünü döndürür: "Eşkenar", "İkizkenar", "Çeşitkenar" ya da "Geçersiz"."""
    if a <= 0 or b <= 0 or c <= 0:
        return "Geçersiz"  # kenar uzunluğu pozitif olmalı
    elif a + b <= c or a + c <= b or b + c <= a:
        return "Geçersiz"  # üçgen eşitsizliği sağlanmıyor
    else:
        # Buraya yalnızca geçerli üçgenler gelir. Eşkenar kontrolü ikizkenardan ÖNCE gelmeli.
        if a == b and b == c:
            return "Eşkenar"
        elif a == b or b == c or a == c:  # noqa: SIM109 (sözde koddaki gibi açık yazıldı)
            return "İkizkenar"
        else:
            return "Çeşitkenar"


if __name__ == "__main__":
    k1 = float(input("1. kenar: "))
    k2 = float(input("2. kenar: "))
    k3 = float(input("3. kenar: "))
    print(ucgen_turu(k1, k2, k3))
