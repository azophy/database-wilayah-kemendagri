import pymysql
import json
import os, glob

# Configuration variables
dbhost = 'localhost'
dbuser = 'root'
dbpass = 'root'
dbname = 'wilayah_indonesia'

base_cdn_url = 'https://rawgit.com/azophy/database-wilayah-kemendagri/master/results/'
resdir = 'results/' # folder untuk menyimpan file2 json hasil export
prov_filename = 'list_provinsi'
kab_filename = 'list_kabupaten_'
kec_filename = 'list_kecamatan_'
kel_filename = 'list_kelurahan_'

# kosongkan folder hasil
files = glob.glob(resdir + '/*')
for f in files:
    os.remove(f)

# koneksi database
db = pymysql.connect(host=dbhost, user=dbuser, passwd=dbpass, db=dbname)
cur = db.cursor()

def export_json(content, filename):
    with open(filename, 'w') as f:
        json.dump(content, f)

# buat list provinsi
cur.execute("SELECT * FROM tbl_regions WHERE parent_code='0'")
rows = cur.fetchall()
all_provinsi = []
for row in rows:
    all_provinsi.append( [ row[1], row[2], base_cdn_url + kab_filename + row[1] + '.json' ] )
export_json(all_provinsi, resdir + prov_filename + '.json')

# buat list kabupaten
all_kabupaten = []
for provinsi in all_provinsi:
    cur.execute("SELECT * FROM tbl_regions WHERE parent_code='"+provinsi[0] + "'")
    rows = cur.fetchall()
    kabupaten = []
    for row in rows:
        kabupaten.append( [ row[1], row[2], base_cdn_url + kec_filename + row[1] + '.json' ] )
    export_json(kabupaten, resdir + kab_filename + provinsi[0] + '.json')
    all_kabupaten += kabupaten

# buat list kecamatan
all_kecamatan = []
for kabupaten in all_kabupaten:
    cur.execute("SELECT * FROM tbl_regions WHERE parent_code='"+kabupaten[0] + "'")
    rows = cur.fetchall()
    kecamatan = []
    for row in rows:
        kecamatan.append( [ row[1], row[2], None ] )
        # kecamatan.append( [ row[1], row[2], base_cdn_url + kel_filename + row[1] + '.json' ] )
    export_json(kecamatan, resdir + kec_filename + kabupaten[0] + '.json')
    all_kecamatan += kecamatan

# buat list kelurahan
# all_kelurahan = []
# for kecamatan in all_kecamatan:
#     cur.execute("SELECT * FROM tbl_regions WHERE parent_code='"+kecamatan[0] + "'")
#     rows = cur.fetchall()
#     kelurahan = []
#     for row in rows:
#         kelurahan.append( [ row[1], row[2], None ] )
#     export_json(kelurahan, resdir + kel_filename + kecamatan[0] + '.json')
#     all_kelurahan += kelurahan
