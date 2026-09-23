# Özet

Dersin konu akışı, temel kavramlardan algoritma karşılaştırmasına doğru ilerler:

```mermaid
flowchart TD
    A["M1 Algoritma ve problem çözme"] --> B["M2 Tasarlama teknikleri"]
    B --> C["M3 Akış diyagramları"]
    C --> D["M4 Görselleştirme"]
    D --> E["M5 Giriş/çıkış ve veri tipleri"]
    E --> F["M6 Değişkenler ve operatörler"]
    F --> G["M7 Karar yapıları"]
    G --> SA(["Sprint A"])
    SA --> H["M8 Döngüler"]
    H --> I["M9 Fonksiyonlar"]
    I --> J["M10 Arama"]
    J --> K["M11 Sıralama"]
    K --> L["M12 Uygulanabilirlik"]
    L --> SB(["Sprint B"])
```

## Modüller

| Modül | Özet |
|---|---|
| [M1](../m1_algoritma_ve_problem_cozme/README.md) | Algoritma nedir, iyi bir algoritmanın özellikleri, Pólya'nın dört adımı, derleyici ve yorumlayıcı, ilk Python programı ve ilk test. |
| [M2](../m2_tasarim_teknikleri/README.md) | Hesaplamalı düşünme: ayrıştırma, soyutlama, örüntü tanıma; adım adım iyileştirme; dersin sözde kod standardı; kaba kuvvet ile yarıya bölme. |
| [M3](../m3_akis_diyagramlari/README.md) | Akış şeması sembolleri, sıra/seçim/tekrar yapıları, çizim kuralları, iz tablosu ile elle yürütme, sözde kod ↔ akış şeması dönüşümü. |
| [M4](../m4_gorsellestirme/README.md) | draw.io, Mermaid, Flowgorithm, Python Tutor ve VisuAlgo ile algoritmaları ve akış şemalarını görselleştirme. |
| [M5](../m5_giris_cikis_veri_tipleri/README.md) | Girdi-işlem-çıktı modeli, `input()` ve `print()`, `int`/`float`/`str`/`bool`, tip dönüşümü, f-string ile biçimlendirme. |
| [M6](../m6_degiskenler_operatorler/README.md) | Değişkenler ve sabitler, aritmetik/karşılaştırma/mantıksal operatörler, işlem önceliği, kayan nokta tuzakları. |
| [M7](../m7_karar_yapilari/README.md) | `if`/`elif`/`else`, iç içe kararlar, koşul sırası, sınır değer testleri; harf notu, artık yıl, üçgen türü, kargo ücreti. |
| [Sprint A](../sprint_a_proje/README.md) | M1–M7 ile çözülen bireysel proje. |
| [M8](../m8_donguler/README.md) | `while` ve `for`, sayaç/toplayıcı/en büyük kalıpları, iz tablosu, `break`/`continue`, iç içe döngüler, listelere giriş. |
| [M9](../m9_fonksiyonlar/README.md) | `def`, parametre ve dönüş değeri, `return` ile `print` farkı, kapsam, docstring, fonksiyonları pytest ile test etme. |
| [M10](../m10_arama/README.md) | Doğrusal ve ikili arama, karşılaştırma sayısı, iz tabloları, `in`, `list.index` ve `bisect`. |
| [M11](../m11_siralama/README.md) | Kabarcık, seçmeli ve eklemeli sıralama; karşılaştırma/takas sayısı, kararlılık, `sorted()` ve `list.sort()`. |
| [M12](../m12_uygulanabilirlik/README.md) | Algoritma seçme ölçütleri, adım sayma, Büyük-O'ya giriş, zaman ölçümü; dört vaka çalışması. |
| [Sprint B](../sprint_b_final_proje/README.md) | Tüm dönemi kapsayan grup projesi, algoritma karşılaştırma raporu ve sunum. |
