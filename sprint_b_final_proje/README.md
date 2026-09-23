# 🏁 Proje Sprinti B (Final)

<p align="center"><em>Hafta 14</em></p>

Dönemin son haftası, problem çözme ve algoritma tasarlamaya yönelik final projesine ayrılmıştır.
Proje; döngüler, fonksiyonlar ve arama/sıralama algoritmalarından en az birini içermelidir.

## 🧭 Amaç

Final projesi dönemin tamamını bir araya getirir. [Proje Sprinti A](../sprint_a_proje/README.md)'da
tek seferlik bir hesaplamayı üç temsille (sözde kod, akış diyagramı, Python + testler) çözmüştünüz.
Bu kez problem daha büyüktür: bir **veri koleksiyonu** üzerinde çalışacak, işi **fonksiyonlara**
bölecek, **döngülerle** gezecek ve en az bir **arama ya da sıralama** algoritması kullanacaksınız.
Buna ek olarak, [M12](../m12_uygulanabilirlik/README.md)'deki gibi aynı alt problem için **iki farklı
algoritmayı karşılaştırıp** seçiminizi gerekçelendireceksiniz.

Proje **2–3 kişilik gruplarla** yapılır (öğretim üyesi farklı duyurmadıkça). Her grup üyesi projenin
tamamını anlamalı ve açıklayabilmelidir.

!!! info "Zorunlu bileşenler"

    Hangi konuyu seçerseniz seçin, projenizde şunlar bulunmalı:

    * En az bir liste ve onu gezen `for` / `while` döngüleri (M8)
    * Her biri tek bir iş yapan, parametre alıp değer döndüren en az dört fonksiyon (M9)
    * Kendi yazdığınız en az bir arama (M10) ya da sıralama (M11) algoritması. Python'un hazır
      `sorted()` fonksiyonunu **karşılaştırma için** kullanabilirsiniz, ama kendi sürümünüz de olmalı.
    * Aynı alt problem için iki algoritmanın adım sayısı ve/veya süre karşılaştırması (M12)

## 🎯 Beklenen çıktılar

* Problemin tanımı, girdi/çıktı listesi ve sözde kod
* Akış diyagramı
* Fonksiyonlara ayrılmış Python sürümü ve `pytest` testleri
* En az iki farklı algoritmanın karşılaştırıldığı kısa bir rapor (M12)

## 💡 Örnek proje konuları

Aşağıdaki konulardan **birini** seçin ya da aynı zorlukta kendi konunuzu sprintin ilk günü öğretim
üyesine onaylatın. Veriler program içinde bir liste olarak tanımlanabilir; dosyadan okumak zorunlu
değildir.

### B1. Öğrenci not yönetimi

Bir dersin öğrencilerini (numara, ad, not) tutan ve bunlar üzerinde işlem yapan bir program.
Kullanıcı bir menüden işlem seçer ve program o işlemi yaptıktan sonra menüye döner.

* Öğrenci ekleme, numaraya göre arama, sınıf ortalaması, en yüksek ve en düşük not
* Notlara göre sıralı başarı listesi (kendi sıralama fonksiyonunuzla)
* Karşılaştırma önerisi: numaraya göre doğrusal arama ile sıralı listede ikili arama

### B2. Kütüphane kitap arama

Başlık, yazar, yıl ve raf kodu bilgisi olan en az 30 kitaplık bir katalog. Kullanıcı başlığa ya da
yazara göre arama yapabilir, kitapları yıla göre sıralı listeleyebilir.

* Başlığın bir kısmıyla arama (ör. "algoritma" geçen tüm kitaplar)
* Yıla ya da başlığa göre sıralama; ödünç verme / iade durumu
* Karşılaştırma önerisi: her aramada doğrusal tarama ile bir kez sıralayıp ikili arama (M12 §5.3)

### B3. Basit envanter (stok) takibi

Bir kantinin ya da kırtasiyenin ürünlerini (kod, ad, adet, birim fiyat) tutan program. Satış ve stok
girişi yapıldıkça adetler güncellenir.

* Ürün ekleme, satış (stok yetersizse uyarı), stok girişi, toplam stok değeri
* Stoğu kritik seviyenin altına düşen ürünlerin listesi; fiyata ya da adede göre sıralama
* Karşılaştırma önerisi: aynı ürün kodunun iki kez eklenip eklenmediğini iç içe döngü ile kontrol
  etmek ve önce sıralayıp komşulara bakmak (M12 §5.2)

### B4. Kelime oyunu

Adam asmaca ya da kelime tahmin oyunu. Program bir kelime listesinden kelime seçer, kullanıcı harf
tahmin eder, program doğru harfleri gösterir ve hak sayısını takip eder.

* Tahmin edilen harfleri tutma, aynı harfin tekrar tahminini engelleme, kazanma/kaybetme durumu
* Oyun sonunda istatistik: en çok tahmin edilen harfler ya da en kısa sürede bilinen kelimeler (sıralı)
* Karşılaştırma önerisi: tahmin edilen harfin daha önce denenip denenmediğini liste ile ve `set` ile
  kontrol etmek

### B5. Sınav sonuç analizi

Bir sınavın sonuçlarını (öğrenci numarası ve puan) analiz eden program.

* Ortalama, ortanca (median), en yüksek/en düşük puan, standart sapma
* Puan aralıklarına göre dağılım (0–49, 50–69, 70–84, 85–100) ve metin tabanlı bir çubuk grafik (`*` ile)
* Karşılaştırma önerisi: ortanca için tam sıralama ile ilk yarıyı sıralayıp durmak; ya da kabarcık
  ile seçmeli sıralamanın karşılaştırma sayıları

## 📦 Teslim paketi

Örnek klasör yapısı (B2 için):

```text
grup_adi_sprint_b/
├── README.md               ← grup üyeleri, problem tanımı, girdi/çıktı, çalıştırma, iş bölümü
├── sozde_kod.md            ← ana akış + her fonksiyonun sözde kodu
├── akis_diyagramlari/
│   ├── ana_menu.png        ← programın genel akışı
│   └── ikili_arama.png     ← en az bir algoritmanın ayrıntılı akışı
├── kutuphane.py            ← fonksiyonlar + if __name__ == "__main__": bloğu
├── test_kutuphane.py       ← pytest testleri
└── karsilastirma.md        ← iki algoritmanın karşılaştırma raporu (M12)
```

* **README.md:** Grup üyeleri ve her üyenin katkısı, problem tanımı, girdi/çıktı tablosu,
  çalıştırma komutları (`uv run python kutuphane.py`, `uv run pytest`).
* **Sözde kod:** Ders standardında; ana akış ve her fonksiyon için `FONKSİYON ... FONKSİYON SONU` blokları.
* **Akış diyagramı:** En az iki diyagram: genel akış (menü döngüsü) ve seçtiğiniz arama/sıralama
  algoritmasının ayrıntılı diyagramı. Fonksiyon çağrıları için alt program sembolünü kullanın.
* **Python:** Her fonksiyonun tip ipuçları ve Türkçe docstring'i olsun. `input()` / `print()` yalnızca
  menü kısmında; hesaplayan fonksiyonlar değer döndürsün.
* **Testler:** Her hesaplayan fonksiyon için en az iki test; toplamda en az on test. Boş liste, tek
  elemanlı liste, bulunamayan eleman gibi uç durumlar mutlaka olsun. Karşılaştırdığınız iki
  algoritmanın **aynı sonucu verdiğini** gösteren bir test ekleyin.
* **Karşılaştırma raporu (1–2 sayfa):** Hangi alt problemi, hangi iki algoritmayla çözdünüz?
  Her birinin sözde kodu, Büyük-O tahmini, farklı `n` değerleri için adım sayısı ya da
  `time.perf_counter` ölçümü (tablo), ve hangisini neden seçtiğiniz (doğruluk, zaman, bellek,
  okunabilirlik, girdi özellikleri).

## 🗓️ Sprint haftası çalışma planı

Final projesine M12 haftasında başlamanız önerilir; sprint haftası tamamlama ve sunum haftasıdır.

| Oturum | Yapılacaklar | O günün çıktısı |
|---|---|---|
| **1. gün** | Grup ve konu kesinleşir. Problem tanımı, girdi/çıktı listesi, fonksiyon listesi ve iş bölümü. | README taslağı, fonksiyon listesi |
| **2. gün** | Sözde kod ve akış diyagramları. Karşılaştırılacak alt problem ve iki algoritma seçilir. | `sozde_kod.md`, diyagram taslakları |
| **3. gün** | Fonksiyonları yazma ve her biri yazılır yazılmaz testlerini ekleme. Menü döngüsünü en sona bırakın. | Çalışan fonksiyonlar + testler |
| **4. gün** | Karşılaştırma deneyi (adım sayma / zamanlama), rapor, kod temizliği, üç temsilin tutarlılık kontrolü. | `karsilastirma.md`, geçen testler |
| **5. gün** | Teslim ve kısa sunum: 5–7 dakika anlatım + canlı çalıştırma, ardından sorular. | Teslim paketi, sunum |

!!! tip "Sunumda ne anlatılır?"

    Problemi bir cümleyle tanıtın, programı canlı çalıştırın, `pytest` çıktısını gösterin ve
    karşılaştırma tablonuzu yorumlayın: "Hangi algoritmayı neden seçtik?" Sorular her grup üyesine
    ayrı ayrı yöneltilebilir.

## 📋 Değerlendirme

| Ölçüt | Ağırlık | Tam puan için |
|---|---:|---|
| Problem tanımı ve girdi/çıktı listesi | %5 | Kapsam, veriler ve varsayımlar açık |
| Sözde kod | %15 | Ders standardında; ana akış ve tüm fonksiyonlar; kodla tutarlı |
| Akış diyagramı | %10 | Doğru semboller; genel akış + en az bir algoritmanın ayrıntılı diyagramı |
| Python doğruluğu | %20 | Zorunlu bileşenler ve konu özellikleri çalışıyor; hatalı girişlerde çökmüyor |
| Testler | %15 | En az on test; uç durumlar; iki algoritmanın aynı sonucu verdiği test; hepsi geçiyor |
| Kod okunabilirliği | %10 | Tek iş yapan fonksiyonlar, anlamlı adlar, tip ipuçları, docstring, tekrar yok |
| Algoritma seçimi gerekçesi (karşılaştırma raporu) | %15 | Adım sayısı / ölçüm tablosu, Büyük-O tahmini, M12 ölçütleriyle ikna edici gerekçe |
| Kısa sunum | %10 | Süreye uyum, canlı çalıştırma, her üyenin sorulara cevap verebilmesi |
| **Toplam** | **%100** | |

## 🤝 Akademik dürüstlük ve yapay zekâ araçları

Grup içinde her şeyi paylaşabilirsiniz; gruplar arasında fikir tartışmak serbesttir, ama kod, sözde
kod, diyagram ve rapor paylaşılmaz. İnternetten ya da bir kitaptan uyarladığınız bir algoritma varsa
kaynağını README'de belirtin.

Yapay zekâ araçlarını (sohbet botları, kod asistanları) bir kavramı anlamak, hata mesajını yorumlamak
ya da yazdığınız kodu gözden geçirmek için kullanabilirsiniz. Kullandıysanız README'nin sonuna kısa bir
**beyan** ekleyin: hangi araç, hangi amaçla, projenin hangi kısmında. Beyan edilen kullanım
cezalandırılmaz; beyan edilmeyen kullanım dürüstlük sorunu sayılır. Her grup üyesi teslim edilen **her
satırı açıklayabilmelidir**; sunumdaki sorular bunu ölçmek içindir. Ayrıntılı kurallar için öğretim
üyesinin duyurularını esas alın.
