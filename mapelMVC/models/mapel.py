class Mapel:
    KEY = 'mapel'
    def __init__(self):
        self.__daftarMapel = {}
        self.__tabelMapel = []
        self.__maxMapel = 0

    #membuat daftar mapel (Buat/Create)
    def buatMapel(self,hari,*daftarMapel):
        mapel = {}
        if (len(daftarMapel)) >= 1:
            i = 0
            for mpl in daftarMapel:
                i += 1
                key = f'{self.KEY}{i}'
                mapel[key] = mpl
                if i > self.__maxMapel:
                    self.__maxMapel = i

            self.__daftarMapel[hari] = mapel

    #membaca table mapel (Baca/Read)
    def bacaTabelMapel(self):
        maxMapel = self.__maxMapel
        key = self.KEY
        self.__tabelMapel.append(list(self.__daftarMapel.keys()))

        i = 0
        tblMpl = []
        for i in range(1, maxMapel+1):            
            for hari in self.__daftarMapel:
                hariMapel = len(self.__daftarMapel[hari])
                if i <= hariMapel:
                    tblMpl.append(self.__daftarMapel[hari][f'{key}{i}'])
                else:
                    tblMpl.append('')
            
            tblTemp = tblMpl.copy()
            self.__tabelMapel.append(tblTemp)
            tblMpl.clear()

        return(self.__tabelMapel)

    #membaca daftar mapel (Baca/Read)
    def bacaMapel (self,hari):
        return self.__daftarMapel[hari]
    
    #membaca daftar mapel (Baca/Read)
    def bacaNilaiMapel (self,hari,key):
        return self.__daftarMapel[hari][key]

    #membaca semua daftar mapel (BacaSemua/ReadAll)
    def bacaSemuaMapel (self):
        return self.__daftarMapel

    #membaca maxMapel
    def bacaMaxMapel (self):
        return self.__maxMapel

    #mengubah daftar mapel (Ubah/Update)
    def ubahMapel (self,hari,key,value):
        self.__daftarMapel[hari][key] = value

    #menghapus daftar mapel (Hapus/Delete)
    def hapusMapel (self,hari):
        self.__daftarMapel.pop(hari)

    #akhir class Mapel

class Sekolah:
    def __init__(self):
        self.__dataSekolah = {}

    #membuat daftar mapel (Buat/Create)
    def buatDataSekolah(self,nama,alamat,kelas):
        self.__dataSekolah['nama'] = nama
        self.__dataSekolah['alamat'] = alamat
        self.__dataSekolah['kelas'] = kelas

    def bacaDataSekolah(self):
        return self.__dataSekolah

    def bacaNilaiDataSekolah(self,key):
        return self.__dataSekolah[key]

    def ubahNilaiDataSekolah(self,key,value):
        self.__dataSekolah[key] = value

class Menu:
    KEY = 'mapel'
    def __init__(self):
        self.__menu = []

    #membuat daftar menu (Buat/Create)
    def buatMapel(self,*daftarMenu):
        if (len(daftarMenu)) >= 1:
            for menu in daftarMenu:
                self.__menu.append(menu)

    def bacaMenu(self):
        return self.__menu
        