"""M9 - Bir fonksiyonu başka bir fonksiyonun içinden çağırmak: sıcaklık dönüşümü."""


def fahrenheit(celsius: float) -> float:
    """Celsius cinsinden sıcaklığı Fahrenheit'a çevirir."""
    return celsius * 9 / 5 + 32


def donusum_tablosu(baslangic: int, bitis: int, adim: int = 10) -> list[str]:
    """baslangic'tan bitis'e (dahil) kadar Celsius-Fahrenheit dönüşüm satırlarını döndürür."""
    satirlar: list[str] = []
    for c in range(baslangic, bitis + 1, adim):
        satirlar.append(f"{c} C = {fahrenheit(c):.1f} F")
    return satirlar


if __name__ == "__main__":
    for satir in donusum_tablosu(-10, 40):
        print(satir)
