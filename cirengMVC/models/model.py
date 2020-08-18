class Bahan:

    def __init__(self):
        self.__daftarBahan = {}

    #membuat daftar bahan (Buat/Create)
    def buatBahan(self,nama,desc,satuan,qtyMenu,hargaBeli,faktorHarga):
        bahan = {
            'Nama' : nama,
            'Desc' : desc,
            'Satuan' : satuan,
            'QtyMenu' : qtyMenu,
            'biayaUnit' : 0, #dihitung kemudian
            'FaktorMenu' : 0, #dihitung kemudian
            'Qty' : 0, #dihitung kemudian
            'Biaya' : 0, #dihitung kemudian
            'HargaBeli' : hargaBeli,
            'FaktorHarga' : faktorHarga,
            'HargaSatuan' : 0 #dihitung kemudian
        }
        self.__daftarBahan[bahan['Nama']] = bahan

    #membaca daftar bahan (Baca/Read)
    def bacaBahan (self,nama):
        return self.__daftarBahan[nama]
    
    #membaca daftar bahan (Baca/Read)
    def bacaNilaiBahan (self,nama,key):
        return self.__daftarBahan[nama][key]

    #membaca semua daftar bahan (BacaSemua/ReadAll)
    def bacaSemuaBahan (self):
        return self.__daftarBahan

    #mengubah daftar bahan (Ubah/Update)
    def ubahBahan (self,nama,key,value):
        self.__daftarBahan[nama][key] = value

    #menghapus daftar bahan (Hapus/Delete)
    def hapusBahan (self,nama):
        self.__daftarBahan.pop(nama)

    #akhir class Bahan

class Kemasan:
    def __init__(self):
        self.__kemasan = {
            'qty' : 10,
            'biayaKemasan' : 500, #haraga beli kemasan berikut kertas minyak, staples dll
            'biayaTotal' : 0 #dihitung kemudian
        }

    #membaca daftar bahan menu(Baca/Read)
    def bacaKemasan (self):
        return self.__kemasan
    
    #membaca daftar bahan menu(Baca/Read)
    def bacaNilaiKemasan (self,key):
        return self.__kemasan[key]

    #mengubah kemasan (Ubah/Update)
    def ubahKemasan (self,key,value):
        self.__kemasan[key] = value

    #akhir class Kemasan

class Hasil:
    def __init__(self):
        self.__hasil = {
            'hargaJualTotal' : 0,#dihitung kemudian
            'jumlahKemasan' : 0,#dihitung kemudian
            'sisaCireng' : 0,#dihitung kemudian
            'untungRugi' : 0,#dihitung kemudian
            'biayaTotal' : 0 #dihitung kemudian
        }

    #membaca Hasil(Baca/Read)
    def bacaHasil (self):
        return self.__hasil
    
    #membaca nilai Hasil(Baca/Read)
    def bacaNilaiHasil (self,key):
        return self.__hasil[key]

    #mengubah nilai Hasil (Ubah/Update)
    def ubahNilaiHasil (self,key,value):
        self.__hasil[key] = value

    #akhir class Hasil

