# Giriş

Algoritma Tasarımı dersine hoş geldiniz! Bu sayfa dersin nasıl işlediğini ve ilk haftadan önce
yapmanız gereken kurulumları anlatır.

!!! info "Durum"

    Giriş metni hazırlanıyor. Aşağıdaki kurulum listesi kesinleşmiştir.

## 🧰 Kurulum { #kurulum }

Derste kullanılan araçların hepsi ücretsizdir.

| Araç | Ne için | Platform | Gerekli mi? |
|---|---|---|---|
| [Python 3.11+](https://www.python.org/downloads/) | Metin tabanlı programlama | Hepsi | Evet |
| [uv](https://docs.astral.sh/uv/) | Python paket ve sanal ortam yöneticisi | Hepsi | Evet |
| [VS Code](https://code.visualstudio.com/) | Kod editörü | Hepsi | Evet |
| [Git](https://git-scm.com/) | Materyali indirme ve güncelleme | Hepsi | Önerilir |
| [draw.io](https://app.diagrams.net/) | Akış şeması çizimi | Web, masaüstü | Evet |
| [Flowgorithm](http://www.flowgorithm.org/) | Çalıştırılabilir akış şemaları | Sadece Windows | İsteğe bağlı |
| [Python Tutor](https://pythontutor.com/) | Kodu adım adım görselleştirme | Web | Kurulum gerektirmez |

### Kurulumu doğrulama

```bash
python --version   # Python 3.11 veya üstü
uv --version
git --version
```

Ardından repoyu indirip testleri çalıştırın:

```bash
git clone https://github.com/aligunesgit/AlgoritmaTasarimi.git
cd AlgoritmaTasarimi
uv sync
uv run pytest
```

`1 passed` çıktısını görüyorsanız ortamınız hazırdır.
