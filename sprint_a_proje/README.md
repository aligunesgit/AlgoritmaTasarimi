# 🚀 Proje Sprinti A

<p align="center"><em>Hafta 8 (ara sınav haftası)</em></p>

Bu haftada yeni konu anlatılmaz. Öğrenciler M1–M7'de öğrendiklerini (algoritma tasarlama, akış
diyagramı, giriş/çıkış, veri tipleri, operatörler, karar yapıları) tek bir küçük projede birleştirir.

## 🧭 Amaç

Dönemin ilk yarısında bir problemi adım adım çözmenin araçlarını tek tek gördük. Bu sprintte hepsini
bir arada kullanacaksınız: bir problemi anlayıp girdi ve çıktılarını belirleyecek, çözümü önce
**sözde kod** ve **akış diyagramı** ile tasarlayacak, sonra **Python**'da yazıp **testlerle**
doğrulayacaksınız. Bu, [Projeler](../pages/projects.md) sayfasında anlatılan üç temsilin ilk
uygulamasıdır.

Proje **bireyseldir** (öğretim üyesi farklı duyurmadıkça). Amaç büyük bir program yazmak değil,
küçük bir problemi baştan sona **düzgün** çözmektir.

!!! warning "Yalnızca M1–M7 araçları"

    Bu projede **döngü ve liste kullanılmaz**; bunları M8'de göreceğiz. Programınız bir kez çalışır:
    girdileri alır, kararları verir, sonucu yazar ve biter. Kullanabileceğiniz araçlar: `input()`,
    `print()`, `int()`, `float()`, `str`, `bool`, değişkenler, sabitler, aritmetik ve karşılaştırma
    operatörleri, `and` / `or` / `not`, `if` / `elif` / `else` ve iç içe kararlar.

## 🎯 Beklenen çıktılar

* Problemin tanımı ve girdi/çıktı listesi
* Sözde kod
* Akış diyagramı (draw.io, Mermaid veya Flowgorithm)
* Python sürümü ve en az üç test durumu

## 💡 Proje konuları

Aşağıdaki konulardan **birini** seçin. Kendi konunuzu önermek isterseniz, aynı zorlukta olduğundan ve
yalnızca M1–M7 araçlarıyla çözülebildiğinden emin olup sprintin ilk günü öğretim üyesine onaylatın.

### A1. Vücut kitle indeksi ve sağlık tavsiyesi

Kullanıcıdan kilo (kg) ve boy (m) alınır, vücut kitle indeksi (VKİ = kilo / boy²) hesaplanır ve
Dünya Sağlık Örgütü'nün yetişkinler için kullandığı sınıflara göre bir kategori ile kısa bir tavsiye
yazılır. Program bir sağlık teşhisi değil, bir hesaplama alıştırmasıdır.

* VKİ'yi iki ondalık basamakla yazmak
* En az dört kategori: zayıf (< 18,5), normal (18,5–24,9), fazla kilolu (25–29,9), obez (≥ 30)
* Sıfır ya da negatif boy/kilo girilirse hata mesajı vermek

### A2. Kargo ücret hesaplayıcı

Bir kargo firmasının ücretini paketin ağırlığına, mesafe bölgesine (şehir içi / yakın / uzak) ve
teslimat türüne (standart / hızlı) göre hesaplayan bir program. Ücret tarifesini siz belirleyin ve
README'de tablo olarak yazın.

* En az üç ağırlık kademesi ve üç bölge
* Hızlı teslimat için ek ücret, belirli bir tutarın üstünde ücretsiz kargo gibi en az bir kural
* Geçersiz bölge kodu ya da negatif ağırlık için uyarı

### A3. Not hesaplama sistemi

Bir öğrencinin vize, final ve ödev notlarını alıp ağırlıklı ortalamasını hesaplayan, harf notunu ve
geçme durumunu belirleyen bir program. Ağırlıkları ve harf aralıklarını sabit (M6) olarak tanımlayın.

* Ağırlıklı ortalama ve harf notu (ör. AA, BA, ..., FF)
* Finalden belirli bir notun altında alan öğrencinin ortalamadan bağımsız olarak kalması gibi en az
  bir ek kural
* 0–100 aralığı dışındaki notları reddetmek

### A4. Otopark ücreti

Giriş ve çıkış saatini (saat ve dakika olarak) alıp kalınan süreyi ve ücreti hesaplayan bir program.
Tarife kademeli olmalı (ör. ilk 1 saat sabit, sonrası saat başı) ve günlük bir üst sınırı olmalı.

* Süreyi dakika cinsinden hesaplamak ve kademeye göre ücretlendirmek (`//` ve `%` operatörleri)
* Abone ya da engelli sürücü için indirim gibi en az bir özel durum
* Çıkış saati girişten önceyse (aynı gün varsayımıyla) hata mesajı

### A5. Basit hesap makinesi

İki sayı ve bir işlem işareti (`+`, `-`, `*`, `/`, `//`, `%`, `**`) alıp sonucu yazan bir program.
Kullanıcının hatalı girişlerine karşı dayanıklı olmalı.

* Yedi işlemin tamamı
* Sıfıra bölmede program çökmeden anlamlı bir mesaj
* Tanınmayan işlem işareti için uyarı; sonucu tam sayıysa ondalıksız yazmak

## 📦 Teslim paketi

Tüm dosyalar tek bir klasörde, sıkıştırılmış olarak (ya da öğretim üyesinin belirttiği ortamda)
teslim edilir. Örnek klasör yapısı (A1 için):

```text
ad_soyad_sprint_a/
├── README.md          ← problem tanımı, girdi/çıktı listesi, nasıl çalıştırılır
├── sozde_kod.md       ← ders standardında sözde kod (M2)
├── akis_diyagrami.png ← ya da .drawio / .fprg / Mermaid içeren .md
├── vki.py             ← program: mantık fonksiyonda, input/print __main__ bloğunda
└── test_vki.py        ← en az üç pytest testi
```

* **README.md:** Problemin 3–5 cümlelik tanımı, girdi/çıktı tablosu (ad, tip, birim, geçerli aralık),
  varsayımlarınız ve çalıştırma komutları (`uv run python vki.py`, `uv run pytest`).
* **Sözde kod:** [M2](../m2_tasarim_teknikleri/README.md)'deki standarda uyun (`BAŞLA`, `OKU`, `EĞER ... İSE`, `←`).
* **Akış diyagramı:** [M3](../m3_akis_diyagramlari/README.md)'teki sembollerle; her karar kutusunun
  iki çıkışı etiketli olmalı.
* **Python:** Hesaplama ve karar mantığını M1'deki gibi bir fonksiyona koyun (ör.
  `def vki_kategori(kilo: float, boy: float) -> str:`), `input()` ve `print()` yalnızca
  `if __name__ == "__main__":` bloğunda olsun. Böylece fonksiyonu test edebilirsiniz.
* **Testler:** En az üç test: bir normal durum, bir **sınır değer** (ör. VKİ tam 25,0) ve bir
  **geçersiz girdi**.

## 🗓️ Sprint haftası çalışma planı

| Oturum | Yapılacaklar | O günün çıktısı |
|---|---|---|
| **1. gün** | Konuyu seç, problemi anla (Pólya 1. adım), girdi/çıktı listesini ve kuralları yaz. Kendi konunu seçtiysen onaylat. | README taslağı, girdi/çıktı tablosu |
| **2. gün** | Sözde kodu yaz; aynı mantığı akış diyagramına dök. İkisini kâğıt üzerinde örnek girdilerle "elle çalıştır". | `sozde_kod.md`, akış diyagramı |
| **3. gün** | Python'a çevir. Önce fonksiyonu yaz, sonra `__main__` bloğunu ekle. [Python Tutor](https://pythontutor.com/) ile adım adım izle. | Çalışan `.py` dosyası |
| **4. gün** | Test yaz ve çalıştır; sınır değerleri ve geçersiz girdileri dene. Bulduğun hataları düzelt, sözde kodu ve diyagramı da güncelle. | `test_*.py`, geçen testler |
| **5. gün** | README'yi tamamla, üç temsilin birbiriyle tutarlı olduğunu kontrol et, teslim et. | Teslim paketi |

!!! tip "Üç temsil aynı algoritmayı anlatmalı"

    Değerlendirmede en sık görülen sorun, kodun sonradan değişip sözde kod ve akış diyagramının
    eski hâlinde kalmasıdır. Koddaki her `if`/`elif` için akış diyagramında bir karar kutusu ve
    sözde kodda bir `EĞER` / `DEĞİLSE EĞER` satırı olmalı.

## 📋 Değerlendirme

| Ölçüt | Ağırlık | Tam puan için |
|---|---:|---|
| Problem tanımı ve girdi/çıktı listesi | %10 | Girdiler, çıktılar, birimler, geçerli aralıklar ve varsayımlar açıkça yazılmış |
| Sözde kod | %20 | Ders standardına uygun, belirli ve sonlu; tüm kurallar ve hata durumları var |
| Akış diyagramı | %20 | Doğru semboller; her karar iki etiketli çıkışlı; sözde kod ve kodla birebir tutarlı |
| Python doğruluğu | %25 | Tüm zorunlu özellikler çalışıyor; geçersiz girdilerde program anlamlı mesaj veriyor |
| Testler | %15 | En az üç test; normal durum, sınır değer ve geçersiz girdi kapsanmış; hepsi geçiyor |
| Kod okunabilirliği | %10 | Anlamlı Türkçe değişken adları, sabitler, docstring, gereksiz tekrar yok |
| **Toplam** | **%100** | |

## 🤝 Akademik dürüstlük ve yapay zekâ araçları

Arkadaşlarınızla fikir alışverişi yapabilir, dersin materyallerinden ve belgelerden yararlanabilirsiniz;
ancak teslim ettiğiniz sözde kod, akış diyagramı ve kod **sizin** olmalıdır. Başkasının çözümünü
kopyalamak ya da kendi çözümünüzü paylaşmak akademik dürüstlük ihlalidir.

Yapay zekâ araçlarını (sohbet botları, kod asistanları) bir konuyu anlamak ya da bir hata mesajını
yorumlamak için kullanabilirsiniz. Kullandıysanız README'nin sonuna kısa bir **beyan** ekleyin: hangi
aracı, hangi amaçla kullandınız. Beyan edilen kullanım cezalandırılmaz; beyan edilmeyen kullanım
dürüstlük sorunu sayılır. Her durumda, teslim ettiğiniz **her satırı açıklayabilmelisiniz**; öğretim
üyesi kodunuzu sizinle birlikte kısa bir görüşmede inceleyebilir. Ayrıntılı kurallar için öğretim
üyesinin duyurularını esas alın.
