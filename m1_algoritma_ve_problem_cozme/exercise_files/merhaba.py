"""M1 - İlk program: kullanıcıyı adıyla selamlar."""


def selamla(ad: str) -> str:
    """Verilen ada göre bir selam cümlesi döndürür."""
    return f"Merhaba, {ad}!"


if __name__ == "__main__":
    kullanici = input("Adınız nedir? ")
    print(selamla(kullanici))
