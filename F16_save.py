import C01_fungsiDasar as fd
import os

def _ubahJadiString(arr):

    _panjang = fd.len(arr)
    _lebar = fd.len(arr[0])
    _data = ''

    for x in range(_panjang):
        for y in range(_lebar):
            _data += str(arr[x][y]) +";"
        _data += "\n"

    return _data


def simpan(_arrData, tipe,cari):

    directory = os.getcwd()
    _daftarFolder = []
    for dirs, in os.walk(directory):
        _daftarFolder += dirs



    if(fd.find(_daftarFolder,cari) != -1):
        # Jika ada folder
        pass

    else:
        # Jika tidak ada folder
        os.makedirs(cari)

    if(tipe == "game"):
        # [["id","nama","kategori","tahun_rilis","harga","stok"]]
        buka = os.path.join(os.getcwd(), cari, "game.csv")
    elif(tipe == "kepemilikan"):
        # [["game_id","user_id"]]
        buka = os.path.join(os.getcwd(), cari, "kepemilikan.csv")
    elif(tipe == "user"):
        # [["id","username","nama","password","role","saldo"]]
        buka = os.path.join(os.getcwd(), cari, "user.csv")
    else:
        # [["game_id","nama","harga","user_id","tahun_beli"]]
        buka = os.path.join(os.getcwd(), cari, "riwayat.csv")

    #_hasil = _ubahJadiString(_gabung) + _ubahJadiString(_arrData)
    # Asumsikan di dalam matriksnya, sudah terdefinisi header
    _hasil = _ubahJadiString(_arrData)
    a = open(buka,"w", encoding='utf-8')        # encoding= utf-8 agar dapat menggunakan tabel ASCII yang lebih luas hingga 1114112 karakter
    a.writelines(_hasil)



