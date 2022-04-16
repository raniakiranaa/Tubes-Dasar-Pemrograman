import fungsiDasar as fd
import fungsiBuatan as fb
import register as reg
import login as login
import addGame as ag
import ubahGame as ug
import ubahStok as us
import listingGame as lg
import beliGame as bg
import lihatGameSudahDibeli as lgsd
import topup
import history
import help as help
import exit
import cipher as cp
import magicConchShell as mcs

_role = "user"
_loggedIn = False
_valCommand = ["register", "login", ""]
_loggedUser = ["1", "2", "3", "4", "5", 0]
"""Data user yang telah login
1 : id
2 : username
3 : nama
4 : password
5 : role (admin/user)
6 : saldo
"""


_usersData = [["1", "2", "3", "4", "5", 0]]
"""Diimport dari user.csv sebagai variabel global
1 : id
2 : username
3 : nama
4 : password
5 : role (admin/user)
6 : saldo
"""

_gameData = [["1", "2", "3", 2000, 0, 0]]
"""Diimport dari game.csv sebagai variabel global
1 : id
2 : nama
3 : kategori
4 : tahun rilis
5 : harga
6 : stok
"""

_history = [["1", "2", 0, "4", 2000]]
"""Diimport dari riwayat.csv sebagai variabel global
1 : id game
2 : nama game
3 : harga game
4 : id pembeli
5 : tahun pembelian
"""

_possession = [["1", "2"]]
"""Diimport dari kepemilikan.csv sebagai variabel global
1 : id game
2 : id pemilik
"""

def mintaCommand():
    global _role, _loggedIn, _usersData, _gameData, _history, _possession, running
    command = input(">>> ").lower()
    if _loggedIn:
        if login.isValid(_role, command): #validasi perintah admin dan user
            if command == "register":
                _usersData = reg.register(_usersData)
            elif command == "login":
                print('Anda sudah login! Untuk melihat list command, ketik "help".')
            elif command == "ubah_game":    # Mengubah spesifikasi data game
                ug.ubahGame(_gameData)
            elif command == "ubah_stok":    # Mengubah data stok game
                us.ubahStok(_gameData)
            elif command == "listing_game_toko":    # Melihat daftar game yang ada     
                lg.listing_game(_gameData)
            elif command == "buy_game":
                _wanted = input("Masukkan ID Game: ")               # Membeli game
                if(bg.beli(_wanted,_loggedUser, _possession, _gameData, _usersData, _history)):
                    _history     = bg._ubahHistory(_wanted, _loggedUser, _possession, _gameData, _usersData, _history)
                    _gameData    = bg._ubahGameData(_wanted, _loggedUser, _possession, _gameData, _usersData, _history)
                    _loggedUser  = bg._ubahLoggedUsers(_wanted, _loggedUser, _possession, _gameData, _usersData, _history)
                    _usersData   = bg._ubahUsersData(_wanted, _loggedUser, _possession, _gameData, _usersData, _history)
                    _possession  = bg._ubahPossession(_wanted, _loggedUser, _possession, _gameData, _usersData, _history) 
            elif command == "list_game":
                lgsd.lihat(_loggedUser[0],_gameData,_possession)    # melihat daftar game yang dimiliki 
            elif command == "help":     # melihat list command
                help.help(_role)
            elif command == "exit": 
                running = exit.exit()
            elif command == "kerangajaib":
                mcs.kerangAjaib()                                   # Kerang Ajaib
        else: # command tidak valid dengan _role
            pass
    
    else: #_loggedIn = False
        if command == "login":      
            _loggedUser = login.login(_usersData)
            if _loggedUser != None: #username dan password sudah tervalidasi
                _role = _loggedUser[4]
                _loggedIn = True
        elif command == "help":     # melihat list command
            help.help(_role)                         
        else:
            # validasi perintah, tidak boleh melakukan apa-apa sebelum login KECUALI HELP
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')

            



running = True


if __name__ == "__main__":                          # Inti program
    # load.load()
    while running:
        mintaCommand()

    print("Selamat menikmati hari anda :(")
