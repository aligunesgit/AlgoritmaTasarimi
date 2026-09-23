"""M8 - İç içe döngülerle çarpım tablosu."""


def carpim_tablosu(n: int) -> str:
    """1'den n'e kadar çarpım tablosunu, her satırda bir çarpım olacak şekilde metin olarak döndürür."""
    metin = ""  # metin toplayıcı: boş metinle başlar
    for i in range(1, n + 1):  # dış döngü: satırlar
        for j in range(1, n + 1):  # iç döngü: her satır için tüm sütunlar
            metin = metin + f"{i} x {j} = {i * j}\n"
    return metin


def carpim_sayisi(n: int) -> int:
    """n x n çarpım tablosunda iç döngünün gövdesinin kaç kez çalıştığını sayar."""
    sayac = 0
    for _i in range(n):  # _ öneki: değişkeni gövdede kullanmıyoruz
        for _j in range(n):
            sayac = sayac + 1
    return sayac


if __name__ == "__main__":
    boyut = int(input("Tablo boyutu: "))
    print(carpim_tablosu(boyut), end="")
    print(f"Toplam {carpim_sayisi(boyut)} çarpım yapıldı.")
