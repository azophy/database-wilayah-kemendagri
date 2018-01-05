Indonesian Ministry of Internal Affairs Region Code and Region Name Database
===================
Fork of https://github.com/edwin/database-wilayah-kemendagri.

Sebagai seorang developer freelance, gue beberapa kali harus berurusan dengan data lokasi yang dimiliki klien-klien saya. Kalau sudah berurusan dengan masalah lokasi, seringkali kita juga harus menyimpan data-data detail terkait misalnya provinsi dan/atau kabupaten lokasi yang dimaksud. Untuk memudahkan menyimpan keterangan provinsi dan/atau sampai dengan kelurahan tersebut kita seringkali membutuhkan suatu aturan kode. Salah satu caranya untuk di Amerika Serikat orang seringkali menyingkat kode negara bagian mereka dengan 2 huruf, misal 'TX' untuk Texas dan 'CA' untuk California.

Sebenarnya tidak ada aturan yang baku untuk pembuatan kode ini. Hampir setiap programmer memiliki preferensi masing-masing. Sah-sah saja kalau seorang programmer mau membuat aturan pengkodean sendiri kalau memang itu dirasa nyaman dan memudahkan. Kita bisa saja menggunakan aturan singkatan seperti negara bagian AS tadi, atau memanfaatkan kode nomor telepon misalnya, atau bisa juga memanfaatkan kode pos.

Adapun di proyek ini kita memanfaatkan list kode daerah yang sudah disusun oleh kemendagri untuk digunakan sebagai kode alias dari daerah-daerah tadi. Keuntungan kode dari kemendagri ini adalah antara lain list daerahnya yang cukup lengkap (karena memang dikeluarkan oleh lembaga pemerintahan yang paling berwenang soal pembagian wilayah di Indonesia), dan kode-kodenya digunakan secara luas sebagai kode dalam Nomor Identitas Kependudukan (NIK), alias nomor yang ada di KTP orang Indonesia.

Proyek ini berupaya untuk mengubah database sql yang sudah dibuat oleh agan edwin ( github.com/edwin ) menjadi file-file json siap pakai yang bisa dipakai untuk aplikasi web interaktif (umumnya memanfaatkan teknik-teknik AJAX).

File-file JSON dari proyek ini bisa dipanggil dengan url:
- kode provinsi: rooturl + list_provinsi.json
- kode kabupaten: rooturl + list_kabupaten_<kode_kabupaten>.json
- kode kecamatan: rooturl + list_kabupaten_<kode_kecamatan>.json

Proyek ini memanfaatkan layanan CDN dari rawgit.com, sehingga untuk aksesnya menggunakan rooturl 'https://rawgit.com/azophy/database-wilayah-kemendagri/master/results/'

Proyek ini hanya menyajikan file json sampai level kecamatan saja. Untuk menampilkan sampai level kelurahan silahkan clone proyek ini, hilangkan commant dari blok kode terakhir di generator.py dan generate file2 json kelurahan

File-file json ini hanya berisi 3 kolom: kode_daerah kemendagri, nama daerah, dan url ke file rincian sub-daerah yang bersangkutan (untuk level kecamatan isinya kosong).

Untuk menggenerate sendiri file-file ini, silahkan jalankan script `generator.py`. Script ini memanfaatkan Python 2.7 dengan plugin pymsql (bisa di install dengan pip `pip install pymsql` atau dengan package manager dari OS, misal di ubuntu/debian `sudo apt-get install python-pymysql`.

License
-----------
AGPL . Sedikit penjelasan dari situs AGPL: 

> The GNU Affero General Public License is a modified version of the ordinary GNU GPL version 3. It has one added requirement: if you run a modified program on a server and let other users communicate with it there, your server must also allow them to download the source code corresponding to the modified version running there.

Examples
----------

Revisions
-------------------
* 22 Oct 2015 - 34 Province, 514 Regencies, 7094 Sub-Districts and 82505 Villages

Appreciations
--------------------
List of regional codes are kindly provided by Indonesian Ministry of Internal Affairs and Gozali Kumara's KawalDesa (https://github.com/ghk/kawaldesa)
Edwin (https://github.com/edwin) as the one published the SQL version of this list.
