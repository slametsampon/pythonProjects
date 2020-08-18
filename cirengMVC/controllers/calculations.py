class Calculations:

    def __init__(self,app):
        self.app = app
        self.__jumlahCireng = 0
        self.__hargaJual = 0

    #global function/methode
    def hitungHargaUnit(self):
        daftarBahan = self.app.bahan.bacaSemuaBahan()
        daftarBahan['CJ']['biayaUnit'] = 0
        for bahan in daftarBahan:
            if daftarBahan[bahan]['FaktorHarga'] > 0:
                daftarBahan[bahan]['HargaSatuan'] = int(daftarBahan[bahan]['HargaBeli'] / daftarBahan[bahan]['FaktorHarga'])
                daftarBahan[bahan]['FaktorMenu'] = daftarBahan[bahan]['QtyMenu'] / daftarBahan['CJ']['QtyMenu']
                daftarBahan[bahan]['biayaUnit'] = int((daftarBahan[bahan]['HargaSatuan'] * daftarBahan[bahan]['QtyMenu']) / daftarBahan['CJ']['QtyMenu'])
                daftarBahan['CJ']['biayaUnit'] += daftarBahan[bahan]['biayaUnit']

        kemasan = self.app.kemasan.bacaKemasan()
        kemasan['biayaTotal'] = (kemasan['qty'] * daftarBahan['CJ']['biayaUnit']) + kemasan['biayaKemasan']

    def hitungBiaya(self):
        daftarBahan = self.app.bahan.bacaSemuaBahan()
        daftarBahan['CJ']['Biaya'] = 0
        for bahan in daftarBahan:
                daftarBahan[bahan]['Qty'] = int(daftarBahan[bahan]['FaktorMenu'] * self.__jumlahCireng)
                daftarBahan[bahan]['Biaya'] = int(daftarBahan[bahan]['Qty'] * daftarBahan[bahan]['HargaSatuan'])
                daftarBahan['CJ']['Biaya'] += daftarBahan[bahan]['Biaya']
        daftarBahan['CJ']['Qty'] = self.__jumlahCireng

    def hitungUtungRugi(self):
        jumlahKemasan = int(self.__jumlahCireng/self.app.kemasan.bacaNilaiKemasan('qty'))
        sisaCireng = int(self.__jumlahCireng % self.app.kemasan.bacaNilaiKemasan('qty'))
        hargaJualTotal = jumlahKemasan*self.__hargaJual
        biayaTotal = jumlahKemasan*self.app.kemasan.bacaNilaiKemasan('biayaKemasan')+self.app.bahan.bacaNilaiBahan('CJ','Biaya')
        untungRugi = hargaJualTotal - biayaTotal
        
        self.app.hasil.ubahNilaiHasil('jumlahKemasan',jumlahKemasan)
        self.app.hasil.ubahNilaiHasil('sisaCireng',sisaCireng)
        self.app.hasil.ubahNilaiHasil('hargaJualTotal',hargaJualTotal)
        self.app.hasil.ubahNilaiHasil('biayaTotal',biayaTotal)
        self.app.hasil.ubahNilaiHasil('untungRugi',untungRugi)

    def setJumlahCireng(self,val):
        self.__jumlahCireng = val

    def getJumlahCireng(self):
        return self.__jumlahCireng

    def setHargaJual(self,val):
        self.__hargaJual = val

    def getHargaJual(self):
        return self.__hargaJual
        