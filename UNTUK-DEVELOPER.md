# Perubahan yang perlu diterapkan ke pcxtrader.com

Diperbarui 15 September 2026. Sumber kebenaran ada di repo ini, folder `site/`.

Situs statis di repo ini sudah memuat semua perubahan di bawah. pcxtrader.com
masih memakai angka lama. Daftar ini menyebut teks persisnya supaya bisa dicari
langsung di kode kalian.

Ada tiga perubahan. Yang pertama paling besar karena satu angka menarik banyak
angka lain.

---

## 1. Spread akun Standard: 1.0 pips menjadi 1.5 pips

### 1a. Penyebutan spread

Ganti di mana pun muncul:

| Sebelum | Sesudah |
|---|---|
| `from 1.0 pips` | `from 1.5 pips` |
| `Spreads from 1.0 pips` | `Spreads from 1.5 pips` |
| `1.0 pips (EURUSD)` | `1.5 pips (EURUSD)` |
| `Spread from 1.0 pip` | `Spread from 1.5 pips` (perhatikan, "pip" jadi "pips") |

Halaman yang memuatnya: Standard, Accounts, ECN, Demo, Precious Metals, dan
beranda. Termasuk `<meta name="description">` halaman Standard dan blok
`application/ld+json` di halaman yang sama.

**Jangan ikut diubah:** di beranda ada kartu harga pasar yang menampilkan
`AUDUSD ... Spread 1.0 pips`. Itu spread instrumen AUDUSD, satu keluarga dengan
EURUSD 0.2 dan GBPUSD 0.7, bukan spread akun Standard.

### 1b. Angka yang ikut berubah karena diturunkan dari spread

Dasar hitungannya: satu standard lot EURUSD, 1 pip = $10. Jadi 1.5 pip = $15.

| Tempat | Sebelum | Sesudah |
|---|---|---|
| Kuitansi Standard, halaman Standard dan Accounts | `$10.00` | `$15.00` |
| Accounts, blok "We did the math against ourselves" | `about $3 less per lot, roughly 30%` | `about $8 less per lot, roughly 53%` |
| Accounts, ringkasan versi ponsel | `$10.00 vs $7.00 per lot` | `$15.00 vs $7.00 per lot` |
| Accounts, paragraf penutup | `Three dollars per lot is about $60 a month if you trade 20 lots.` | `Eight dollars per lot is about $160 a month if you trade 20 lots.` |
| ECN, tabel "The difference at your volume" | `$3` `$30` `$60` `$150` | `$8` `$80` `$160` `$400` |
| ECN, catatan kaki | `starting spread: $10.00 versus $7.00 per lot` | `starting spread: $15.00 versus $7.00 per lot` |
| Standard, FAQ "What does one lot cost on Standard?" | `At the starting spread of 1.0 pips, one standard lot of EURUSD costs $10.00` | `At the starting spread of 1.5 pips, one standard lot of EURUSD costs $15.00` |
| Standard, FAQ "Is there any commission on the Standard account?" | `the spread, from 1.0 pips` | `the spread, from 1.5 pips` |
| Standard, blok `application/ld+json` | dua pertanyaan di atas dan `feesAndCommissionsSpecification` | ikut disesuaikan |

Dua kalimat berubah kata, bukan cuma angka: **Three dollars** menjadi **Eight
dollars**, dan **roughly 30%** menjadi **roughly 53%**.

### 1c. Bar perbandingan di halaman Accounts

Bar di bawah kedua total dihitung dari nilai totalnya, bukan dari lebar yang
ditulis tangan. Kalau implementasi kalian juga menghitung dari nilai, tidak ada
yang perlu disentuh. Kalau lebarnya ditulis manual, sesuaikan: porsi navy
menjadi 46,7% dari bar, yaitu $7 dari $15, sisanya ekor emas.

Bar pada tabel volume di halaman ECN tidak berubah, karena seluruh nilainya
naik dengan kelipatan sama sehingga proporsinya tetap.

---

## 2. Gambar angka di halaman Standard

Ini yang paling mudah terlewat, karena angkanya ada **di dalam gambar**, bukan
di teks, jadi tidak akan ketemu waktu mencari string.

| | |
|---|---|
| Berkas lama | `assets/prop-one-number.webp` — ilustrasi 3D bertuliskan **1.0** |
| Berkas baru | `assets/prop-one-number-v2.webp` — bertuliskan **1.5**, tersedia di repo ini |
| Ukuran | 492 x 420, praktis sama dengan yang lama (491 x 420), jadi tata letak tidak bergeser |
| Teks alt | `One number: 1.5.` |

Nama berkasnya sengaja dibedakan, bukan ditimpa, supaya cache browser dan CDN
tidak menyajikan gambar lama. Tolong jangan dikembalikan ke nama lama.

---

## 3. Kartu Precious Metals di halaman Standard

Kartu "akun lain" di bagian bawah halaman Standard masih mengutip angka untuk
emas, padahal spesifikasi akun itu sendiri berbunyi Raw spread dan Floating.
Spread mengambang tidak punya angka awal untuk dikutip.

| Sebelum | Sesudah |
|---|---|
| `gold from 10 cents + $7 per lot` | `raw gold spread + $7 per lot` |

Halaman Demo dan Precious Metals sudah memakai bahasa yang benar, jadi yang
perlu diubah hanya satu tempat di halaman Standard.

---

## Cara tercepat menerapkannya

Semua halaman final ada di folder `site/`. Nama berkasnya mengikuti URL:

    site/index.html                     →  /
    site/accounts.html                  →  /accounts
    site/accounts-standard.html         →  /accounts/standard
    site/accounts-ecn.html              →  /accounts/ecn
    site/accounts-demo.html             →  /accounts/demo
    site/accounts-precious-metals.html  →  /accounts/precious-metals
    site/legal-*.html                   →  /legal/*

Ambil teks dan angkanya dari sana, jangan dari ingatan atau dari versi lama.
Aset gambar ada di `site/assets/`.

## Cara memastikan sudah benar

Setelah rilis, cari di halaman yang sudah tayang. Yang berikut ini **harus nol
hasil**:

    1.0 pips        (kecuali kartu harga AUDUSD di beranda)
    $10.00
    about $3 less
    roughly 30%
    Three dollars
    $60 a month
    $150
    gold from 10 cents
    prop-one-number.webp

Dan yang berikut **harus ada**:

    1.5 pips        di Standard, Accounts, ECN, Demo, Precious Metals, beranda
    $15.00          di Standard dan Accounts
    roughly 53%     di Accounts
    $160 a month    di Accounts
    $400            di tabel volume halaman ECN
    prop-one-number-v2.webp   di Standard

## Catatan

Angka komisi ECN $7 per lot dan spread ECN 0.0 pips **tidak berubah** pada
perubahan ini. Begitu juga minimum deposit: Standard $10, ECN $100, Precious
Metals $1,000, Demo $0.

Leverage masih dibahas terpisah dan belum final, jadi biarkan seperti sekarang
sampai ada kabar lanjutan.
