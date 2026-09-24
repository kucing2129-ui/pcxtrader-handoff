# Perubahan yang perlu diterapkan ke pcxtrader.com

Diperbarui 24 September 2026. Sumber kebenaran ada di repo ini, folder `site/`.

Putaran sebelumnya, yaitu spread Standard 1.5 pips, gambar angka, dan kartu
Precious Metals, **sudah kalian terapkan dan sudah tayang**. Terima kasih.
Dokumen ini hanya berisi yang baru.

---

## PENTING: jangan terapkan dengan menimpa halaman

pcxtrader.com sekarang memuat beberapa hal yang **tidak ada di repo ini**,
karena kalian yang menambahkannya. Kalau halaman di sini disalin bulat bulat,
semuanya hilang.

Yang wajib dipertahankan:

| Fitur di pcxtrader.com | Keterangan |
|---|---|
| **Pemilih bahasa English / 中文** | Tidak ada di repo ini sama sekali |
| **Daftar yurisdiksi tanpa China** | Repo ini masih memuat China. Milik kalian yang benar, jangan ikut diganti |
| Penyamaran alamat email oleh Cloudflare | Biarkan apa adanya |

Jadi perlakukan dokumen ini sebagai **daftar tambalan**, bukan perintah ganti
berkas. Ambil potongan yang disebut, tempel ke halaman kalian.

---

## Satu perubahan: akun keempat, Bonus Account

Akun baru bernama **Bonus Account**, karakter **Lin**. Harganya sama persis
dengan Standard, yang membedakan hanya minimum deposit.

| Hal | Nilai |
|---|---|
| Spread | from 1.5 pips |
| Commission | $0 |
| Leverage | up to 1:500 |
| Minimum deposit | **$1,500** |
| Sisanya, mulai dari eksekusi sampai instrumen | identik dengan Standard |

### 1. Kartu akun di beranda dan di halaman Accounts

Kartu keempat, diletakkan **setelah Precious Metals**. Isinya:

    LIN
    Bonus Account
    Bonuses land in this account.*
    SPREADS FROM  1.5 pips
    Min deposit   $1,500
    Commission    $0
    Leverage      up to 1:500
    *Terms and conditions apply.
    Not for you if you are just trying things out. This one is for when you are ready.
    [ Open Account ]

Catatan bentuk:

- Kartu ini **tidak punya tautan "See full details"**, karena halaman
  `/accounts/bonus` memang belum ada. Di repo ini tempatnya diisi elemen kosong
  setinggi baris itu, supaya tombol Open Account tetap sejajar dengan tiga
  kartu lain. Kalau tata letak kalian memakai cara lain, silakan, yang penting
  tombolnya tetap sejajar.
- Warna kartunya ivory, berbeda dari navy milik ECN, porselen milik Standard,
  dan emas milik Precious Metals.
- Gambar karakternya `assets/card-lin-v2.webp`, 638 x 900, sama seperti kartu
  cast lain.

### 2. Tabel perbandingan di halaman Accounts

Tambah **kolom kelima** berjudul `Bonus Account`, setelah Precious Metals.
Isinya menyalin kolom Standard, **kecuali satu baris**:

| Baris | Nilai |
|---|---|
| Minimum deposit | **$1,500** |
| Semua baris lain | sama persis dengan kolom Standard |

Judul kelompok baris, yaitu Pricing, Execution, Requirements dan Options,
tadinya `colspan="5"`, sekarang `colspan="6"`.

Di tampilan ponsel tabel ini berubah jadi satu kolom dengan tombol pemilih di
atasnya. Tambahkan satu tombol lagi berlabel **Bonus Account**.

Judul kolom Bonus Account **tidak ditautkan** ke halaman mana pun, sedangkan
tiga judul lain tertaut. Itu memang disengaja, karena halamannya belum ada.

### 3. Menu dan footer

- **Dropdown Accounts di navbar**: tambah item keenam, **Bonus Account**,
  setelah Demo
- **Footer kolom Accounts**: tambah **Bonus Account** setelah Precious Metals
- Keduanya mengarah ke kartu di halaman Accounts, yaitu `/accounts#bonus`.
  Kartu Bonus Account di halaman itu diberi `id="bonus"`

### 4. Hitungan akun

Situs sekarang punya empat akun live. Dua kalimat berubah:

| Tempat | Sebelum | Sesudah |
|---|---|---|
| Beranda, di bawah "Every trader started where you are." | `Three accounts and a free demo.` | `Four accounts and a free demo.` |
| Halaman Accounts, kalimat pembuka | `Three live accounts and one free demo.` | `Four live accounts and one free demo.` |
| Halaman Accounts, `<meta name="description">` | `Three live accounts and a free demo.` | `Four live accounts and a free demo.` |

### 5. Kartu "akun lain" di halaman akun

Di bagian bawah halaman Standard, ECN, Demo, dan Precious Metals ada deretan
kartu kecil berisi akun lainnya. Tambahkan satu kartu di setiap halaman:

    Bonus Account
    from 1.5 pips, $1,500 minimum

Mengarah ke `/accounts#bonus`.

### 6. Foto bersama cast di halaman Accounts

Diganti versi berlima, Lin ikut berdiri di ujung kanan:
`assets/cast-group-v3.webp`. Berkas lama `cast-group.webp` masih dipakai
sebagai dasar, jadi jangan dihapus.

### 7. Data SEO

Tambahkan satu blok `application/ld+json` di halaman Accounts:

```json
{"@context":"https://schema.org","@graph":[
{"@type":"FinancialProduct","name":"PCX Bonus Account",
 "provider":{"@type":"Organization","name":"Prime Codex Ltd","alternateName":"PCX"},
 "url":"https://pcxtrader.com/accounts#bonus",
 "feesAndCommissionsSpecification":"Spreads from 1.5 pips with no commission. Minimum deposit $1,500. Maximum leverage up to 1:500. Bonus campaigns apply; terms and conditions apply."}]}
```

---

## Dua perbaikan tampilan, berlaku untuk semua kartu akun

Ditemukan dari tangkapan layar ponsel, dan sudah diperbaiki di repo ini.

**Gambar karakter di ponsel.** Di bawah 768px, gambar di semua kartu akun
tingginya 196px. Kartu baru sempat memakai ukuran desktop dan terlihat lebih
besar sendiri. Pastikan aturan ponsel kalian mencakup kartu keempat.

**Baris dalam kartu harus mulai di ketinggian sama.** Kutipan di bawah judul
ada yang satu baris ada yang dua, dan baris catatan seperti
"+ $7 commission per lot" hanya ada di sebagian kartu. Akibatnya daftar
spesifikasi dan tombol tidak sejajar antar kartu. Di repo ini blok kutipan
selalu menyediakan ruang dua baris, dan kartu tanpa catatan diberi baris kosong
setinggi satu baris.

## Satu perbaikan yang berlaku untuk seluruh situs

Di Chrome Android, mode gelap otomatis membalik warna halaman mana pun yang
tidak menyatakan skemanya, dan situs ini jadi tampil gelap. Tambahkan dua meta
ini di setiap halaman:

```html
<meta name="color-scheme" content="light">
<meta name="theme-color" content="#FAF6EF">
```

---

## Berkas gambar baru

| Berkas | Isi |
|---|---|
| `assets/card-lin-v2.webp` | Lin untuk kartu akun, 638 x 900 |
| `assets/cast-group-v3.webp` | Foto bersama berlima |

Keduanya ada di `site/assets/` di repo ini.

## Cara memastikan sudah benar

Setelah rilis, cari di halaman yang sudah tayang.

Harus **nol hasil**:

    Three accounts
    Three live accounts

Harus **ada**:

    Bonus Account        di 13 halaman, lewat navbar dan footer
    $1,500               di beranda dan halaman Accounts
    card-lin-v2.webp     di beranda dan halaman Accounts
    cast-group-v3.webp   di halaman Accounts
    color-scheme         di 13 halaman

Dan pastikan **masih ada**:

    Pemilih bahasa English / 中文
    Daftar yurisdiksi tanpa China

## Catatan

Situs menyebut Bonus Account, tetapi belum ada halaman yang menjelaskan
bonusnya. Tanda bintang di kartu mengarah ke syarat yang halamannya belum
dibuat. Itu disadari dan sedang dibahas terpisah.
