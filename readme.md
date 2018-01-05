Indonesian Ministry of Internal Affairs Region Code and Region Name Database
===================
Fork of https://github.com/edwin/database-wilayah-kemendagri.

Proyek ini berupaya untuk mengubah database sql yang sudah dibuat oleh agan edwin ( github.com/edwin ) menjadi file-file json siap pakai yang bisa dipakai untuk aplikasi web interaktif (umumnya memanfaatkan teknik-teknik AJAX)

File-file JSON dari proyek ini bisa dipanggil dengan url:
- kode provinsi: rooturl + list_provinsi.json
- kode kabupaten: rooturl + list_kabupaten_<kode_kabupaten>.json
- kode kecamatan: rooturl + list_kabupaten_<kode_kecamatan>.json

Proyek ini memanfaatkan layanan CDN dari rawgit.com, sehingga untuk aksesnya menggunakan rooturl 'https://rawgit.com/azophy/database-wilayah-kemendagri/master/results/'

Proyek ini hanya menyajikan file json sampai level kecamatan saja. Untuk menampilkan sampai level kelurahan silahkan clone proyek ini, hilangkan commant dari blok kode terakhir di generator.py dan generate file2 json kelurahan

File-file json ini hanya berisi 3 kolom: kode_daerah kemendagri, nama daerah, dan url ke file rincian sub-daerah yang bersangkutan (untuk level kecamatan isinya kosong).

Untuk menggenerate sendiri file-file ini, silahkan jalankan script `generator.py`. Script ini memanfaatkan Python 2.7 dengan plugin pymsql (bisa di install dengan pip `pip install pymsql` atau dengan package manager dari OS, misal di ubuntu/debian `sudo apt-get install python-pymysql`.

License: LGPL

Examples
----------

Revisions
-------------------
* 22 Oct 2015 - 34 Province, 514 Regencies, 7094 Sub-Districts and 82505 Villages

Appreciations
--------------------
List of regional codes are kindly provided by Indonesian Ministry of Internal Affairs and Gozali Kumara's KawalDesa (https://github.com/ghk/kawaldesa)
Edwin (https://github.com/edwin) as the one published the SQL version of this list.
