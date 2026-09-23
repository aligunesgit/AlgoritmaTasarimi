"""M6 - Formülleri koda dönüştürmek: sabitler, operatörler ve öncelik."""

import math

KDV_ORANI = 0.20  # sabit: BÜYÜK_HARF ile yazılır, program içinde değiştirilmez


def fahrenhayta_cevir(celsius: float) -> float:
    """Celsius cinsinden sıcaklığı Fahrenheit'a çevirir: F = C * 9/5 + 32."""
    return celsius * 9 / 5 + 32


def daire_alani(yaricap: float) -> float:
    """Yarıçapı verilen dairenin alanını döndürür: A = pi * r**2."""
    return math.pi * yaricap**2  # ** önce: önce kare, sonra çarpma


def kdvli_fiyat(fiyat: float) -> float:
    """KDV hariç fiyata KDV ekleyip kuruşa yuvarlanmış tutarı döndürür."""
    return round(fiyat * (1 + KDV_ORANI), 2)


if __name__ == "__main__":
    c = float(input("Sıcaklık (°C): "))
    print(f"{c} °C = {fahrenhayta_cevir(c)} °F")
    r = float(input("Dairenin yarıçapı: "))
    print(f"Alan: {round(daire_alani(r), 2)}")
    f = float(input("KDV hariç fiyat (TL): "))
    print(f"KDV dahil: {kdvli_fiyat(f)} TL")
