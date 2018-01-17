Indonesian Ministry of Internal Affairs Region Code and Region Name Database
===================
Fork of https://github.com/edwin/database-wilayah-kemendagri.

Sebagai seorang developer freelance, saya beberapa kali harus berurusan dengan data lokasi yang dimiliki klien-klien saya. Kalau sudah berurusan dengan masalah lokasi, seringkali kita juga harus menyimpan data-data detail terkait misalnya provinsi dan/atau kabupaten lokasi yang dimaksud. Untuk memudahkan menyimpan keterangan provinsi dan/atau sampai dengan kelurahan tersebut kita seringkali membutuhkan suatu aturan kode. Salah satu caranya untuk di Amerika Serikat orang seringkali menyingkat kode negara bagian mereka dengan 2 huruf, misal 'TX' untuk Texas dan 'CA' untuk California.

Sebenarnya tidak ada aturan yang baku untuk pembuatan kode ini. Hampir setiap programmer memiliki preferensi masing-masing. Sah-sah saja kalau seorang programmer mau membuat aturan pengkodean sendiri kalau memang itu dirasa nyaman dan memudahkan. Kita bisa saja menggunakan aturan singkatan seperti negara bagian AS tadi, atau memanfaatkan kode nomor telepon misalnya, atau bisa juga memanfaatkan kode pos.

Adapun di proyek ini kita memanfaatkan list kode daerah yang sudah disusun oleh kemendagri untuk digunakan sebagai kode alias dari daerah-daerah tadi. Keuntungan kode dari kemendagri ini adalah antara lain list daerahnya yang cukup lengkap (karena memang dikeluarkan oleh lembaga pemerintahan yang paling berwenang soal pembagian wilayah di Indonesia), dan kode-kodenya digunakan secara luas sebagai kode dalam Nomor Identitas Kependudukan (NIK), alias nomor yang ada di KTP orang Indonesia.

Proyek ini berupaya untuk mengubah database sql yang sudah dibuat oleh agan edwin ( github.com/edwin ) menjadi file-file json siap pakai yang bisa dipakai untuk aplikasi web interaktif (umumnya memanfaatkan teknik-teknik AJAX).

File-file JSON dari proyek ini bisa dipanggil dengan url:
- kode provinsi: rooturl + list_provinsi.json
- kode kabupaten: rooturl + list_kabupaten_<kode_kabupaten>.json
- kode kecamatan: rooturl + list_kabupaten_<kode_kecamatan>.json

Proyek ini memanfaatkan layanan CDN dari rawgit.com, sehingga untuk aksesnya menggunakan rooturl 'https://cdn.rawgit.com/azophy/database-wilayah-kemendagri/<versi terakhir>/results/'. Versi terakhir yang dapat digunakan saat ini adalah versi `v0.3`.

Proyek ini hanya menyajikan file json sampai level kecamatan saja. Untuk menampilkan sampai level kelurahan silahkan clone proyek ini, hilangkan commant dari blok kode terakhir di generator.py dan generate file2 json kelurahan

File-file json ini hanya berisi 3 kolom: kode_daerah kemendagri, nama daerah, dan url ke file rincian sub-daerah yang bersangkutan (untuk level kecamatan isinya kosong).

Untuk menggenerate sendiri file-file ini, silahkan jalankan script `generator.py`. Script ini memanfaatkan Python 2.7 dengan plugin pymsql (bisa di install dengan pip `pip install pymsql` atau dengan package manager dari OS, misal di ubuntu/debian `sudo apt-get install python-pymysql`.

License
-----------
AGPL . Sedikit penjelasan dari situs AGPL: 

> The GNU Affero General Public License is a modified version of the ordinary GNU GPL version 3. It has one added requirement: if you run a modified program on a server and let other users communicate with it there, your server must also allow them to download the source code corresponding to the modified version running there.

Example: Meload data2 di atas menggunakan JQuery
---------

Contoh ini juga dapat dilihat di http://cdn.rawgit.com/azophy/database-wilayah-kemendagri/v0.3/example.html .

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
<body>
    <form action="#">
        <label for="provinsi">Provinsi</label>
        <select id="provinsi" name="provinsi"></select>

        <label for="kabupaten">Kabupaten</label>
        <select id="kabupaten" name="kabupaten"></select>

        <label for="kecamatan">Kecamatan</label>
        <select id="kecamatan" name="kecamatan"></select>

        <button type="submit">Search</button>
    </form>
</body>
<script>
    var rootAreaCodeUrl = 'http://cdn.rawgit.com/azophy/database-wilayah-kemendagri/v0.2/results/';

    // load provinsi on page load
    $(document).ready(function() {
        // init provinsi dropdown
        $.ajax({
            url: rootAreaCodeUrl + 'list_provinsi.json',
            dataType: 'json',
            type: 'get',
            cache: false,
            success: function(content){
                content.forEach(function(v,i) {
                    $('#provinsi').append('<option value="' + v[0] + '">' + v[1] + '</option>' + "\n");
                });
                    
                $('#provinsi').trigger('change');
            },
        });
    });
    
    // load labupaten list
    $('#provinsi').on('change', function() {
        $.ajax({
            url: rootAreaCodeUrl + 'list_kabupaten_' +$('#provinsi').val() + '.json',
            dataType: 'json',
            type: 'get',
            cache: false,
            success: function(content){
                $('#kabupaten').html('');
                content.forEach(function(v,i) {
                    $('#kabupaten').append('<option value="' + v[0] + '">' + v[1] + '</option>' + "\n");
                });
                    
                $('#kabupaten').trigger('change');
            },
        });
    });
    
    // load kecamatan list
    $('#kabupaten').on('change', function() {
        $.ajax({
            url: rootAreaCodeUrl + 'list_kecamatan_' +$('#kabupaten').val() + '.json',
            dataType: 'json',
            type: 'get',
            cache: false,
            success: function(content){
                $('#kecamatan').html('');
                content.forEach(function(v,i) {
                    $('#kecamatan').append('<option value="' + v[0] + '">' + v[1] + '</option>' + "\n");
                });
            },
        });
    });

</script>
</html>
```

Examples: Menggenerate sendiri file2 json
----------
Pertama-tama pastikan dahulu semua program yang dibutuhkan sudah di-install. Program-program yang harus disiapkan:
- MySql
- Python 2.7
- module python-pymsql
- Git

Silahkan googling dahulu cara menginstall program-program tersebut jika belum ada.

Selanjutnya clone dahulu repository ini kemudian import file sql nya. Kode dibawah mengasumsikan kita memiliki database mysql dengan user: root, password: root, dan kita sudah membuat database dengan nama 'wilayah_indonesia'. 

```bash
git clone git@github.com:azophy/database-wilayah-kemendagri.git
mysql -u root -p wilayah_indonesia < tbl_regions.sql
```
Setelah import selesai (yang saya membutuhkan waktu yang luar biasa lama, di https://dba.stackexchange.com/q/17367 ada trik-trik untuk memantau progres import kita kalau dirasa terlalu lama), kita cek dahulu variabel-variabel di file `generator.py` yang perlu disesuaikan. Yang paling penting jelas adalah variabel-variabel yang berkaitan dengan koneksi database (host, username, password, nama database). Variabel-variabel yang lain harusnya tidak perlu diubah.

Setelah di periksa dan tidak ada masalah, masuk ke folder database-wilayah-kemendagri dan jalankan generator.py

```sh
cd database-wilayah-kemendagri
python generator.py
```

Setelah selesai maka file-file json di folder 'results' akan berisi file-file hasil generate terbaru.

Revisions
-------------------
* 22 Oct 2015 - 34 Province, 514 Regencies, 7094 Sub-Districts and 82505 Villages

Appreciations
--------------------
List of regional codes are kindly provided by Indonesian Ministry of Internal Affairs and Gozali Kumara's KawalDesa (https://github.com/ghk/kawaldesa)
Edwin (https://github.com/edwin) as the one published the SQL version of this list.
