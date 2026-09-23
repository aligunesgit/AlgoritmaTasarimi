"""M4 - Celsius'tan Fahrenheit'a dönüşüm, ara adımlarıyla birlikte."""


def fahrenheita_cevir(celsius: float) -> float:
    """Celsius cinsinden sıcaklığı Fahrenheit'a çevirir: F = C * 9 / 5 + 32.

    Formülü bilerek iki adıma bölüyoruz; Python Tutor'da her ara sonucun
    ayrı bir değişken olarak belirdiğini göreceksiniz.
    """
    carpim = celsius * 9 / 5  # 1. adım: ölçek farkı
    fahrenheit = carpim + 32  # 2. adım: sıfır noktası farkı
    return fahrenheit


if __name__ == "__main__":
    sicaklik = 25
    print(sicaklik, "°C =", fahrenheita_cevir(sicaklik), "°F")
