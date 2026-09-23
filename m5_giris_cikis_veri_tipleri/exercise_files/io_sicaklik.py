"""M5 - Sıcaklık dönüştürücü: girdi (str) → dönüşüm (float) → biçimli çıktı."""


def celsiustan_fahrenheita(celsius: float) -> float:
    """Celsius değerini Fahrenheit'a çevirir: F = C * 9 / 5 + 32."""
    return celsius * 9 / 5 + 32


def sicaklik_raporu(celsius: float) -> str:
    """Dönüşüm sonucunu tek ondalık basamakla biçimlendirilmiş bir cümle olarak döndürür."""
    fahrenheit = celsiustan_fahrenheita(celsius)
    return f"{celsius:.1f} °C = {fahrenheit:.1f} °F"


if __name__ == "__main__":
    metin = input("Sıcaklık (°C): ")  # GİRDİ: input() her zaman str döndürür
    derece = float(metin)  # İŞLEM öncesi: str → float dönüşümü
    print(sicaklik_raporu(derece))  # ÇIKTI
