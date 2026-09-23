"""M8 - Bir not listesi üzerinde sayaç, toplayıcı ve en büyük/en küçük kalıpları."""


def not_ortalamasi(notlar: list[float]) -> float:
    """Notların ortalamasını döndürür. Liste boşsa 0.0 döndürür."""
    if len(notlar) == 0:
        return 0.0  # sıfıra bölmeyi önlüyoruz
    toplam = 0.0
    for not_degeri in notlar:
        toplam = toplam + not_degeri
    return toplam / len(notlar)


def gecen_sayisi(notlar: list[float]) -> int:
    """50 ve üzeri not alan öğrenci sayısını döndürür (sayaç kalıbı)."""
    sayac = 0
    for not_degeri in notlar:
        if not_degeri >= 50:
            sayac = sayac + 1
    return sayac


def en_yuksek_not(notlar: list[float]) -> float:
    """Listedeki en büyük notu döndürür. Liste boş olmamalıdır."""
    en_buyuk = notlar[0]  # ilk elemanı "şimdilik en büyük" kabul et
    for i in range(1, len(notlar)):
        if notlar[i] > en_buyuk:
            en_buyuk = notlar[i]
    return en_buyuk


def en_dusuk_not(notlar: list[float]) -> float:
    """Listedeki en küçük notu döndürür. Liste boş olmamalıdır."""
    en_kucuk = notlar[0]
    for not_degeri in notlar:
        if not_degeri < en_kucuk:
            en_kucuk = not_degeri
    return en_kucuk


def gecerli_notlarin_ortalamasi(notlar: list[float]) -> float:
    """0-100 aralığı dışındaki hatalı girişleri atlayarak ortalama hesaplar (continue)."""
    toplam = 0.0
    adet = 0
    for not_degeri in notlar:
        if not_degeri < 0 or not_degeri > 100:
            continue  # bu turu atla, sıradaki nota geç
        toplam = toplam + not_degeri
        adet = adet + 1
    if adet == 0:
        return 0.0
    return toplam / adet


if __name__ == "__main__":
    notlar: list[float] = []
    print("Notları tek tek girin. Bitirmek için -1 yazın.")
    while True:
        giris = float(input("Not: "))
        if giris == -1:
            break  # gözcü (sentinel) değer: döngüden çık
        notlar.append(giris)

    if len(notlar) == 0:
        print("Hiç not girilmedi.")
    else:
        print(f"Öğrenci sayısı : {len(notlar)}")
        print(f"Ortalama       : {not_ortalamasi(notlar):.2f}")
        print(f"Geçen sayısı   : {gecen_sayisi(notlar)}")
        print(f"En yüksek / en düşük: {en_yuksek_not(notlar)} / {en_dusuk_not(notlar)}")
