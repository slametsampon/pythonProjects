# import only system from os 
from os import system, name 

class View:

    def __init__(self,app):
        self.app = app

    # define our clear screen function 
    def clearScreen(self): 
    
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
    
        # for mac and linux(here, os.name is 'posix') 
        else: 
            _ = system('clear') 

    def view2D(self,data2D):
        #data2D = self.controller.bahan.bacaSemuaBahan()
        #view bahan
        header = True
        i = 0
        for layerSatu in data2D:
            i += 1
            layerDuaText = f'{i}'
            firstTextLayerDua = True
            if header:
                header = False
                keysLayerDua = data2D[layerSatu].keys()
                headerText = 'No.'
                for key in keysLayerDua:
                    headerText += f'\t{key}'
                print(headerText)
            for layerDua in data2D[layerSatu]:
                layerDuaText += f'\t{data2D[layerSatu][layerDua]}'
            print(layerDuaText)

    def viewInputCireng(self):
        #input jumlah Cireng
        jumlahCireng = int(input('\n\nMasukkan Jumlah Cireng (biji) : '))
        if jumlahCireng <= 0:
            jmlCireng = self.app.bahan.bacaNilaiBahan('CJ','QtyMenu')
            bahanBaku = self.app.bahan.bacaNilaiBahan('TT','QtyMenu')

            jumlahTepung = int(input('Masukkan Jumlah Tepung (gram) : '))
            jumlahCireng = (jumlahTepung*jmlCireng)/bahanBaku

        self.app.hitung.setJumlahCireng(jumlahCireng)

        #input harga jual per kemasan
        biayaCireng = self.app.kemasan.bacaNilaiKemasan('biayaTotal')
        print(f'\nBiaya Cireng Kemasan\tRp.{int(biayaCireng):,d}')
        hargaJual = int(input('Masukkan Harga Jual\tRp.'))

        self.app.hitung.setHargaJual(hargaJual)

    def viewHasil(self):
        jumlahCireng = f'{int(self.app.hitung.getJumlahCireng())}'
        jumlahKemasan = f'{int(self.app.hasil.bacaNilaiHasil("jumlahKemasan"))}'
        sisaCireng = f'{int(self.app.hasil.bacaNilaiHasil("sisaCireng"))}'
        hargaJualTotal = f'Rp.{int(self.app.hasil.bacaNilaiHasil("hargaJualTotal")):,d}'
        biayaTotal = f'Rp.{int(self.app.hasil.bacaNilaiHasil("biayaTotal")):,d}'
        untungRugi = f'Rp.{abs(int(self.app.hasil.bacaNilaiHasil("untungRugi"))):,d}'

        print(f'Jumlah Cireng : {jumlahCireng}')
        print(f'Jumlah Kemasan : {jumlahKemasan}')
        print(f'Sisa Cireng : {sisaCireng}')
        print(f'Harga Jual\t{hargaJualTotal}')
        print(f'Biaya Total\t{biayaTotal}')
        if self.app.hasil.bacaNilaiHasil("untungRugi") > 0 :
            print(f'Untung\t\t{untungRugi}')
        else:
            print(f'Rugi\t\t{untungRugi}')
